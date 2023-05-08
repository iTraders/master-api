# -*- encoding: utf-8 -*-

import os

class Config:
    """Base Configuration Class - Inherited by Others"""

    DEBUG      = False
    TESTING    = False
    SECRET_KEY = os.getenv("SECRET_KEY", "my_secret_key")

    # database centric variables can be initialized like
    DATABASE_USERNAME = os.getenv("_iTraders_MASTER_API_DB_USERNAME", "user")
    DATABASE_PASSWORD = os.getenv("_iTraders_MASTER_API_DB_PASSWORD", "pass")
    DATABASE_HOSTNAME = os.getenv("_iTraders_MASTER_API_DB_HOSTNAME", "localhost")
    DATABASE_PORTNUMBER = os.getenv("_iTraders_MASTER_API_DB_PORTNUMBER", 3306)

    # sqlalchemy settings
    PRESERVE_CONTEXT_ON_EXCEPTION  = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        __SA_DB_CON__ = "mysql+pymysql:/"
        return f"{__SA_DB_CON__}/{self.DATABASE_USERNAME}:{self.DATABASE_PASSWORD}" + \
            f"@{self.DATABASE_HOSTNAME}:{self.DATABASE_PORTNUMBER}/{self.schema_name}"


class DevelopmentConfig(Config):
    """Development Configuration: invoke this using config_name = dev"""

    DEBUG = True # This is a development server.

    def __init__(self) -> None:
        super().__init__()
        self.schema_name = "test"


class TestingConfig(Config):
    """Testing Environment: invoke this using config_name = test"""

    DEBUG   = True
    TESTING = True

    def __init__(self) -> None:
        super().__init__()
        self.schema_name = "test-database"


class ProductionConfig(Config):
    """Production Environment: invoke this using config_name = prod"""

    pass # configure for production environment here

config_by_name = dict(
        dev  = DevelopmentConfig,
        test = TestingConfig,
        prod = ProductionConfig
    )

key = Config.SECRET_KEY
