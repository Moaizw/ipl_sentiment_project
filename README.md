# IPL Sentiment Project

Creating a system, which ranks youth indian players based on how often they're mentioned and how positively they're talked about on Reddit. 

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
