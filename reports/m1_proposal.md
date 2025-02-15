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

Our data consists of 5 datasets, one dataset from each year from 2020-2024, from the World Happiness Report. These datasets cover approximately 140-150 countries per year. They include key features that contribute to each countries rank, called `Ladder Score` (happiness ranking). These features are related to economy, social factors, and governance.

### Data Types:

-   `Country Name`: name of country (categorical)
-   `Regional indicator`: geographical region (categorical) - not included in every years raw data, but added in our processed data
-   `Ladder score`: Overall happiness ranking (numerical)
-   `Explained by: Log GDP per capita`: Economic well-being (numerical)
-   `Explained by: Social support`: Social well-being (numerical)
-   `Explained by: Healthy life expectancy`: Expected healthy lifespan (numerical)
-   `Explained by: Freedom to make life choices`: Individual autonomy (numerical)
-   `Explained by: Generosity`: Generous behaviors in the country (numerical)
-   `Explained by: Perceptions of corruption`: Trust in institutions and government (numerical)

We will also derive `Happiness Rank Change`, which will be a numerical column capturing the difference in a countries ranking between years. Additionally, we will create a numerical feature called `regional average`, which aggregates happiness scores across continents for regional comparison.These engineered features will enable users to explore and understand global well-being on a deeper level.

The datasets will be loaded from the World Happiness Report website. Additionally, we will combine these datasets and ensure every country is assigned to a region.

## Research Questions and Usage Scenarios

Tomasz is a 30-year-old businessman. He wants to explore the possibility of immigrating to another country as he is unhappy with the political situations and lifestyles in his country. He wants to see which countries offer the best possible conditions for him and his girlfriend to live in long-term and wants to pick a country based on factors including level of corruption, citizen freedom, GDP, and potential others, that are important to him.

When Tomasz opens the app, he will be shown step-by-step instructions leading him to first explore continents of his interest, then explore countries of his interest based on the different happiness criteria, navigating from the left to right side of the page. Tomasz starts by selecting a continent then choosing how many countries they would like to see in the result using an interactive slider, as well as the happiness criteria (e.g. GDP, Freedom, etc). Upon selection of continent, map will zoom into the continent chosen, and Tomasz will be shown line charts of the top countries according to the chosen criteria for comparison. If after viewing these, he has some ideas about which countries might be his favourites, he can then continue to the right to select his top 5 most important happiness criteria and the countries he would like to see compared in those criteria. A radar chart will be shown at the bottom right. Here, countries of different continents can be selected for comparison.

For example, Tomasz may decide to choose Europe as a continent first and see which 5 European countries rank highest in the 3 criteria of interest to him: Freedom, GDP, and Perception of Corruption. He may then change the continent to North America and Oceania and do similar comparisons. Afterwards, he decided France, Australia, and Canada are his top favourite countries around the world and used a radar chart to see how these 3 countries compare in his top 5 priorities: Freedom, Perception of Corruption, Life Expectancy, GDP, and Social Support. By examining the radar chart, he will get an overall picture of how the 3 countries compare according to his happiness priorities and make a final decision on where to immigrate to, or conduct further research on Google for any other questions that he has, such as immigration processes, to help him narrow down the selection.

## App Sketch & Brief Description

The application consists of three key sections, each enabling users to explore and compare global happiness metrics independently. These sections provide interactive visualizations and filtering options to facilitate data exploration and analysis.

-   **Left Panel:** This section features an interactive world map where users can filter by continent to examine individual countries' happiness rankings. Hovering over a country dynamically displays its happiness rank in a tooltip, offering an intuitive way to explore regional variations.

-   **Middle Panel:** Users can analyze specific attributes such as Log GDP per capita and Social Support through an interactive slider and dropdown menus. The slider allows users to define the number of top-ranked countries to include, while the dropdown enables attribute selection. The selected attributes are visualized using line charts to show trends and comparisons across the chosen countries.

-   **Right Panel:** This section provides multiple dropdown menus for users to select specific attributes and countries for direct comparison. A polygon (radar) plot is generated to illustrate the differences among the selected attributes across the chosen countries. Constraints are applied to ensure a manageable number of selections for clear and meaningful visualization.

By integrating these interactive components, the application enables users to explore world happiness data from multiple perspectives, facilitating insights into regional patterns, key contributing factors, and cross-country comparisons.

<br><br>

![app sketch](../img/sketch.png "App Sketch")
