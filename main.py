# One-liner about AI coding agents for make.fun's ai-joke-03 bounty.
# Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set).
# The judge reads exactly the bytes written, so no trailing newline.
import os
from pathlib import Path

JOKE = "I asked my coding agent to explain its own code. It said: 'I wrote it. Understanding it was never in the prompt.'"

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(JOKE, encoding="utf-8")
