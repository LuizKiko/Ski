import streamlit as st

def content(replace: str):
    if replace == "studyCaseSki":
            replace = """
                    ### Skiing around the world
                    ---
                    ##### User Need:
                    > As a passionate skier eagerly anticipating my next thrilling adventure on the slopes, I'm keen on meticulously planning every detail to ensure an optimal experience. The distance from my home to the ski destination, the cost involved, and the prevailing weather conditions are critical factors that I carefully consider to make the most informed decision for a memorable and exhilarating ski trip.
                    ---
                    ##### Value Delivered:
                    + Number of ski stations around and its geolocation
                        + Facilitate the dashboard user to comprehend the best places to visit for a Ski adventure
                    + Heatmap of prices
                        + Which support the user with his cost management
                    + Snow information
                        + Historical information about the snowfall from last year to help predicting the best season to go
                    + Highest altitude of the stations
                        + For the the adventurers who consider a more wild trip :)
                    ---
                    ##### Future improvements:
                    + Overlapping view of ski stations with snowfall
                        + To make even easier for the user to decide where to go based on the weather/distance
                    + Heatmap of visitors per month
                        + Who likes wait in lines? Finding the best time to go to a ski station can grant you a better experience
                    + Access channels
                        + Roads and airports distances from the stations can be handy to arrive and leave on time!
                    ---
                    ##### Data source:
                    + [Maven Analytics](https://mavenanalytics.io/data-playground) | [Country Codes Alpha](https://www.iban.com/country-codes)                    
                    """        
    else:
          return None

    return st.markdown(replace)