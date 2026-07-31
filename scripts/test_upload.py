#!/usr/bin/env python3
"""Тест загрузки тестового файла в веб-рут сервера."""

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
        
        # Запишем тестовый файл в /var/www/html
        print("Writing test.txt...")
        sftp = ssh.open_sftp()
        with sftp.open("/var/www/html/test.txt", "w") as f:
            f.write("KODA-DZEN-AUTOMATION-TEST")
        sftp.close()
        
        # Пробуем скачать его по HTTP
        test_url = "http://45.11.93.42/test.txt"
        print(f"Testing URL: {test_url}")
        try:
            with urllib.request.urlopen(test_url, timeout=5) as res:
                content = res.read().decode().strip()
                print("Response:", content)
                if content == "KODA-DZEN-AUTOMATION-TEST":
                    print("SUCCESS! We can host any file on the server webroot!")
                    return 0
        except Exception as e:
            print("HTTP check failed on IP, trying domain...")
            
        test_url_domain = "https://koda-fd.ru/test.txt"
        print(f"Testing URL: {test_url_domain}")
        try:
            with urllib.request.urlopen(test_url_domain, timeout=5) as res:
                content = res.read().decode().strip()
                print("Response:", content)
                if content == "KODA-DZEN-AUTOMATION-TEST":
                    print("SUCCESS! We can host any file on koda-fd.ru!")
                    return 0
        except Exception as e:
            print("HTTP check failed on domain:", e)

        ssh.close()
        return 1
    except Exception as e:
        print("Failed:", e)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
