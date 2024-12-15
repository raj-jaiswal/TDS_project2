# Goodreads Dataset Summary

## Overview
The dataset `goodreads.csv` consists of comprehensive information about a collection of books listed on Goodreads. This dataset is prime for analysis related to literary trends, author popularity, and reader engagement. It includes valuable metrics like average ratings, the number of ratings, and reader reviews, making it suitable for studies in bibliometrics, sentiment analysis, and machine learning applications in NLP.

## Data Structure
The dataset contains the following columns:
- **book_id**: Unique identifier for each book.
- **goodreads_book_id**: Goodreads specific book identifier.
- **best_book_id**: Identifier for the best-rated version of the book.
- **work_id**: Unique identifier associated with the work (all editions of the book).
- **books_count**: Number of editions or formats of the book.
- **isbn**: ISBN number for the book.
- **isbn13**: 13-digit ISBN number.
- **authors**: Names of the authors.
- **original_publication_year**: Year the book was originally published.
- **original_title**: Title as it appeared in the first publication.
- **title**: Full title of the book as listed on Goodreads.
- **language_code**: Language code indicating book's language.
- **average_rating**: Average rating received by the book.
- **ratings_count**: Total number of ratings the book has received.
- **work_ratings_count**: Total ratings across all editions.
- **work_text_reviews_count**: Number of text reviews submitted.
- **ratings_1** to **ratings_5**: Count of 1 to 5 star ratings.
- **image_url**: URL link to the book cover image.
- **small_image_url**: URL link to a smaller version of the book cover image.

