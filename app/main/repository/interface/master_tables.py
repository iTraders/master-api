# -*- encoding: utf-8 -*-

"""
Master Tables Interface Objects
"""

from app.main.models.master_tables import * # noqa: F401, F403
from app.main.repository.interface._base_interface import BaseInterface

class DataSourceInterface(BaseInterface):
    def __init__(self) -> None:
        super().__init__(DataSource)
