import pytest

from app.services.prompt import build_system_prompt
from app.services.truth_sheet import load_truth_sheet

RECEIPT = "ev_bank_transfer_receipt"


@pytest.fixture
def sheet():
    return load_truth_sheet("case1", "victim")


def test_locked_secret_not_in_prompt(sheet):
    prompt = build_system_prompt(sheet, [])

    assert sheet.hides[0].fact not in prompt
    assert sheet.lies[0].claim in prompt


def test_unlocked_secret_in_prompt(sheet):
    prompt = build_system_prompt(sheet, [RECEIPT])

    assert sheet.hides[0].fact in prompt
    assert sheet.lies[0].claim not in prompt


@pytest.mark.parametrize("evidence_shown", [[], [RECEIPT]])
def test_truth_never_in_prompt(sheet, evidence_shown):
    prompt = build_system_prompt(sheet, evidence_shown)

    assert sheet.lies[0].truth not in prompt