### First Few Rows of Data
| book_id | goodreads_book_id | best_book_id | work_id | books_count | isbn        | isbn13            | authors                          | original_publication_year | original_title                   | title                                         | language_code | average_rating | ratings_count | work_ratings_count | work_text_reviews_count | ratings_1 | ratings_2 | ratings_3 | ratings_4 | ratings_5 | image_url                                                       | small_image_url                                                 |
|---------|--------------------|---------------|---------|-------------|-------------|-------------------|----------------------------------|---------------------------|-----------------------------------|-----------------------------------------------|---------------|-----------------|----------------|---------------------|--------------------------|------------|------------|------------|------------|------------|------------------------------------------------------------------|------------------------------------------------------------------|
| 1       | 2767052            | 2767052       | 2792775  | 272         | 439023483   | 9780439023480     | Suzanne Collins                 | 2008                      | The Hunger Games                 | The Hunger Games (The Hunger Games, #1)        | eng           | 4.34           | 4780653        | 4942365              | 155254                   | 66715      | 127936     | 560092     | 1481305    | 2706317    | https://images.gr-assets.com/books/1447303603m/2767052.jpg   | https://images.gr-assets.com/books/1447303603s/2767052.jpg   |
| 2       | 3                  | 3             | 4640799  | 491         | 439554934   | 9780439554930     | J.K. Rowling, Mary GrandPré     | 1997                      | Harry Potter and the Philosopher's Stone | Harry Potter and the Sorcerer's Stone (Harry Potter, #1)   | eng           | 4.44           | 4602479        | 4800065              | 75867                    | 75504      | 101676     | 455024     | 1156318    | 3011543    | https://images.gr-assets.com/books/1474154022m/3.jpg         | https://images.gr-assets.com/books/1474154022s/3.jpg         |
| 3       | 41865              | 41865         | 3212258  | 226         | 316015849   | 9780316015840     | Stephenie Meyer                | 2005                      | Twilight                        | Twilight (Twilight, #1)                         | en-US         | 3.57           | 3866839        | 3916824              | 95009                    | 456191    | 436802     | 793319     | 875073     | 1355439    | https://images.gr-assets.com/books/1361039443m/41865.jpg    | https://images.gr-assets.com/books/1361039443s/41865.jpg    |
| 4       | 2657               | 2657          | 3275794  | 487         | 61120081    | 9780061120080     | Harper Lee                      | 1960                      | To Kill a Mockingbird           | To Kill a Mockingbird                           | eng           | 4.25           | 3198671        | 3340896              | 72586                    | 60427      | 117415     | 446835     | 1001952    | 1714267    | https://images.gr-assets.com/books/1361975680m/2657.jpg     | https://images.gr-assets.com/books/1361975680s/2657.jpg     |

## Statistical Analysis

### Summary Statistics
The dataset has a total of **10000** entries with the following descriptive statistics:

| Statistic | book_id | goodreads_book_id | best_book_id | work_id   | books_count | isbn13              | original_publication_year | average_rating | ratings_count | work_ratings_count | work_text_reviews_count | ratings_1 | ratings_2 | ratings_3 | ratings_4 | ratings_5 |
|-----------|---------|--------------------|---------------|-----------|-------------|---------------------|---------------------------|-----------------|---------------|--------------------|--------------------------|-----------|-----------|-----------|-----------|-----------|
| Mean      | 5000.50 | 5264697            | 5471214       | 8646183   | 75.71       | 9.755044e+12        | 1981.99                   | 4.00            | 54001.24      | 59687.32           | 2919.96                  | 1345.04   | 3110.89    | 11475.89  | 19965.70  | 23789.81  |
| Std Dev   | 2886.90 | 7575462            | 7827330       | 11751060  | 170.47      | 4.428619e+11        | 152.58                    | 0.25            | 157370.00     | 167803.80         | 6124.38                  | 6635.63   | 9717.12    | 28546.45  | 51447.36  | 79768.89  |
| Min       | 1.00    | 1.00               | 1.00          | 87        | 1           | 1.951703e+08        | -1750                     | 2.47            | 2716          | 5510                | 3                        | 11        | 30        | 323       | 750.00     | 754.00    |
| Max       | 10000.00| 33288640           | 35534230      | 5639960   | 3455        | 9.790008e+12        | 2017                      | 4.82            | 4780656       | 4942365           | 155254                   | 456191   | 436802    | 793319    | 1481305   | 3011543  |

### Correlation Analysis
The correlation matrix derived from the dataset revealed several significant correlations:

| Variables                         | Correlation Coefficient |
|-----------------------------------|-------------------------|
| goodreads_book_id vs best_book_id | 0.9666                  |
| work_id vs goodreads_book_id      | 0.9294                  |
| ratings_count vs work_ratings_count| 0.9951                  |
| ratings_1 vs ratings_2            | 0.9261                  |

This indicates a high degree of collinearity between several ratings metrics and their aggregated forms.

## Outliers Detected Using the Z-Score Method
Outliers were identified based on the Z-score method, specifically in the following records:

| book_id | goodreads_book_id | best_book_id | work_id | books_count | isbn       | authors                  | original_publication_year | average_rating | ratings_count | work_ratings_count | work_text_reviews_count | ratings_1 | ratings_2 | ratings_3 | ratings_4 | ratings_5 | image_url                                                       | small_image_url                                                 |
|---------|--------------------|---------------|---------|-------------|------------|--------------------------|---------------------------|-----------------|---------------|--------------------|--------------------------|-----------|-----------|-----------|-----------|-----------|
| 278     | 29056083           | 29056083      | 48765776| 95          | 751565350  | John Tiffany, J.K. Rowling | 2016                      | 3.75           | 270603        | 397773             | 53365                    | 15828     | 35842     | 96395     | 133156    | 116552    | https://images.gr-assets.com/books/1470082995m/29056083.jpg | https://images.gr-assets.com/books/1470082995s/29056083.jpg |
| 1432    | 28187230           | 28187230      | 48209164| 37          | 1501132938 | Ruth Ware                | 2016                      | 3.67           | 90541         | 109821             | 12391                    | 2029      | 8795      | 33879     | 43732     | 21386     | https://images.gr-assets.com/books/1465878007m/28187230.jpg | https://images.gr-assets.com/books/1465878007s/28187230.jpg |
| 1498    | 28587957           | 28587957      | 45950662| 46          | 345544951  | Jodi Picoult             | 2016                      | 4.35           | 73745         | 97404              | 11839                    | 1035      | 2060      | 9633      | 33373     | 51303     | https://images.gr-assets.com/books/1468057481m/28587957.jpg | https://images.gr-assets.com/books/1468057481s/28587957.jpg |
| 1538    | 30555488           | 30555488      | 48287641| 48          | 385542364  | Colson Whitehead         | 2016                      | 4.04           | 72052         | 92096              | 11045                    | 1259      | 3885      | 16777     | 38456     | 31719     | https://images.gr-assets.com/books/1493178362m/30555488.jpg | https://images.gr-assets.com/books/1493178362s/30555488.jpg |

### Scatter Plot Description
A scatter plot visualizing the relationship between `work_ratings_count` and `ratings_count` reveals a nearly linear correlation, suggesting that as the number of ratings for a work increases, the total count of ratings also tends to increase significantly.

![Scatter Plot](scatter_plot.png)

## Interpretation
### Linear Regression Results
The linear regression analysis of `ratings_1` predicting `ratings_2` yielded the following results:
- **Intercept**: 1286.7040
- **Coefficient**: 1.3562
- **Mean Squared Error (MSE)**: 13431611.5081
- **R² Score**: 0.8577

This confirms a strong positive relationship, indicating that higher 1-star ratings correlate positively with 2-star ratings.

## Implications
The analysis suggests several actionable insights:
- **High correlation between ratings** indicates strong reader consensus—books with lower ratings tend to have fewer reader engagements, suggesting the need for further promotional strategies.
- **Outliers** may suggest a focus for marketing pushes or require examination to understand their popularity despite lower average ratings.
- The scatter plot can help identify trends for targeted marketing campaigns, focusing on books with high ratings counts to boost visibility.

## Key Findings
- Strong correlations exist across ratings metrics within the dataset.
- Outliers identified present unique cases worthy of further examination.
- A linear regression indicates potential forecasting capabilities for ratings.
- The dataset encourages further exploration into trends related to publication years and language preferences.

## Conclusion
In conclusion, this analysis of the Goodreads dataset underscores valuable patterns and insights into reader preferences and author popularity. Understanding the statistical relationships and outlier behavior provides opportunities for targeted marketing strategies and enhanced reader engagement. Collectively, these findings lay the groundwork for in-depth exploration into literary data analytics.