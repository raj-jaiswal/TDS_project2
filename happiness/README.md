# Happiness Dataset Analysis

## Overview
The dataset `happiness.csv` contains multidimensional data related to happiness metrics across various countries over different years. It includes various factors thought to influence life satisfaction and well-being, such as economic performance, social support, health metrics, and perceptions of freedom and corruption. This analysis aims to explore the relationships between these variables and identify significant patterns, trends, and outliers, providing actionable insights for policymakers and researchers.

## Data Structure
The dataset consists of the following columns:

- **Country name**: Name of the country.
- **Year**: Year of measurement.
- **Life Ladder**: A numerical measure of subjective well-being.
- **Log GDP per capita**: Logarithm of GDP per capita, a measure of economic performance.
- **Social support**: A measure of social relationships and community support.
- **Healthy life expectancy at birth**: Expected number of years a newborn would live in good health.
- **Freedom to make life choices**: A measure of individual freedom and agency.
- **Generosity**: A measure of altruistic behavior.
- **Perceptions of corruption**: A measure of trust in government and business.
- **Positive affect**: A measure of positive emotions experienced.
- **Negative affect**: A measure of negative emotions experienced.

### First Few Rows of Data
plaintext
| Country name | Year | Life Ladder | Log GDP per capita | Social support | Healthy life expectancy at birth | Freedom to make life choices | Generosity | Perceptions of corruption | Positive affect | Negative affect |
|--------------|------|-------------|---------------------|----------------|----------------------------------|-----------------------------|------------|--------------------------|----------------|-----------------|
| Afghanistan  | 2008 | 3.724       | 7.35                | 0.451          | 50.5                             | 0.718                       | 0.164      | 0.882                    | 0.414          | 0.258           |
| Afghanistan  | 2009 | 4.402       | 7.509               | 0.552          | 50.8                             | 0.679                       | 0.187      | 0.85                     | 0.481          | 0.237           |
| Afghanistan  | 2010 | 4.758       | 7.614               | 0.539          | 51.1                             | 0.600                       | 0.118      | 0.707                    | 0.517          | 0.275           |
| Afghanistan  | 2011 | 3.832       | 7.581               | 0.521          | 51.4                             | 0.496                       | 0.160      | 0.731                    | 0.480          | 0.267           |


## Statistical Analysis
### Summary Statistics

The summary statistics for the dataset are as follows:

| Statistic | Year       | Life Ladder | Log GDP per capita | Social support | Healthy life expectancy at birth | Freedom to make life choices | Generosity | Perceptions of corruption | Positive affect | Negative affect |
|-----------|------------|-------------|---------------------|----------------|----------------------------------|-----------------------------|------------|--------------------------|----------------|-----------------|
| Mean      | 2014.76    | 5.48        | 9.40                | 0.81           | 63.40                            | 0.75                        | 0.0001     | 0.74                     | 0.65           | 0.27            |
| Std Dev   | 5.06       | 1.13        | 1.15                | 0.12           | 6.84                             | 0.14                        | 0.16       | 0.18                     | 0.11           | 0.09            |
| Min       | 2005       | 1.28        | 5.53                | 0.23           | 6.72                             | 0.23                        | -0.34      | 0.04                     | 0.18           | 0.08            |
| Max       | 2023       | 8.02        | 11.68               | 0.99           | 74.60                            | 0.99                        | 0.70       | 0.98                     | 0.88           | 0.71            |

### Correlation Analysis
The correlation matrix distributed from a Pearson correlation analysis highlights significant correlations among variables:

- Life Ladder & Log GDP per capita: **0.7836**
- Life Ladder & Social support: **0.7227**
- Life Ladder & Healthy life expectancy at birth: **0.7149**
- Log GDP per capita & Healthy life expectancy at birth: **0.8193**
  
These correlations indicate strong relationships between economic performance (GDP) and both subjective well-being (Life Ladder) and health metrics.

## Outliers
Detected outliers using the Z-score method indicate the following entries, which can skew results or point to atypical scenarios in the data:

| Country name | Year | Life Ladder | Log GDP per capita | Social support | Healthy life expectancy at birth | Freedom to make life choices | Generosity | Perceptions of corruption | Positive affect | Negative affect |
|--------------|------|-------------|---------------------|----------------|----------------------------------|-----------------------------|------------|--------------------------|----------------|-----------------|
| Afghanistan  | 2022 | 1.281       | NaN                 | 0.228          | 54.875                           | 0.368                       | NaN        | 0.733                    | 0.206          | 0.576           |
| Venezuela     | 2017 | 5.071       | 5.943               | 0.896          | 64.750                           | 0.636                       | 0.050      | 0.844                    | 0.697          | 0.363           |

Afghanistan experiences a critically low Life Ladder score in 2022, indicating severe distress, while Venezuela's data points suggest improving conditions post-2017 despite economic struggles.

## Scatter Plot Description
The scatter plot visualized as "scatter_plot.png" shows the relationship between the Life Ladder and Log GDP per capita. The analysis reveals a positive trend, where higher economic performance correlates significantly with increased life satisfaction. However, notable outliers indicate deviations that suggest socio-economic conditions and public sentiment might not always align with expectations based on GDP.

## Interpretation
The insights suggest that while economic indicators like GDP are important, they are not the sole determinants of happiness. Factors such as social support, health, and freedoms also play crucial roles. The correlations demonstrate interconnectedness between these variables, where improvement in one could lead to enhancements in overall well-being.

## Key Findings
- **Strong correlations** exist among Life Ladder, GDP, social support, and health metrics, underscoring the importance of economic prosperity in promoting happiness.
- **Outliers** might indicate countries facing unique challenges that impact well-being despite economic metrics.
- **Visual analysis** of the relationship between Life Ladder and GDP highlights the importance of contextual factors beyond wealth accumulation.

## Conclusion
The analysis of the `happiness.csv` dataset reveals intricate relationships among various factors influencing well-being across nations. The significant correlations, statistical exploration, and identification of outliers provide valuable insights for policymakers, highlighting the complexities of happiness. Prioritizing social support, health, and sense of freedom alongside economic development can create a holistic approach towards enhancing life satisfaction globally. Further investigation into specific countries and conditions could yield actionable strategies for improving happiness metrics.