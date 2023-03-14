"""
Module provides a simple cubic_rectification function.
"""

import logging
from dataclasses import dataclass, field
from typing import Optional

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

# @dataclass
class ParticipantData:
    """Class for storing and working with event participant data."""
    
    # Fields for @dataclass
    # participant_data: pd.DataFrame = field(default_factory=pd.DataFrame, args=[])
    # catering_list: pd.DataFrame | None = None
    # catering_list: pd.DataFrame | None = None   
    
    def __init__(self, event, civi_data=None):
        self.event: str = event
        self.civi_data: Optional(pd.DataFrame) = civi_data
        self.participant_data: Optional(pd.DataFrame) = None
        self.catering_list: Optional(pd.DataFrame) = None

    def run_checks():
        raise NotImplementedError

    def format():
        raise NotImplementedError

    def read_and_merge_data(self, reader_args, reader_kwargs=(), reader='CiviLocalExportReader') -> float:
        
        readers = {'CiviLocalExportReader': CiviLocalExportReader()}
        if reader in readers:
            reader = readers[reader]
        
        new_data = reader(*reader_args, **dict(reader_kwargs))
        
        self.participant_data = self.participant_data.merge(new_data)