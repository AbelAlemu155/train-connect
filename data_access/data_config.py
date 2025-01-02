
# the module for creating a pool for the postgress connector

import psycopg2 
from psycopg2 import pool

# Creation of an instance for the SimpleConnectionPool class.
simple_conn_pool = psycopg2.pool.SimpleConnectionPool(2, 10, user="postgres",

                                                        password="train_admin",
                                                        host="127.0.0.1",
                                                        port="5432",
                                                        database="train_connect_db")

# except (Exception, psycopg2.DatabaseError) as error:





