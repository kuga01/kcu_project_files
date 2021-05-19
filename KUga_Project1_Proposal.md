## Design a System to Identify NYC Subway Stations With the Most Targetted Audience
---
Kalu Chibueze Uga

#### Abstract
---
Women Tech Women Yes (WTWY) reached out to my firm and asked us to use the New York City (NYC) Metropolitan Transportation Authority (MTA) subway turnstile data to help them target a large pool of potential gala participants who also have a high probability to contribute to their organization. We propose to design a system that will use the NYC MTA turnstile data and income distribution in the city to properly target audience for WTWY gala.


#### Design
---

* The designed system will look into the busiest entries and exits period during the weekdays and make recommendations to WTWY based on the peak activity period. An efficient way to target desired audience will be to place WTWY agents at the busy stations during peak activity periods.
* WTWY will benefit greatly from this system because the targeted audience are more likely to attend the gala and make contributions to the organization.


#### Data 
---

* The primary dataset is a 12-week NYC MTA turnstile data that will be gathered from [MTA](http://web.mta.info/developers/data/nyct/turnstile/).
* The secondary dataset will be reliable data that shows income distribution in NYC by zip code. No definite source at this time.
* An individual sample size is the weekly dataset from NYC MTA turnstile that is collected every four hours. This project will be exploring turnstile entries and exits on busy weekday.
* The target of this project are individuals who earn above average income in NYC because they have a higher chance of making contributions to WTWY at the gala.

#### Tools
---

* Pandas will be used for data acquisition, data cleansing, database setup, and data maniputation. 
* Matplotlib will be used for data visualization.


#### MVP Goal
---

* The goal of the project is to find a set of busy NYC subway stations in high-income zipcodes and propose the best period for a WTWY agent to collect emails on weekdays.
* The findings will be communicated through graph.
