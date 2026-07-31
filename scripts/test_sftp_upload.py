#!/usr/bin/env python3
"""Тест загрузки файла в папку LMS через SFTP."""

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
        
        print("Writing sftp_test.txt to /var/www/club-lms/ ...")
        sftp = ssh.open_sftp()
        with sftp.open("/var/www/club-lms/sftp_test.txt", "w") as f:
            f.write("KODA-LMS-STATIC-TEST")
        sftp.close()
        
        test_url = "https://koda-fd.ru/club-lms/sftp_test.txt"
        print(f"Testing URL: {test_url}")
        try:
            with urllib.request.urlopen(test_url, timeout=5) as res:
                content = res.read().decode().strip()
                print("Response:", content)
                if content == "KODA-LMS-STATIC-TEST":
                    print("SUCCESS! static hosting works perfectly in /var/www/koda-club-lms/ !")
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
