# Milestone 4 Reflection

## Implementations Since Last Milestone

### App Functionality

- Included sidebar texts to for data interpretation
- Used caching to load data
- Displayed loading spinner wheels
- Normalized data for all categories to be on the same scale
- Had bar chart annotation show 'Continent Average' when comparing all continents
- Set default filter values to display initial radar chart

### Data Processing

- Created .parquet files for reading data
- Fixed issue of some countries not showing up

### App Design

- Created separate tab for radar chart
- Converted line chart to bar chart
- Ensured horizonal orientation x-axis labels
- Moved bar chart annotations to right of plot
- Moved app creator information to footer and added data source
- Set favicon and tab title for the webpage

### Documentation

- Updated demo.gif and texts in README to reflect current state of app

## Major Feature Modifications from Proposal

### Bar Chart

Bar chart can be more impactful visually than line charts for comparing data between countries.

### Tab View

Since radar chart generation requires distinct user controls (i.e. filters) from the rest of the app, it makes more sense to move it to a different tab.

### Side Bars

Sticky side bars that remain in place when scrolling nest filters for customized data visualizations. This makes it especially easier for users to navigate a long webpage with a large map and bar chart and is a better design than we originally had where filters are positioned on top of the data visualizations.

### Abandoned Feature

Zooming in and out on the map due to limitation of Altair package (with instructor's approval)

## Impact, Limitations & Opportunities

What we do well:

- App has functionalities specifically targeting a well-defined group of users, geared especially towards those needing information for immigration decisions, to enable comparison of categories important to lifestyle satisfication and financial wellbeing
- App visualizes comparisons across all continents as well as within continents by displaying the top 10 countries, providing users concise data summaries of each happiness category
- App lets users decide which countries and categories to compare, creating a customized data visualization experience that are meaningful on a personal level
- App explains how to interpret the data with example, ensuring users understand what the numbers represent
- App has a clear layout and designed to make navigation easy and intuitive for users with all technical backgrounds

Future improvements:

- Continue to investigate reasons for few countries still not showing up in data visualizations
- Seek alternative data visualization tools and customization methods to:
  - Enable zooming in and out on the map and faciliate smooth scrolling while cursor is on the map
  - Show more accurate-to-hover tooltip information on radar chart
  - Improve how professional-looking the data visualizations are
- Improve app speed through alternative deployment tools and optimization of backend data processing
- Further improve consistency of color theme, app design and interactivity
