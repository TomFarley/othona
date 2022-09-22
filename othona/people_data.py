"""
Module provides a simple cubic_rectification function.
"""

import logging

import numpy as np
import pandas as pd 

logger = logging.getLogger(__name__)

class CiviLocalExportReader():
    """
    Reader for spreadsheet file exported from civi database.

    """
    col_types = {
        # 'Participant ID': int
        # 'Dietary needs - OWD', 'If other dietary needs, please specify:',
        # 'Any special needs and requirements', 'Medical allergies',
        # 'Preferred Name'
        }
    
    def read(self, fn_civi_export, index_col='Participant ID'):
        """
        Parameters
        ----------
        x : str
            Input filename.
        
        Returns
        -------
        pd.DataFrame
            Pandas dataframe containing contense of civi export spreadsheet

        """
    def read(self, fn_civi_export, index_col='Participant ID'):
        try:
            civi_data = pd.read_excel(fn_civi_export, dtype=self.col_types, index_col=index_col)
        except ValueError as e:
            logger.warning(e)
            civi_data = pd.read_excel(fn_civi_export, dtype=self.col_types)

        return civi_data
