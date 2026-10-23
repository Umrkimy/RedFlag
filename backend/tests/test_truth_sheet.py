import pytest
from pydantic import ValidationError

from app.services import truth_sheet
from app.services.truth_sheet import load_truth_sheet


def test_load_truth_sheet():
    sheet = load_truth_sheet("case1", "victim")

    assert sheet.id == "victim"
    assert sheet.name == "Aina"
    assert len(sheet.hides) == 2


def test_load_truth_sheet_missing_file():
    with pytest.raises(FileNotFoundError):
        load_truth_sheet("case1", "does_not_exist")


def test_load_truth_sheet_invalid(tmp_path, monkeypatch):
    folder = tmp_path / "case1" / "characters"
    folder.mkdir(parents=True)
    (folder / "broken.yaml").write_text("name: Aina\n")
    monkeypatch.setattr(truth_sheet, "CASES_DIR", tmp_path)

    with pytest.raises(ValidationError):
        load_truth_sheet("case1", "broken")