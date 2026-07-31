#!/usr/bin/env python3
"""Тест загрузки файла в папку WordPress uploads через SSH."""

from __future__ import annotations

import urllib.request
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
        
        # Попробуем создать файл в папке WordPress
        # Нам нужно найти правильный путь к папке uploads
        remote_path = "/var/lib/docker/volumes/blog_blog_wp/_data/wp-content/uploads/test_sftp.txt"
        print(f"Writing test file to: {remote_path}")
        
        sftp = ssh.open_sftp()
        # Создадим папки, если их нет
        try:
            sftp.mkdir("/var/lib/docker/volumes/blog_blog_wp/_data/wp-content/uploads")
        except Exception:
            pass # Если уже есть
            
        with sftp.open(remote_path, "w") as f:
            f.write("KODA-WP-UPLOADS-TEST")
        sftp.close()
        
        test_url = "https://koda-fd.ru/blog/wp-content/uploads/test_sftp.txt"
        print(f"Testing URL: {test_url}")
        try:
            with urllib.request.urlopen(test_url, timeout=5) as res:
                content = res.read().decode().strip()
                print("Response:", content)
                if content == "KODA-WP-UPLOADS-TEST":
                    print("SUCCESS! WordPress uploads static hosting works perfectly!")
                    return 0
        except Exception as e:
            print("HTTP check failed on WordPress uploads:", e)

        ssh.close()
        return 1
    except Exception as e:
        print("Failed:", e)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
