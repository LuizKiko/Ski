from dotenv import load_dotenv
import pandas as pd


dfSki = pd.read_csv(r"ski\resorts.csv")
dfSnow = pd.read_csv(r"ski\snow.csv")
dfCountryCode = pd.read_csv(r"ski\CountryCodes.csv")
