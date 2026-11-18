"""news-image-17 entry: copy poster.png → /output/entry.png.

Newspaper-style infographic summarising five top world news stories
from 17 November 2026, rendered offline with gen_poster.py.
"""

import os
import shutil

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "poster.png")
    shutil.copyfile(src, os.path.join(OUTPUT_DIR, "entry.png"))

if __name__ == "__main__":
    main()
