📊 KAIM - Predicting Price Moves with News Sentiment

📌 Overview

This project is designed for scalable Python-based Sentiment analysis and Correlation Analysis, combining data cleaning, exploratory data analysis (EDA), and reproducible workflows.

It includes:

Structured source code (src/) Interactive analysis via notebooks (notebooks/) Automated testing (tests/) Utility scripts (scripts/) CI/CD integration via GitHub Actions

The goal is to to conduct a rigorous, two-fold analysis of the provided financial news dataset that leverage the relationship between news sentiment and stock price fluctuations to predict future market movements.

🗂️ Project Structure :
news-sentiment-analysis/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── data/
│   └── raw/
├── notebooks/
│   ├── __init__.py
│   └── README.md
├── src/
│   └── __init__.py
├── tests/
│   └── __init__.py
└── scripts/
    ├── __init__.py
    └── README.md


⚙️ Setup Instructions

Create and activate a virtual environment python -m venv .venv Windows .venv\Scripts\activate Linux / macOS source .venv/bin/activate
Install dependencies pip install -r requirements.txt
📊 Exploratory Data Analysis (EDA) 🔹 How to Run Start Jupyter Notebook: jupyter notebook Navigate to: notebooks/ Open the EDA notebook (e.g., analysis.ipynb) and run all cells. 🔹 Analysis Workflow


📁 Outputs

Generated outputs are organized as follows:

📌 Cleaned Data data/_clean.csv

⚠️ The data/ directory is excluded from version control via .gitignore.

📊 Visualizations

Stored (optionally) in:

reports/figures/ 📝 Reports

Analysis summaries can be stored in(not currently available):

reports/ 🧪 Running Tests

Run unit tests with:

pytest

Tests are automatically executed in CI via:

.github/workflows/unittests.yml

🤖 Automation Scripts

Scripts in scripts/ can be used for:

Data preprocessing Batch execution of analysis Pipeline automation

Run a script:

python scripts/<script_name>.py
