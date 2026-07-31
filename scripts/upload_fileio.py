#!/usr/bin/env python3
"""Загрузка файла dzen_payload.js на file.io."""

from __future__ import annotations

import json
import urllib.request
from pathlib import Path


def main() -> int:
    url = "https://file.io"
    payload_path = Path("dzen_payload.js")
    if not payload_path.is_file():
        print("Error: dzen_payload.js not found")
        return 1

    print("Uploading dzen_payload.js to file.io...")
    boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"
    data = []
    data.append(f"--{boundary}".encode("utf-8"))
    data.append(b'Content-Disposition: form-data; name="file"; filename="dzen_payload.js"')
    data.append(b"Content-Type: application/javascript")
    data.append(b"")
    data.append(payload_path.read_bytes())
    data.append(f"--{boundary}--".encode("utf-8"))
    data.append(b"")
    body = b"\r\n".join(data)

    req = urllib.request.Request(url, data=body)
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    
    try:
        with urllib.request.urlopen(req, timeout=120) as res:
            resp = json.loads(res.read().decode("utf-8"))
            if resp.get("success") is True:
                dl_url = resp["link"]
                print(f"SUCCESS: Uploaded to {dl_url}")
                return 0
            else:
                print("Error: success not True", resp)
                return 1
    except Exception as e:
        print("Upload failed:", e)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
