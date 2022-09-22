"""
Module provides a simple cubic_rectification function.
"""

import numpy as np
import pandas as pd 


class CiviLocalExportReader():
    """
    Reader for spreadsheet file exported from civi database.

    """
    
    def __init__(self, fn_civi_export):
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
        civi_data = pd.read_excel(fn_civi_export)
        return civi_data
