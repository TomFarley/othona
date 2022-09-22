"""
Tests for PeopleData and related classes.
"""

import os
from pathlib import Path

import numpy as np
import pandas as pd

from othona import people_data
from .base_test import BaseTestCase, unittest

cwd = Path(os.getcwd())
path_file = Path(__file__).parent

class TestCiviLocalExportReader(BaseTestCase):
    """
    Tests for the CiviLocalExportReader class.
    """

    def test_teens_choose(self):
        """Test with integer inputs."""

        fn = path_file / 'data/civi_exports/Teens_Choose_Participant_Search.xlsx'
        reader = people_data.CiviLocalExportReader()
        df_people_data = reader.read(fn)

        self.assertIsInstance(df_people_data, pd.DataFrame)
        self.assert_equal(df_people_data.index.name, 'Participant ID')



