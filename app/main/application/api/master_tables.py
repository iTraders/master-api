# -*- encoding: utf-8 -*-

from flask import request
from flask import redirect

from app.main.application._base_resource import BaseResource
from app.main.repository.interface.master_tables import * # noqa: F401, F403

class DataSourceAPI(BaseResource):
    def __init__(self):
        super().__init__()

        # repository/interface objects
        self.data_source_master_interface = DataSourceInterface()


    def get(self):
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> OK <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        return self.formatter.get(self.data_source_master_interface.get_all())
