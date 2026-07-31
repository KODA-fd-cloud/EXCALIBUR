#!/usr/bin/env python3
"""Исследование конфигурации Nginx на сервере."""

from __future__ import annotations

import paramiko


def main() -> int:
    host = "45.11.93.42"
    port = 22
    user = "root"
    password = "#X8R~mJp2hTr"

    print("Connecting to SSH...")
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, user, password)
        
        commands = [
            "ls -la /etc/nginx/sites-enabled",
            "cat /etc/nginx/sites-enabled/* | grep -i -A 10 -B 5 koda-fd.ru",
            "cat /etc/nginx/sites-enabled/*",
            "docker inspect site-app-1 | grep -i mount -A 15"
        ]

        for cmd in commands:
            print(f"\n--- Running: {cmd} ---")
            stdin, stdout, stderr = ssh.exec_command(cmd)
            print(stdout.read().decode("utf-8"))
            print("ERR:", stderr.read().decode("utf-8"))

        ssh.close()
        return 0
    except Exception as e:
        print("Failed:", e)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
