# Proposal

## Motivation and Purpose

**Our Role**:\
We are a team of data scientists passionate about making global well-being insights more accessible.

**Target Audience:**\
Our dashboard is designed for the general public, students, sociologists, and researchers. Basically, anyone interested in exploring well-being and happiness trends.

The [World Happiness Report](https://worldhappiness.report/) provides yearly reports on happiness across the globe and they provide valuable data. Their current dashboard provides interesting visualizations, however, it presents some portions of the report which makes it difficult to explore long term trends and compare multiple factors.

Our interactive dashboard enables users to explore and compare factors related to happiness more robustly. By selecting continent, adjusting filters, and choosing key comparison categories, users can observe trends across different countries through several years. Our dashboard contains features such as an interactive maps, charts, and plots that aids users to understand trends in happiness-related metrics such as GDP, Social support and Life Expectancy.

Our goal is to make the World Happiness Report more accessible to students, educators, researchers for deeper insights and informed discussions regarding global happiness.

## Description of the Data

Our data consists of 5 datasets, one dataset from each year from 2020-2025, from the World Happiness Report. These datasets cover approximately 140-150 countries per year. They include key features that contribute to each countries rank, called `Ladder Score` (happiness ranking). These features are related to economy, social factors, and governance.

### Data Types:

- `Country Name`: name of country (categorical)
- `Regional indicator`: geographical region (categorical) - not included in every years raw data, but added in our processed data
- `Ladder score`: Overall happiness ranking (numerical)
- `Explained by: Log GDP per capita`: Economic well-being (numerical)
- `Explained by: Social support`: Social well-being (numerical)
- `Explained by: Healthy life expectancy`: Expected healthy lifespan (numerical)
- `Explained by: Freedom to make life choices`: Individual autonomy (numerical)
- `Explained by: Generosity`: Generous behaviors in the country (numerical)
- `Explained by: Perceptions of corruption`: Trust in institutions and government (numerical)

We will also derive `Happiness Rank Change`, which will be a numerical column capturing the difference in a countries ranking between years. Additionally, we will create a numerical feature called `regional average`, which aggregates happiness scores across continents for regional comparison.These engineered features will enable users to explore and understand global well-being on a deeper level.

Additionally, we will combine these datasets and ensure every country is assigned to a region.

## App sketch & brief description

This is a single-page app that allows users to make selections through dropdown menus to compare the world happiness data by following the step-by-step instructions on the page, navigating from the left to right side of the app. Users start by selecting a continent. Upon selection, map will zoom into the continent chosen. They can then choose how many countries they would like to see in the result using an interactive slider, and will be shown line charts of the top countries according to the chosen comparison criteria (e.g. GDP, Freedom, etc). Then, continuing further to the right of the page, users can select through dropdown menus the top 5 most important comparison criteria and the countries they would like to see compared, and a radar chart will be shown at the bottom right. Here, countries of different continents can be selected for comparison. Tooltips showing data point values on hover are available on all charts and the map, and users can navigate to any future or previous steps at any time without having to follow any specific order, if they wish.

<br><br>

![app sketch](sketch.jpg "App Sketch")
