markdown
# Media Dataset Analysis

## Overview
The dataset **media.csv** provides insights into various media types, primarily focusing on movies from language-specific genres, particularly Tamil and Telugu. The dataset captures several attributes for each movie, including release date, language, type, title, prominent actors, and their respective ratings based on overall experience, quality, and repeatability. Analyzing this dataset allows stakeholders to understand viewer feedback and trends in the film industry, potentially guiding production, marketing strategies, and future film selections.

## Data Structure
The dataset consists of the following columns:

- **date**: Release date of the movie (format: DD-MMM-YY)
- **language**: Language of the movie (e.g., Tamil, Telugu)
- **type**: Type of media (all entries are 'movie')
- **title**: Title of the movie
- **by**: Main actors featured in the movie
- **overall**: Overall rating (scale: 1 to 5)
- **quality**: Quality rating (scale: 1 to 5)
- **repeatability**: Repeat watch value (scale: 1 to 3)

### First Few Rows of Data
|     date    | language | type  |       title       |               by               | overall | quality | repeatability |
|:-----------:|:--------:|:-----:|:------------------:|:-------------------------------:|:-------:|:-------:|:-------------:|
| 15-Nov-24   |  Tamil   | movie |    Meiyazhagan    |  Arvind Swamy, Karthi          |   4     |   5     |       1       |
| 10-Nov-24   |  Tamil   | movie |     Vettaiyan     | Rajnikanth, Fahad Fazil        |   2     |   2     |       1       |
| 09-Nov-24   |  Tamil   | movie |      Amaran       |  Siva Karthikeyan, Sai Pallavi |   4     |   4     |       1       |
| 11-Oct-24   | Telugu   | movie |       Kushi       |  Vijay Devarakonda, Samantha   |   3     |   3     |       1       |

## Statistical Analysis
### Summary Statistics
| Statistic | overall | quality | repeatability |
|-----------|---------|---------|---------------|
| Mean      | 3.05    | 3.21    | 1.49          |
| Std Dev   | 0.76    | 0.80    | 0.60          |
| Min       | 1.00    | 1.00    | 1.00          |
| Max       | 5.00    | 5.00    | 3.00          |

### Correlation Analysis
The correlation matrix reveals significant relationships among the ratings:
- **Overall vs Quality**: 0.83 (strong positive correlation)
- **Overall vs Repeatability**: 0.51 (moderate positive correlation)

## Outliers
Using the Z-score method, no outliers were detected within the dataset.

## Scatter Plot Description
![Scatter Plot: overall vs quality](scatter_plot.png)

### Axes
- **X-axis**: Overall rating (1 to 5)
- **Y-axis**: Quality rating (1 to 5)

### Data Points
Different colors represent the "overall" ratings:
- Purple (1)
- Blue (2)
- Green (3)
- Yellow (4)
- Black (5)

### Key Points and Trends
- **Cluster at Lower Values**: Notable clustering in the lower left quadrant, indicating many movies score low in both overall experience and quality.
- **Diagonal Trend**: A visible trend line suggests that as overall ratings increase, quality ratings also tend to increase, supporting a positive correlation.
- **Anomalies**: Consistent ratings are seen at (2, 2) and (3, 3), while high overall scores (3, 4) and (4, 5) reflect a strong relationship.

### Legend
A color-coded legend aids in understanding the distribution of ratings.

## Interpretation
### Linear Regression Summary: Overall -> Repeatability
- **Intercept**: 0.2685
- **Coefficient**: 0.4024
- **Mean Squared Error (MSE)**: 0.2638
- **R² Score**: 0.2628

This regression indicates a weak model fit, suggesting that while overall ratings have a positive relationship with repeatability scores, further improvements in predictor variables or data quality may be needed.

## Implications
- **Actionable Insights**: The data indicates a strong positive relationship between overall ratings and quality, suggesting efforts to improve quality could enhance viewers' overall ratings.
- **Areas for Investigation**: Examine movies with low scores to identify common factors affecting ratings.

## Key Findings
- The dataset features primarily Tamil and Telugu movie ratings.
- A significant positive correlation exists between overall and quality ratings.
- No outliers were detected.
- The scatter plot shows a clear trend where higher overall ratings correspond to better quality ratings.
- The linear regression model indicates a weak but positive predictive relationship between overall ratings and repeatability.

## Conclusion
This analysis of the media dataset highlights important trends and relationships in movie ratings, indicating actionable insights for production and marketing. The strong correlation between quality and overall ratings emphasizes the necessity for high-quality productions to achieve favorable viewer experiences. Further investigation into low-rated movies can yield valuable information for industry stakeholders looking to improve their offerings.
