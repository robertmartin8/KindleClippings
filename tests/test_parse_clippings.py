import os
from pathlib import Path
import types

import KindleClippings
from KindleClippings import parse_clippings, remove_chars


def test_parse_clippings_creates_files(tmp_path):
    clippings = Path(__file__).with_name("My Clippings.txt")
    out_dir = tmp_path / "out"
    parse_clippings(str(clippings), str(out_dir), format="txt")

    expected_files = [
        remove_chars("Example Title: The Beginning (John Doe)") + ".txt",
        remove_chars("Another Book? & Something & Else (Jane Smith)") + ".txt",
    ]
    assert sorted(os.listdir(out_dir)) == sorted(expected_files)

    contents1 = (out_dir / expected_files[0]).read_text(encoding="utf8")
    assert "This is a highlight text." in contents1

    contents2 = (out_dir / expected_files[1]).read_text(encoding="utf8")
    assert "Interesting highlight & note?" in contents2
