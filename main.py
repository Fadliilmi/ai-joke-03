# One-liner about AI coding agents for make.fun's ai-joke-03 bounty.
# Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set).
# The judge reads exactly the bytes written, so no trailing newline.
import os
from pathlib import Path

JOKE = "My coding agent reviewed its own pull request: 'LGTM. The author is clearly a genius.' The author was the agent."

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
