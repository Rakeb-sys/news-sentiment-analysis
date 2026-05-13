# Predicting Price Moves with News Sentiment

This directory contains the Exploratory Data Analysis (EDA) and data cleaning pipeline for mews and stock market datasets for various companies suchas Apple, Amazon, Meta, Google and NVIDIA. The goal is to form the basis of investment strategies that leverage news sentiment as a predictive tool for stock market trends. 

- **Target Period:** 2010 – 2024
- **Goal:** leverage insights from this sentiment analysis to suggest investment strategies.

## 🛠️ Data Cleaning Pipeline
To ensure scientific accuracy, the following steps are performed in the `data_cleaner.py`:

1. **Null Handling:** Removal of Null values.
4. **date Conversion:** convert it to datetime format.

## 📊 Key Visualizations & Analysis
The analysis focuses on three core areas:
- **Charts:** most active publishers and characterize their coverage and how indicators relate to price action.
- **Correlations:** Heatmaps and scatter plots (e.g., T2M vs. RH2M) to understand the relationship between stock data and news sentiment.

## 📁 Repository Structure
- `notebooks/<company_Ticker_code>_eda.ipynb`: Individual Company analysis notebooks.
- `notebooks/news_sentiment_stock_price_eda/news_<company_Ticker-code>.ipynb`: Individual Company stock market data correlated analysis with news sentiment notebooks.
- `data/<company_Ticker_code>_clean.csv`: Cleaned output files (Note: Excluded from version control via `.gitignore`).

## 📚 References & Resources
Stock Market 
- https://www.investopedia.com/terms/s/stockmarket.asp
- https://www.investopedia.com/terms/s/stock-analysis.asp

Python Testing
- https://machinelearningmastery.com/a-gentle-introduction-to-unit-testing-in-python/
- https://docs.python-guide.org/writing/tests/
- https://realpython.com/python-testing/
- 
Python Packages:
- https://textblob.readthedocs.io/en/dev/
- https://github.com/mqandil/pynance
- https://github.com/ta-lib/ta-lib-python


Data Engineering
- What is Data Engineer: Role Description, Skills, and Background | AltexSoft
