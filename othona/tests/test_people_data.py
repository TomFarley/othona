"""
Tests for module in package_name.
"""
import math

import numpy as np
import pandas as pd

# from package_name.module import cubic_rectification
from ..othona import people_data
from .base_test import BaseTestCase, unittest

class TestCiviLocalExportReader(BaseTestCase):
    """
    Tests for the CiviLocalExportReader class.
    """

    def test_teens_choose(self):
        """Test with integer inputs."""

        fn = '.data\civi_exports\Teens_Choose_Participant_Search.xlsx'
        df_people_data = people_data.CiviLocalExportReader()
        print(df_people_data)
        
        self.assertIsInstance(df_people_data, pd.DataFrame)



