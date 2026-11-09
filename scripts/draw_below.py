"""Sheets of the selected training photos whose probability for their own city is below a limit.

Reads the probabilities that `curate.py suspects` saved, so the model does not
run again, and draws them with curate.py, lowest probability first:

    python scripts/draw_below.py results/curate/suspects_baseline_seed0.csv --below 0.3

Sheets go to results/curate/below03_baseline_seed0_<city>_NN.png, each with a
.csv, so that `curate.py drop` takes the sheet name and numbers. Photos no
longer in track_a/selection.csv are left out.
"""

import argparse
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import curate  # noqa: E402
from rules import CITIES  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("table", help="the suspects_<run>.csv that curate.py suspects wrote")
    ap.add_argument("--below", type=float, default=0.3, help="own-city probability below this")
    args = ap.parse_args()

    table = Path(args.table)
    run = table.stem.removeprefix("suspects_")
    selected = set(curate.read_selection())
    with open(table, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f)
                if r["path"] in selected and float(r["own_city_probability"]) < args.below]
    limit = f"{args.below:g}".replace(".", "")  # 0.3 -> 03
    for city in CITIES:
        mine = sorted((float(r["own_city_probability"]), r["path"], r["answer"]) for r in rows if r["city"] == city)
        items = [(curate.TRAIN / p, f"{city} {pr:.2f}, says {answer}") for pr, p, answer in mine]
        names = curate.draw_sheets(f"below{limit}_{run}_{city}", items)
        print(f"{city}: {len(items)} photos below {args.below} on {len(names)} sheets"
              + (f", {names[0]} to {names[-1]}" if names else ""))


if __name__ == "__main__":
    main()
