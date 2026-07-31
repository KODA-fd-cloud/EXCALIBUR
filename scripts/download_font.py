#!/usr/bin/env python3
"""Скачивание шрифта Montserrat-ExtraBold из рабочего репозитория JulietaUla."""

from __future__ import annotations

import urllib.request
from pathlib import Path

def main() -> int:
    font_url = "https://github.com/JulietaUla/Montserrat/raw/master/fonts/ttf/Montserrat-ExtraBold.ttf"
    output_path = Path("Montserrat-ExtraBold.ttf")
    
    if output_path.is_file():
        print(f"OK font already exists: {output_path}")
        return 0
        
    print(f"Downloading font from {font_url}...")
    headers = {"User-Agent": "Mozilla/5.0"}
    req = urllib.request.Request(font_url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        output_path.write_bytes(response.read())
    print(f"OK font saved to {output_path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
