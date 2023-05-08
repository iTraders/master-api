# -*- encoding: utf-8 -*-

"""API Management and Server Running Module"""

import os
from app import app

if __name__ == "__main__":
    # call back from environment variables, setup using `.env/README.md`
    # else, let the flask app engine run in localhost development mode for testing
    app.run(
        port = os.getenv("MASTER_API_SERVING_PORT", 5000), # run the application on default 5000 Port
        # localhost is required to run the code from m/c
        # else, 0.0.0.0 can be used for docker container
        host = os.getenv("MASTER_API_SERVING_HOST", "0.0.0.0") # define host, as required
    )
