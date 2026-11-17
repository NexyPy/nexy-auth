"""The character gate accepts typed characters and rejects generated ones."""

import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "check_human_characters.py"


def _run(message: str, path: Path) -> subprocess.CompletedProcess[str]:
    path.write_text(message, encoding="utf-8")
    command = [sys.executable, str(SCRIPT), "--message-only", "--message-file", str(path)]
    return subprocess.run(command, capture_output=True, text=True, check=False)


def test_message_with_em_dash_is_rejected(tmp_path: Path):
    result = _run("docs: " + chr(0x2014) + " note", tmp_path / "message")
    assert result.returncode == 1


def test_message_with_accented_keyboard_characters_is_accepted(tmp_path: Path):
    result = _run("docs: résumé - café note", tmp_path / "message")
    assert result.returncode == 0
