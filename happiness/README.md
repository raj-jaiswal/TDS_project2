# Happiness Data Analysis

## Overview
The dataset titled `happiness.csv` encompasses a range of indicators measuring the happiness and well-being of various countries over different years. The key variables of interest include the Life Ladder score, Log GDP per capita, social support, healthy life expectancy, freedom to make choices, generosity, perceptions of corruption, and levels of positive and negative affect. This analysis aims to uncover insights into how these factors correlate with happiness and explore notable trends within the data.

## Data Structure
The dataset contains the following columns:

- **Country name**: Name of the country
- **Year**: The year in which the data was collected
- **Life Ladder**: A score representing overall life satisfaction
- **Log GDP per capita**: The logarithm of the GDP per capita, serving as a measure of economic prosperity
- **Social support**: The extent of assistance available to individuals in their community
- **Healthy life expectancy at birth**: Average number of years a newborn is expected to live in good health
- **Freedom to make life choices**: The degree of freedom people feel they have in making life choices
- **Generosity**: A measure of charitable giving
- **Perceptions of corruption**: A measure of public perception regarding the level of corruption in government and business
- **Positive affect**: A score representing positive feelings and moods
- **Negative affect**: A score representing negative feelings and moods

## Statistical Analysis
The statistical overview of the dataset reveals:

- **Mean Values**:
  - Life Ladder: 5.48
  - Log GDP per capita: 9.40
  - Social support: 0.81 
  - Healthy life expectancy: 63.40 years
  - Freedom to make life choices: 0.75
  - Generosity: 0.0001
  - Perceptions of corruption: 0.74
  - Positive affect: 0.65
  - Negative affect: 0.27 

- **Standard Deviations** indicate variation:
  - Life Ladder: ±1.13
  - Log GDP per capita: ±1.15
  - Social support: ±0.12 

- **Range of Values**:
  - Life Ladder spans from 1.28 to 8.02, showcasing significant variation in happiness levels across countries and years.

## Correlation Analysis
The relationships between the various factors are noteworthy:

- The highest correlation was observed between **Log GDP per capita** and **Life Ladder** (0.78), illustrating a strong relationship between economic prosperity and life satisfaction.
- **Social support** (0.72) and **healthy life expectancy** (0.71) also exhibit significant positive correlations with happiness, indicating that communities that provide robust support and health services tend to yield happier citizens.
- **Freedom to make life choices** (0.54) suggests that personal autonomy is essential for perceived happiness.

## Outliers
Outlier detection using the z-score method identified several unusual data points:

1. **Afghanistan** in 2022 and 2023 showed extreme low Life Ladder scores (1.281 and 1.446 respectively), revealing the country’s ongoing struggles.
2. **Venezuela's** scores from 2017 to 2019 displayed concerning patterns in life satisfaction amidst economic challenges.
3. A few entries from **Bangladesh** and **Benin** also reflected lower life satisfaction in specific years.

## Interpretation
This dataset paints a poignant picture of global happiness dynamics. Countries with robust economic indicators such as high GDP per capita and healthy life expectancy tend to have higher life satisfaction, as evidenced by the significant correlations. However, anomalies, as identified in outlying countries, suggest that economic metrics alone do not capture the full fabric of happiness, as social factors and perceptions of well-being are crucial.

## Key Findings
- Economic prosperity is closely tied to happiness, but social support and health also play pivotal roles.
- Outlier countries like Afghanistan and Venezuela exemplify challenges that impede happiness despite other potential indicators.
- Personal freedoms and community supports emerge as necessary elements for enhancing life satisfaction.

## Conclusion
In summary, the analysis of the `happiness.csv` dataset underscores the multifaceted nature of happiness, emphasizing that while economic and health factors are vital, social influences and individual freedoms significantly contribute to how people perceive their lives. The correlations and outlier observations serve as critical reminders of the ongoing global challenges in enhancing human well-being.

![Scatter Plot](scatter_plot.png)
*The scatter plot above illustrates the relationship between Life Ladder and Log GDP per capita, further emphasizing the strong correlation identified through statistical analysis.*