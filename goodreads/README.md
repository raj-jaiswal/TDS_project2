# Analysis of Goodreads Book Data

## Overview
This document presents a detailed analysis of a dataset containing information on various books available on Goodreads. The dataset includes key attributes such as book IDs, authors, publication years, language, ratings, and reviews. By examining this data, we can gain insights into the reading preferences and trends among users on the Goodreads platform.

## Data Structure
The dataset consists of the following columns:

- **book_id**: Unique identifier for the book.
- **goodreads_book_id**: Goodreads-specific book ID.
- **best_book_id**: Indicates the best book in its category.
- **work_id**: Unique identifier for the work.
- **books_count**: Number of editions of the book available.
- **isbn**: International Standard Book Number (ISBN).
- **isbn13**: ISBN-13 representation.
- **authors**: Author(s) of the book.
- **original_publication_year**: The year the book was originally published.
- **original_title**: The original title of the book.
- **title**: Title of the book as listed on Goodreads.
- **language_code**: Language code for the book's primary language.
- **average_rating**: Average rating of the book.
- **ratings_count**: Total number of ratings received.
- **work_ratings_count**: Total ratings for the work.
- **work_text_reviews_count**: Count of text reviews provided by readers.
- **ratings_1 to ratings_5**: Count of ratings from 1 to 5 stars.
- **image_url**: URL for the book's cover image.
- **small_image_url**: URL for a smaller version of the book's cover image.

## Statistical Analysis
The dataset comprises **10,000** entries with the following statistical insights:

- **Average Rating**: The average rating of books is approximately **4.00** with a standard deviation of around **0.25**, indicating that most books get ratings between **2.47** and **4.82**.
- **Ratings Count**: On average, each book has received about **54,001** ratings, with a maximum of **4,780,653** ratings for a single book.
- **Publication Year**: The original publication year ranged from **-1750** (which likely indicates an error) to **2017**, with a mean publication year of **1982**.
- **Work Text Reviews Count**: The dataset shows an average of **2,920** text reviews per work, with a range up to **155,254**.

## Correlation Analysis
A correlation matrix reveals interesting relationships among attributes, notably:

- **Ratings Count and Work Ratings Count**: A strong positive correlation (**0.995**) suggests that as the number of ratings increases, the work's total rating count also increases significantly.
- **Ratings Count and Average Rating**: Moderate correlation exists, where higher ratings count leads to higher average ratings.

Here's a brief interpretation of some key pairs:
- Ratings distribution tends to be positively skewed, indicating that most books receive a higher number of positive ratings.
- The correlation among individual rating counts and total ratings points to consistent user feedback patterns across books.

## Outliers
Outliers detected using z-score methods include:

- **Harry Potter and the Cursed Child**: Average rating of **3.75** with **270,603** ratings, indicating it is well-rated but not as enthusiastically received as its predecessors.
- Some titles like **The Woman in Cabin 10** and **Small Great Things** that also lie on the edge of the distribution, hinting at fluctuating reader preferences.

## Interpretation
The analysis shows that user engagement is robust, with significant data points suggesting a strong enthusiasm for well-regarded titles. The positive correlations indicate that high ratings not only attract more ratings but also reinforce the book's standing in the Goodreads community.

### Key Findings
- Most books cluster around a favorable rating range (4.0-5.0), reflecting a generally positive reader experience.
- Outliers are notable and display varying levels of acceptance, showing that while some bestselling books are overwhelmingly popular, others receive mixed reviews.
- The high counts of ratings and reviews suggest engaged readership, reflecting a vibrant community of reviewers and raters.

## Conclusion
The analysis of Goodreads data provides a snapshot of user preferences and engagement levels within the reading community. The overall positive ratings, combined with high engagement metrics, suggest that readers are actively reviewing and discussing books, offering valuable insights for authors, publishers, and marketers. Engaging with the community around these ratings could enhance the visibility of books and enrich reader experiences.

![Scatter Plot](scatter_plot.png)
*The scatter plot above illustrates the relationship between ratings_count and work_ratings_count, showcasing the strong linear correlation found in the data.*