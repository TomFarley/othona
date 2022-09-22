"""
Tests for module in package_name.
"""
import os
from pathlib import Path

import numpy as np
import pandas as pd

import othona
from othona import people_data

cwd = Path(os.getcwd())
path_othona = Path(othona.__path__[0])

from othona.people_data import CiviLocalExportReader

fn = path_othona / 'tests/data/civi_exports/Teens_Choose_Participant_Search.xlsx'
print(fn)

reader = people_data.CiviLocalExportReader()
df_people_data = reader.read(fn)

print(df_people_data)
print(df_people_data.columns)