# -*- encoding: utf-8 -*-

"""
Master Table(s) SQL Alchemy ORM Defination

A set of ORM queries is defined based on Flask-Docker Template Design
The table structures is available under `./algorithms/assets/data`
but maybe shifted/organised under `master-api` repository.
"""

# import os
from app.main import db

# class ENUMConfig(object):
#     def __init__(self) -> None:
#         self.base_dir = os.path.join(os.path.abspath(__file__), "config", "enum")


#     def _read_file(self, filename : str) -> list:
#         return list(map(lambda x : x.strip().replace("\n", ""), open(filename, "r").readlines()))


#     @property
#     def exchange_segment(self) -> list:
#         return self._read_file("exchange_segment")


#     @property
#     def exchange_segment(self) -> list:
#         return self._read_file("exchange_segment")

class DataSource(db.Model):
    __tablename__ = 'data_source'

    id = db.Column(db.String(25), primary_key = True)
    uri = db.Column(db.String(1024), nullable = True)
    name = db.Column(db.String(64), nullable = False, unique = True)
    yaml_version = db.Column(db.String(25), nullable = True)
    created_at = db.Column(db.TIMESTAMP, server_default = "CURRENT_TIMESTAMP")
    updated_at = db.Column(db.TIMESTAMP, onupdate = "CURRENT_TIMESTAMP", nullable = True)


class InstrumentsType(db.Model):
    __tablename__ = 'instruments_type'

    _id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    symbol = db.Column(db.String(32), nullable = False)
    company_name = db.Column(db.String(255), nullable = True)
    incorporation_date = db.Column(db.Date, nullable = True)
    company_website = db.Column(db.String(255), nullable = True)
    exchange_segment = db.Column(db.Enum('NSE', 'BSE', 'NFO', 'CDS', 'MCX', 'NCDEX'), nullable = False)
    instrument_type = db.Column(db.Enum('AMXIDX', 'AUCSO', 'COMDTY', 'FUTCOM', 'FUTCUR', 'FUTIDX', 'FUTIRC', 'FUTIRT', 'FUTSTK', 'INDEX', 'OPTCUR', 'OPTFUT', 'OPTIDX', 'OPTIRC', 'OPTSTK', 'UNDCUR', 'UNDIRC', 'UNDIRD', 'UNDIRT'), nullable = True)
    lot_size = db.Column(db.Integer, nullable = True)
    data_source = db.Column(db.String(255), nullable = False)
    created_at = db.Column(db.TIMESTAMP, server_default = 'CURRENT_TIMESTAMP')
    updated_at = db.Column(db.TIMESTAMP, onupdate = 'CURRENT_TIMESTAMP', nullable = True)
