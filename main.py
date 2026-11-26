import os

ENTRY = "v8.0.1 — Sleep now starts within 30 seconds of lying down; replaying every embarrassing thing you said since 2011 was a known issue, now resolved."


def validate(entry: str) -> None:
    # Gate check (kit: /output/entry.txt must be UTF-8 text of 1 to 160
    # characters, not only white space) — fail loudly instead of writing
    # an entry the sealed scorer would reject. The judge also weighs a
    # true single line, so reject embedded newlines here too.
    if entry != entry.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not 1 <= len(entry) <= 160:
        raise ValueError(f"entry is {len(entry)} chars, gate is 1-160")
    if not entry.strip():
        raise ValueError("entry must not be only whitespace")
    entry.encode("utf-8")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
