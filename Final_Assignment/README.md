# PULPNET - IIT Kanpur VOX Populi Chatbot

A transformer-based chatbot that answers questions about IIT Kanpur using information scraped from Vox Populi IIT Kanpur website.

## Features

- Answers queries related to IIT Kanpur using scraped Vox Populi articles.
- Uses a QA model built with transformer architecture.
- Simple, interactive web interface built with Streamlit.

## Files Included

- `app1.py` — Main application file containing the chatbot and QA pipeline.
- `iitk_vox_articles_fin.txt` — Scraped article content from Vox Populi.
- `scraper.ipynb` — Jupyter notebook containing the web scraping code.
- `demo.mp4` — Demonstration video of the chatbot in action.

## Installation and Setup

### Prerequisites

- Python 3.x
- pip package manager
- Anaconda (recommended) or virtual environment

### Steps to Run

1. Download the `app1.py` and `iitk_vox_articles_fin.txt` files into the same folder.
2. Open **Anaconda Prompt** (or command prompt if using a virtual environment).
3. Navigate to the folder containing your files.
3. Run the streamlit app by typing `streamlit run app1.py` in the prompt window.

A browser window will automatically open within a few seconds where you can type your queries and interact with the chatbot.