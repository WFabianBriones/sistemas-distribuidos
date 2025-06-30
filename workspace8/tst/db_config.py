#!/usr/bin/env python3 

import psycopg2
import psycopg2.extras

def get_db_connection():
    conn = psycopg2.connect(
        host = '127.0.0.1',
        database = 'flaskdb',
        user = 'uleam',
        password = 'uleam20251'
    )
    return conn