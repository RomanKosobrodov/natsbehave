import os
import glob
import json


def parse_scenarios(src):
    if not os.path.exists(src):
        return
    for fn in glob.glob("**/*.json", recursive=True):
        with open(fn, "r") as f:
            yield json.load(f)
    return