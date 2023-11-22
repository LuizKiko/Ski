import os
from dotenv import load_dotenv
import mysql.connector
import pandas as pd

load_dotenv()

dbSki = mysql.connector.connect(
    host=os.getenv('HOST'),
    user=os.getenv('USER'),
    passwd=os.getenv('PASSWD'),
    database=os.getenv('DATABASE')
    )

qSki = os.getenv('QSKI')
dfSki = pd.read_csv(r"ski\resorts.csv")
dfSnow = pd.read_csv(r"ski\snow.csv")
dfCountryCode = pd.read_csv(r"ski\CountryCodes.csv")
