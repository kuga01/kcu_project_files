# Identifying NYC Subway Stations With the Most Target Audience
Kalu Chibueze Uga

## Abstract
The goal of this project is to help Women Tech Women Yes (WTWY) identify the top subway stations in New York City where they can place agents to collect email addresses for their upcoming gala. I worked with NYC MTA turnstile data set and 2019 NYC Median household Income data from U.S. Bureau of Labor Statistics. After cleaning the turnstile data, high target subway stations were identified by screening for stations with high daily activity and matching those stations to NYC zip codes with high Median household income (greater than $90,000.00). Folium was used to build an interactive map that communicates the findings.

## Design
This project design was based on the assumption that WTWY is interested in capturing audience that will make donations at the gala. The designed system focused on the stations with high daily activity (sum of daily entries and exits)  during the weekdays and identified periods with peak activity during the day. This system will enable WTWY to efficiently reach the desired audience by placing agents at the target station during peak activity periods. 

## Data
The primary dataset consists of 11-week NYC MTA turnstile data and the secondary data is the 2019 NYC median househole income data. The turnstile data coonsists of data from 378 stations while the data on median income consists of median household income for 187 NYC zip codes.  A GeoJson file which consists of the coordinates of the polygon that maps NYC zip codes was overlayed on the map of NYC in folium so that an interactive chart with style and highlight functions could be generated. 

## Algorithms

*Data Cleaning*
1. Removed unwanted spaces in column headers
2. Dropped duplicate rows and replaced  rows with null values.
3. It is safe to assume that an efficient turnstile can allow 1 person per second which is equivalent to 3600 persons per hour, 14400 persons per 4 hrs and 86400 persons per day. Thus, the total daily sum of ENTRIES and EXITS for a turnstile should not be more than 86400. 
4. Identified days with reverse counts and used the "get_daily_counts" function to resolve the issue. The choice of the max_counter was based on the statistics of the field (ENTRIES or EXITS). The outlier was at the max value whereas the 75th and 99th percentile values were reasonable and not too far apart. I used the 99th percentile values.  
    - For daily analysis, set "max_counter" for entries and exits to 1444 and 1868 respectively.
    - For 4 hr analysis, set "max_counter" for entries and exits to 808 and 1039 respectively.

*Interactive Map Visualization*
1. Read NYC GeoJson file into pandas using geopandas
2. Renamed "postalCode" attribute to "ZIPCODE".
3. Merged the GeoJson dataframe to our target stations dataframe (RIGHT JOIN).
4. Used folium highlight and style functions to create interactive map of target stations. On mousehover, the display shows ZIPCODE, Median Household Income, Subway Station, and Average Daily Activity.

## Tools
- Numpy and Pandas were used for data manipulation
- Matplotlib and seaborn for plotting.
- Folium and geopandas for interctive map visualization.

## Communication
Screenshots of the recommended target stations are presented below.
| Average Daily Activity at Target Stations | Interactive Map of Target Stations |
|:----: |:------:|
| <img src="https://github.com/kuga01/kcu_project_files/blob/main/MTA_Project_Final/plots/Subway_target_stations.png" width = "450" height = "225">   | <img src="https://github.com/kuga01/kcu_project_files/blob/main/MTA_Project_Final/plots/Subway_nyc_map_2.png" width = "450" height = "225">    |
