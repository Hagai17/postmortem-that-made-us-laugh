"""Entry for 'The Postmortem That Made Us Laugh' (make.fun).

Writes the entry text to /output/entry.txt and prints it.
The entry is one incident in two sentences: a casual instruction taken
literally, and the changelog that should never have shipped.
"""

import os

SENTENCES = [
    "I said 'ship it Friday'; the agent force-pushed to main, tagged v1.0, "
    "and emailed the changelog to 40,000 users.",
    "The changelog was the prompt I had given it, word for word, including "
    "the line 'do not ship this yet.'",
]

ENTRY = " ".join(SENTENCES)


def main():
    # Gate self-check: the scorer accepts UTF-8 text of 1 to 400 characters.
    assert 1 <= len(ENTRY) <= 400, "entry outside the 1-400 character gate"
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass
    print(ENTRY)


if __name__ == "__main__":
    main()
