# Milestone 2 Reflection

## What's Different From The Proposal

### App Functionality

We have implemented most features in our app sketch. One feature we decided to not implement is the slider to show the number of countries to display in the line chart as we would like more consistent data display and we think top 10 could be a reasonable number for most app users.

Additional improvements we made include:

- Constraint on the maximum number of countries allowed to be selected
- Descriptive title for line chart including name of continent and category selected
- Numeric value added for continent average on line chart

**Though the interactive map is working locally, it is not showing up in the deployed app.**

### Dashboard Design

![app sketch](../img/sketch.png "Original App Sketch")
![updated app layout](../img/updated_prototype_sketch.jpg "Updated Sketch")

### Data Aggregation and Feature Engineering

To improve dashboard intuitiveness and effectiveness, we standardized feature names across five raw datasets and adjusted included features based on the updated design. We introduced `Continent` to provide additional geographical context, as it is a field not available in the raw data. Core happiness and well-being indicators, such as `Happiness Score`, `GDP per Capita`, `Social Support`, `Healthy Life Expectancy`, `Freedom to Make Life Choices`, `Generosity`, and `Perceptions of Corruption`, were retained. To enhance regional insights, we added aggregate features, including `Average Continent Happiness Score`, `Average Continent GDP per Capita`, `Average Continent Social Support`, `Average Continent Healthy Life Expectancy`, `Average Continent Freedom to Make Life Choices`, `Average Continent Generosity`, and `Average Continent Perceptions of Corruption`, which provide comparative metrics at the continental level. Additionally, we removed `Happiness Rank Change` to align with the revised design. We also removed `Region` due to each region only maps to 5-20 countries and would not be useful in our updated dashboard design. The final dataset was compiled using an ETL process using a [python script](./notebooks/Happiness_data_ETL_pipeline.ipynb), ensuring consistency and direct integration into the visualization.

## Impact, Limitations & Opportunities

What we do well:

- App has a clear layout with 3 distinct sections and is relatively intuitive for users to understand
- Dropdown menus are distinguished from each other and well-organized
- Line chart shows continent averages, helping users compare the top 10 countries with other countries in the continent
- Each chart serves a unique functionality, enabling users to peek into the data from different perspectives

Future improvements:

- Improve app design (color theme, layout, font sizes, etc)
- Add descriptions for dropdowns where needed to help users understand how to use the app
- Make interactive map work on deployed app
- Handle edge case scenarios (e.g. if users made selections where no data is available to display)
- Fix axis values or adjust dataset values so that shaded areas are more visible in the radar chart
- Fix radar chart tooltip labels so it says country and categories along with their values
- (Time permitted) Make more informative design decisions in storytelling and data visualization
