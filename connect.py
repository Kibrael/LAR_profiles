import psycopg2
import psycopg2.extras
from collections import OrderedDict
import json
import csv
import sys
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os


def connect():
    #parameter format for local use
    params = {
    'dbname':'hmdamaster',
    'user':'roellk',
    'password':'',
    'host':'localhost',}
    try:
        conn = psycopg2.connect(**params)
        print "i'm connected"
    except psycopg2.Error as e: #if database connection results in an error print the following
        print "I am unable to connect to the database: ", e
    return  conn, conn.cursor()#(cursor_factory=psycopg2.extras.DictCursor) #return a dictionary cursor object


def pull_FI_LAR(cur, conn, agency, rid, table):
    SQL = "SELECT * FROM {table} WHERE agency = {agency} and rid = {rid}".format(table = table, rid = rid, agency=agency)
    print SQL
    SQL = "SELECT * FROM {table} WHERE concat(agency, rid) ='90000852218'".format(table=table)
    cur.execute(SQL,)

conn, cur = connect()

LAR_cols = ['year', 'agency', 'rid', 'loan_type', 'property_type', 'loan_purpose', 'occupancy', 'preapproval', 'amount', 'action', 'msa', 'state', 'county', 'tract', 'ethnicity', 'co_ethnicity', 'race1', 'race2', 'race3', 'race4', 'race5', 'co_race1', 'co_race2', 'co_race3', 'co_race4', 'co_race5', \
'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'rate_spread', 'hoepa', 'lien', 'edit_status', 'sequence', 'population', 'min_population_pct', 'median_income', 'tract_to_msa_income_pct', 'num_owner_occ_units', 'num_single_fam_units', 'app_date_ind']
pull_FI_LAR(cur, conn, '9', '0000852218', 'hmdalar2014')

LAR_df = pd.DataFrame(cur.fetchall())
LAR_df.columns= LAR_cols
print LAR_df.head()