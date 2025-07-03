# IPL Sentiment Project

Creating a system, which ranks youth cricket players based on how often they're mentioned and how positively they're talked about on Reddit. 

## Table of Contents

- [Overview](#overview)
- [Pipeline](#pipeline)
- [Data Files](#data-files)
- [Installation](#installation)
- [Usage](#usage)
- [Dashboard](#dashboard)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project involves streaming data (posts & comments) from the r/ipl subreddit. Once this data is collected, sentiment analysis is performed to analyse the sentiment behind each post. It then uses Fuzzy Matching to link sentiment mentions to a database of youth cricket players scraped from tournament websites. These sentiment scores are then aggregated for each player and are ranked accordingly. The results are then visualised via an interactive streamlit dashboard. 

## Pipeline

1. **Stream Data from Reddit** using [PRAW](https://praw.readthedocs.io/en/stable/).  
   - Outputs:
     - `reddit_comments_batch.csv`
     - `reddit_posts_batch.csv`

2. **Sentiment Analysis**  
   - Tools: VADER & RoBERTa  
   - Notebook: `Sentiment_analysis.ipynb`  
   - Output: `sentiment_results.csv`

3. **Fuzzy Matching**  
   - Inputs:
     - `sentiment_results.csv`
     - `player_data.csv`  
   - Notebook: `sentiment_with_players_fuzzy.ipynb`  
   - Output: `sentiment_with_players_fuzzy.csv`

4. **Aggregate Sentiment by Player**  
   - Score formula: `(positive_count – negative_count) / total_mentions`  
   - Notebook: `aggregate_sentiment.ipynb`  
   - Output: `ranked_players.csv`

5. **Dashboard**  
   - Script: `dashboard.py`  
   - Runs at `http://localhost:8050`

## Data Files

| File                             | Description                                    |
| -------------------------------- | ---------------------------------------------- |
| `reddit_comments_batch.csv`      | Raw Reddit comments from PRAW                  |
| `reddit_posts_batch.csv`         | Raw Reddit posts from PRAW                     |
| `player_data.csv`                | Scraped list of youth Indian cricket players   |
| `sentiment_results.csv`          | VADER & RoBERTa sentiment scores               |
| `sentiment_with_players_fuzzy.csv` | NER + fuzzy-matched mentions to players      |
| `ranked_players.csv`             | Final sentiment‐based player rankings          |


