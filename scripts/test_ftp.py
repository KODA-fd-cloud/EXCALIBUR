#!/usr/bin/env python3
"""Проверка структуры директорий на сервере koda-fd.ru через FTP."""

from __future__ import annotations

from ftplib import FTP


def main() -> int:
    host = "45.11.93.42"
    user = "root"
    password = "#X8R~mJp2hTr"
    
    print(f"Connecting to FTP {host}...")
    try:
        with FTP() as ftp:
            ftp.connect(host, 21, timeout=30)
            ftp.login(user, password)
            print("Logged in successfully!")
            print("Current directory:", ftp.pwd())
            print("Listing files:")
            files = []
            ftp.retrlines("LIST", files.append)
            for f in files[:20]:
                print(f)
            return 0
    except Exception as e:
        print("FTP Connection failed:", e)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
