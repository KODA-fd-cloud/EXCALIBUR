#!/usr/bin/env python3
"""Листинг директорий на сервере через SFTP (paramiko)."""

from __future__ import annotations

import paramiko


def main() -> int:
    host = "45.11.93.42"
    port = 22
    user = "root"
    password = "#X8R~mJp2hTr"

    print(f"Connecting to SFTP {host}:{port}...")
    try:
        transport = paramiko.Transport((host, port))
        transport.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)
        print("Logged in successfully!")
        
        # Список файлов в /var/www/html
        print("\nListing /var/www/html:")
        try:
            files = sftp.listdir("/var/www/html")
            for f in files:
                print(f)
        except Exception as e:
            print("Failed /var/www/html:", e)

        # Список файлов в /var/www/html/blog
        print("\nListing /var/www/html/blog:")
        try:
            files = sftp.listdir("/var/www/html/blog")
            for f in files:
                print(f)
        except Exception as e:
            print("Failed /var/www/html/blog:", e)

        sftp.close()
        transport.close()
        return 0
    except Exception as e:
        print("SFTP Connection failed:", e)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
