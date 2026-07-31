#!/usr/bin/env python3
"""Исследование файловой структуры сервера через SSH."""

from __future__ import annotations

import paramiko


def main() -> int:
    host = "45.11.93.42"
    port = 22
    user = "root"
    password = "#X8R~mJp2hTr"

    print(f"Connecting to SSH {host}:{port}...")
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, user, password)
        print("Logged in successfully!")

        # Выполняем команду для поиска путей монтирования докера
        commands = [
            "docker ps",
            "docker inspect blog-wordpress-1 | grep -i mount -A 15",
            "find /var/www -maxdepth 3",
            "find /home -maxdepth 3"
        ]

        for cmd in commands:
            print(f"\n--- Running: {cmd} ---")
            stdin, stdout, stderr = ssh.exec_command(cmd)
            out = stdout.read().decode("utf-8")
            err = stderr.read().decode("utf-8")
            if out:
                print(out)
            if err:
                print("ERR:", err)

        ssh.close()
        return 0
    except Exception as e:
        print("SSH Connection failed:", e)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
