import os
from dotenv import load_dotenv
import mysql.connector
import pandas as pd

load_dotenv()

dfSki = pd.read_csv(r"ski\resorts.csv")
dfSnow = pd.read_csv(r"ski\snow.csv")
dfCountryCode = pd.read_csv(r"ski\CountryCodes.csv")
