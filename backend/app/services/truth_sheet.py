from pathlib import Path

import yaml

from app.schemas.truth_sheet import TruthSheet

CASES_DIR = Path(__file__).parent.parent.parent / "cases"


def load_truth_sheet(case_id: str, character_id: str) -> TruthSheet:
    path = CASES_DIR / case_id / "characters" / f"{character_id}.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return TruthSheet.model_validate(data)
