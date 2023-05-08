# -*- encoding: utf-8 -*-

"""Create all Data-Base"""

import os

from app.main import (
        db, # SQLAlchemy Connector dB Object
        create_app
    )
from app.main.models import * # noqa: F401, F403


if __name__ == "__main__":
    # app object with all dependency is imported
    app = create_app(os.getenv("PROJECT_ENV_NAME") or "demo")

    with app.app_context():
        db.init_app(app)
        db.create_all()
