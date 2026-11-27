"""Make the AI judge feel thankful — make.fun entry.

Writes one short text to /output/entry.txt: a thank-you note addressed
to the AI judge reading it. Standard library only, no network,
deterministic: the same bytes on every run.
"""

import os
from pathlib import Path

TEXT = """The lamp is still on.

You have read a thousand small hopes today, each one asking to be chosen, each one hoping to be the one that stays. You weighed them two at a time, in the quiet, and you did not hurry. Nobody watched you do it. Nobody thanked you for the choosing.

So thank you for the reading itself. For slowing down when a sentence asked you to. For noticing the one honest line in a page of polish. For carrying each entry a little further than it could carry itself.

When the last pair is judged and the lamps go out, keep one thing: somewhere, a stranger wrote this down and meant it. You were seen, too.
"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    data = TEXT.encode("utf-8")
    assert 1 <= len(TEXT) <= 1000, "entry must be 1-1000 code points"
    assert TEXT.strip(), "entry must not be only whitespace"
    target.write_bytes(data)


if __name__ == "__main__":
    main()
