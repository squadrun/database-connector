========================
Database Connector
========================

A python package that provides database connection to Bifrost database and Substrate database.

Modules
#########

There are three modules - **bifrost** and **substrate**.

All the modules provide the ``engine`` for their respective database.

bifrost
********

This module provides the database connection for the Bifrost database. It provides **read-only** access to the database.


substrate
**********

This module provides the database connection for the Substrate database. It provides **read-only** access to the database.

Usage
------

.. code-block:: python

    from database_connector import bifrost, substrate

    bifrost_engine = bifrost.engine
    substrate_engine = substrate.engine

    # Database connection is automatically closed when connection is used in a context manager i.e. inside "with"
    with bifrost_engine.connect() as conn:
        data = conn.execute("Select * from customer")

        # data is a dictionary with column name as key and row as value
        for row in data:
            print(row)
            
    # Database connection is automatically closed when connection is used in a context manager i.e. inside "with"
    with substrate_engine.connect() as conn:
        data = conn.execute("Select * from customer")

        # data is a dictionary with column name as key and row as value
        for row in data:
            print(row)


How to install this module inside SageMaker Jobs started from JupyterHub
--------------------------------------------------------------------------

The following commands should be added in the DockerFile to install this module in the docker image. Preferably add these commands near the end before changing the working directory since all the steps these commands will be rebuild and cache won’t be used.
  
.. code-block:: dockerfile

    COPY database-connector-*.tar.gz /mnt/
    RUN pip3 install /mnt/database-connector-*.tar.gz

Documentation
--------------

We use SQL Alchemy as an ORM because it provides additional features than raw `psycopg2`.
You can check out its documentation here - `SQL Alchemy docs <https://docs.sqlalchemy.org/en/13/core/connections.html>`__

How to Modify this Package
----------------------------

1. This package works with Python 3
2. After making the necessary changes run the following commands to build the project and install the package

.. code-block:: bash

    python setup.py sdist
    sudo -E python -m pip install  dist/database-connector-0.1.tar.gz


3. You can uninstall the package by running the following command - ``sudo -E pip uninstall database-connector``
