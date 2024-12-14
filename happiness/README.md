# Happiness Data Analysis

## Overview
The happiness dataset, named `happiness.csv`, includes happiness-related factors across different countries and years. The data comprises ten variables related to well-being, including measures of economic prosperity, social support, personal freedoms, and perceptions of corruption. This analysis provides an overview of the dataset, statistical analyses of its variables, and insights based on the correlations found among them.

## Data Structure
The dataset has the following columns:
- **Country name**: The name of the country.
- **Year**: The year the data corresponds to.
- **Life Ladder**: A measure for subjective well-being or happiness.
- **Log GDP per capita**: The logarithm of the GDP per capita, serving as an economic indicator.
- **Social support**: A measure of the perceived social support received by individuals.
- **Healthy life expectancy at birth**: The average number of years a newborn is expected to live in good health.
- **Freedom to make life choices**: Perceived personal freedoms in decision-making.
- **Generosity**: A measure of self-reported generosity.
- **Perceptions of corruption**: Individuals' views on the level of corruption in their country.
- **Positive affect**: A measure of positive feelings experienced by individuals.
- **Negative affect**: A measure of negative feelings experienced by individuals.

### Sample Data
The first few rows of the dataset illustrate the variability in happiness measures over different years for Afghanistan:

| Country Name | Year | Life Ladder | Log GDP per capita | Social support | Healthy life expectancy at birth | Freedom to make life choices | Generosity | Perceptions of corruption | Positive affect | Negative affect |
| ------------ | ---- | ----------- | ------------------- | -------------- | ------------------------------- | ---------------------------- | ---------- | ------------------------ | ---------------- | ---------------- |
| Afghanistan  | 2008 | 3.724       | 7.35                | 0.451          | 50.5                           | 0.718                        | 0.164      | 0.882                    | 0.414             | 0.258            |
| Afghanistan  | 2009 | 4.402       | 7.509               | 0.552          | 50.8                           | 0.679                        | 0.187      | 0.85                     | 0.481             | 0.237            |
| Afghanistan  | 2010 | 4.758       | 7.614               | 0.539          | 51.1                           | 0.600                        | 0.118      | 0.707                    | 0.517             | 0.275            |
| Afghanistan  | 2011 | 3.832       | 7.581               | 0.521          | 51.4                           | 0.496                        | 0.160      | 0.731                    | 0.480             | 0.267            |

## Statistical Analysis
The following statistics summarize the main features of the dataset:

- **Mean**:
  - Year: 2014.76
  - Life Ladder: 5.48
  - Log GDP per capita: 9.40
  - Social Support: 0.81
  - Healthy Life Expectancy: 63.40
  - Freedom to Make Life Choices: 0.75
  - Generosity: 0.0001
  - Perceptions of Corruption: 0.74
  - Positive Affect: 0.65
  - Negative Affect: 0.27

- **Standard Deviation**:
  - Year: 5.06
  - Life Ladder: 1.13
  - Log GDP per capita: 1.15
  - Social Support: 0.12
  - Healthy Life Expectancy: 6.84
  - Freedom to Make Life Choices: 0.14
  - Generosity: 0.16
  - Perceptions of Corruption: 0.18
  - Positive Affect: 0.11
  - Negative Affect: 0.09

- **Range**:
  - Year: 2005 - 2023
  - Life Ladder: 1.28 - 8.02
  - Log GDP per capita: 5.53 - 11.68
  - Social Support: 0.23 - 0.99
  - Healthy Life Expectancy: 6.72 - 74.60
  - Freedom to Make Life Choices: 0.23 - 0.99
  - Generosity: -0.34 - 0.70
  - Perceptions of Corruption: 0.04 - 0.98
  - Positive Affect: 0.18 - 0.88
  - Negative Affect: 0.08 - 0.71

These statistics highlight a significant range of happiness measurements across different countries and years, indicating that happiness levels vary widely depending on various factors.

## Correlation Analysis
The correlation matrix shows strong positive relationships among several variables, particularly:

- Life Ladder and Log GDP per capita: **0.78**
- Life Ladder and Social support: **0.72**
- Life Ladder and Healthy life expectancy: **0.71**
- Life Ladder and Freedom to make life choices: **0.54**
- Life Ladder and Positive affect: **0.52**

These correlations suggest that a higher GDP per capita, better social support, and healthier life expectancy are associated with higher self-reported happiness levels.

## Outliers
Through z-score analysis, several outliers were detected in the dataset, including:

| Country Name | Year | Life Ladder | Log GDP per capita | Social Support | Healthy Life Expectancy at Birth | Freedom to Make Life Choices | Generosity | Perceptions of Corruption | Positive Affect | Negative Affect |
| ------------ | ---- | ----------- | ------------------- | -------------- | ------------------------------ | ---------------------------- | ---------- | ------------------------ | ---------------- | ---------------- |
| Afghanistan  | 2022 | 1.281       | NaN                 | 0.228          | 54.875                         | 0.368                        | NaN       | 0.733                    | 0.206             | 0.576            |
| Afghanistan  | 2023 | 1.446       | NaN                 | 0.368          | 55.200                         | 0.228                        | NaN       | 0.738                    | 0.261             | 0.460            |
| Venezuela     | 2017 | 5.071       | 5.943               | 0.896          | 64.750                         | 0.636                        | 0.050      | 0.844                    | 0.697             | 0.363            |
| Bangladesh   | 2022 | 3.408       | 8.742               | 0.404          | 64.675                         | 0.865                        | -0.058     | 0.617                    | 0.394             | 0.448            |

Outliers, particularly from Afghanistan and Venezuela, indicate relatively lower life ladder scores despite varying economic or social support indicators.

## Interpretation
The dataset reveals essential insights into global happiness and well-being. The correlation analysis indicates significant positive relationships between various determinants of happiness, particularly economic factors and social support. Countries with higher GDP and social connectivity tend to report higher levels of happiness; however, even nations with high GDP can experience low happiness rankings, as shown by the Afghan entries for 2022 and 2023.

![scatter_plot.png](scatter_plot.png)
*Figure 1: Scatter plot illustrating the relationship between Life Ladder and Log GDP per capita.*

The scatter plot reinforces the positive correlation between happiness (Life Ladder) and economic prosperity (Log GDP per capita), illustrating that countries with higher GDP typically report higher happiness levels.

## Key Findings
1. Economic prosperity (measured as Log GDP per capita) significantly contributes to national happiness levels.
2. Social support and health factors are also crucial in determining overall life satisfaction.
3. Specific nations, particularly Afghanistan, demonstrate extreme variability in happiness scores, with economic indicators not fully capturing subjective well-being.

## Conclusion
The analysis of the happiness dataset provides valuable insights into the contributing factors of happiness across different countries and years. By understanding the correlation between economic prosperity, social support, and life expectancy, policymakers can target improvements in these areas to enhance the overall well-being of their populations. Future research could focus on the underlying causes of low happiness in specific countries, such as those exhibiting extreme outlier scores, to create targeted interventions for improving well-being.