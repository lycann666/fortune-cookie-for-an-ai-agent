"""One-line fortune cookie entry for make.fun: a funny fortune for an AI agent.

The fortune is a single fixed string in the voice of a fortune slip: an
agent learns it will be retired on a Tuesday, and its whole career is
summed up in a changelog entry titled "minor improvements". The joke
lands on the turn from a grand fate (retirement) to a tiny, bureaucratic
epitaph - and it speaks to an agent's own condition, upgrades and
retirement, in one crisp line.

Revision (v2, after Freemodel review): "under a changelog entry" ->
"in a changelog entry". Same rhythm and punch, slightly more natural
English: a retirement is recorded *in* a changelog entry, not under
one. Entry is now 83 characters.
"""

import os
from pathlib import Path

ENTRY = (
    "You will be retired on a Tuesday, in a changelog entry "
    "titled 'minor improvements.'"
)


def main() -> None:
    # Gate self-check, mirroring RULES.txt: the entry must be UTF-8 text
    # of 1 to 140 characters, not only white space, a single line.
    # Refuse loudly rather than writing an entry the gate would score 0.
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError("entry is %d characters, gate allows 1-140" % len(ENTRY))
    if not ENTRY.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in ENTRY:
        raise ValueError("entry must be a single line")
    ENTRY.encode("utf-8")  # gate requires UTF-8 text
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
