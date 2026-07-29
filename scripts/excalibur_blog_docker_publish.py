#!/usr/bin/env python3
"""Publish Excalibur article via SSH + docker exec (when FTP is blocked)."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import paramiko

from excalibur_blog_wp_publish import build_php, load_article, load_env, project_root


def publish_via_docker(article_dir: Path, env: dict[str, str]) -> str:
    host = env.get("SSH_HOST") or env.get("FTP_HOST")
    port = int(env.get("SSH_PORT", "22"))
    user = env.get("SSH_USER") or env.get("FTP_USER")
    password = env.get("SSH_PASSWORD") or env.get("FTP_PASS")
    container = env.get("DOCKER_WP_CONTAINER", "blog-wordpress-1")
    if not all([host, user, password]):
        raise RuntimeError("SSH_HOST/SSH_USER/SSH_PASSWORD (or FTP_*) required in site.env.local")

    payload = load_article(article_dir)
    php = build_php(payload)
    remote_tmp = f"/tmp/excalibur-publish-{payload['slug']}.php"
    remote_in_container = f"/var/www/html/excalibur-publish-{payload['slug']}.php"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, user, password, timeout=60)

    sftp = ssh.open_sftp()
    with sftp.open(remote_tmp, "w") as f:
        f.write(php)
    sftp.close()

    cmds = [
        f"docker cp {remote_tmp} {container}:{remote_in_container}",
        f"docker exec {container} php {remote_in_container}",
        f"rm -f {remote_tmp}",
        f"docker exec {container} rm -f {remote_in_container}",
    ]
    out_parts: list[str] = []
    for cmd in cmds:
        _, stdout, stderr = ssh.exec_command(cmd, timeout=180)
        exit_code = stdout.channel.recv_exit_status()
        out = stdout.read().decode("utf-8", errors="replace")
        err = stderr.read().decode("utf-8", errors="replace")
        if exit_code != 0:
            ssh.close()
            raise RuntimeError(f"Command failed ({exit_code}): {cmd}\n{out}\n{err}")
        out_parts.append(out.strip())

    ssh.close()
    return "\n".join(p for p in out_parts if p)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-dir", type=Path, required=True)
    args = ap.parse_args()
    root = project_root()
    article_dir = args.article_dir if args.article_dir.is_absolute() else root / args.article_dir
    env = load_env(root)
    if env.get("EXCALIBUR_BLOG_ALLOW_PUBLISH", "").strip().lower() != "yes":
        print("BLOCKER: EXCALIBUR_BLOG_ALLOW_PUBLISH != yes", file=sys.stderr)
        return 1

    out = publish_via_docker(article_dir, env)
    print(out)

    payload = load_article(article_dir)
    permalink = ""
    for line in out.splitlines():
        if line.startswith("permalink="):
            permalink = line.split("=", 1)[1].strip()

    result = {
        "slug": payload["slug"],
        "topic_id": payload["topic_id"],
        "permalink": permalink,
        "cover_evidence": payload.get("cover_evidence", {}),
        "raw_output": out,
        "verdict": "pass" if "OK post=" in out else "fail",
        "method": "ssh_docker_exec",
    }
    (article_dir / "wp-publish-result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return 0 if result["verdict"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
