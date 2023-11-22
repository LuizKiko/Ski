import pandas as pd
import streamlit as st
import plotly.express as px
from content import content

def Ski(dfSki: pd.DataFrame, dfCountryCode: pd.DataFrame, dfSnow: pd.DataFrame):
    st.header("Ski Stations")

    with st.expander("Study case"):
        content("studyCaseSki")

    tabStations, tabWeather = st.tabs(["Stations", "Weather"])
    with tabStations:
        st.subheader("Geolocation information")

        #Stations per Country
        groupedContinent = dfSki.groupby('Continent').size().reset_index(name='ContinentCount')
        metricTitle = groupedContinent['Continent'].tolist()
        metricvalues = groupedContinent['ContinentCount'].tolist()
        avgStationQty = groupedContinent['ContinentCount'].mean().round()
        countCols = groupedContinent['Continent'].size
        countCols = st.columns(countCols)

        for i in range(len(countCols)):
            with countCols[i]:
                st.metric(metricTitle[i],metricvalues[i],metricvalues[i]-avgStationQty)

        #Stations per Country plot
        groupedCountry = dfSki.groupby('Country').size().reset_index(name='CountryCount')

        countryBarChart = px.bar(groupedCountry, y='CountryCount', x='Country', text_auto='.2s',
                    title="Ski Stations per country",color='Country')
        countryBarChart.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
        st.plotly_chart(countryBarChart,use_container_width=True)

        # Map plot
        geoStationChart = px.scatter_mapbox(dfSki, lat='Latitude', lon='Longitude', hover_name='Resort',
                                hover_data=['Price', 'Highest point'], 
                                color_discrete_sequence=["steelblue"], zoom=2, width=2050)
        geoStationChart.update_layout(mapbox_style="open-street-map")
        geoStationChart.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(geoStationChart)

        st.divider()
        st.subheader("Prices drilldown")
        Skiprices = dfSki.sort_values(by=['Price'])
        lowestPrice = Skiprices['Price'].min()
        highestPrice = Skiprices['Price'].max()
        avgPrice = Skiprices['Price'].mean().round()
        st.caption("Prices in US Dollars")

        #AVG price per continent
        avgPriceContinent = dfSki.groupby('Continent')['Price'].mean().reset_index(name='ContinentAvg').round(2)
        metricTitle = avgPriceContinent['Continent'].tolist()
        metricvalues = avgPriceContinent['ContinentAvg'].tolist()

        countCols = groupedContinent['Continent'].size
        countCols = st.columns(countCols)

        for i in range(len(countCols)):
            with countCols[i]:
                st.metric(metricTitle[i],metricvalues[i],(metricvalues[i]-avgPrice).round())

        lowestPrice, highestPrice = st.select_slider(
        'Select the price range to inspect:',
        options=Skiprices['Price'],
        value=(lowestPrice, highestPrice))

        avgPriceCountry = dfSki.groupby('Country')['Price'].mean().reset_index(name='Price').round(2)
        avgPriceContryCode = pd.merge(avgPriceCountry, dfCountryCode, on='Country')
        avgPriceContryCode.rename(columns={"Alpha-3 code":"ctry"}, inplace=True)
        avgPriceContryCode = avgPriceContryCode.query("(Price >= @lowestPrice) & (Price <= @highestPrice)")

        # Heatmap prices plot
        priceHeatmap = px.choropleth(avgPriceContryCode, locations='ctry', color='Price',
                            color_continuous_scale="Teal",
                            title="Average prices per country map")
        
        # Update mapbox style
        priceHeatmap.update_layout(mapbox_style="carto-darkmatter")
        priceHeatmap.update_layout(margin={"r":0,"t":50,"l":0,"b":0})
        priceHeatmap.update_layout(autosize=False, width=2000, height=800)
        priceHeatmap.update_traces(valuesuffix='Price', selector=dict(type='sankey'))

        st.plotly_chart(priceHeatmap)

    with tabWeather:    
        DaySnow = st.selectbox("Select the month to check the snow information",
                           (dfSnow['Month'].unique()))
        dfSnow = dfSnow.query("Month == @DaySnow")

        # Create a Plotly map
        geoSnowChart = px.scatter_mapbox(dfSnow, lat='Latitude', lon='Longitude', 
                                color_discrete_sequence=["ivory"], zoom=2, height=900, width=2050)
        geoSnowChart.update_layout(
                mapbox_style="white-bg",
                mapbox_layers=[
                    {
                        "below": 'traces',
                        "sourcetype": "raster",
                        "sourceattribution": "United States Geological Survey",
                        "source": [
                            "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
                        ]
                    }
                ])
        geoSnowChart.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
        st.plotly_chart(geoSnowChart)