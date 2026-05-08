"""
download_flags.py — one-time setup script
==========================================
Downloads all flag SVG files from the flag-icons GitHub release into
  Resources/Data/flag-icons/flags/1x1/
  Resources/Data/flag-icons/flags/4x3/

Run once from the 04-Wordle directory before opening worldle.ipynb:

    python Resources/Data/download_flags.py

Requires only the Python standard library (urllib, pathlib, json).
Takes ~30–60 seconds on a normal connection.
"""
import json
import pathlib
import time
import urllib.request

BASE_URL = "https://raw.githubusercontent.com/lipis/flag-icons/main/"
HERE = pathlib.Path(__file__).parent
FLAGS_DIR = HERE / "flag-icons"
COUNTRY_JSON = FLAGS_DIR / "country.json"


def download_file(url: str, dest: pathlib.Path) -> bool:
    """Download url → dest. Returns True on success, False on 404/error."""
    if dest.exists():
        return True  # already have it
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(r.read())
        return True
    except Exception as exc:
        print(f"  SKIP {dest.name}: {exc}")
        return False


def main():
    with open(COUNTRY_JSON, encoding="utf-8") as f:
        entries = json.load(f)

    iso_entries = [e for e in entries if e.get("iso") and len(e["code"]) == 2]
    total = len(iso_entries)
    ok = 0

    for i, entry in enumerate(iso_entries, 1):
        code = entry["code"]
        for ratio in ("4x3", "1x1"):
            rel = f"flags/{ratio}/{code}.svg"
            url = BASE_URL + rel
            dest = FLAGS_DIR / rel
            if download_file(url, dest):
                ok += 1
        if i % 20 == 0 or i == total:
            print(f"  {i}/{total} countries processed …")
        time.sleep(0.05)   # be polite to GitHub's servers

    print(f"\nDone. {ok} files saved under {FLAGS_DIR.relative_to(HERE.parent.parent)}")


if __name__ == "__main__":
    main()
