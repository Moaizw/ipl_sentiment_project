# ipl_sentiment_project

Creating a system, which ranks youth indian players based on how often they're mentioned and how positively they're talked about on Reddit. 

Pipeline:

1. Streaming Data from Reddit using PRAW -> reddit_comments_batch.csv & reddit_posts_posts.csv

2. Running Sentiment analysis on data extracted using Vader & RoBERTA. Results saved to sentiment_results.csv

3. NER performed (Fuzzy Matching). Used sentiment_results.csv & players_data.csv which is a table of cricket players scraped from cricket websites. This output is saved to sentiment_with_players_fuzzy.csv

4. Aggregate sentiment by players. Sentiment scored by (positive - negative / total mentions). Results saved to ranked_players.csv

5. Created dashboard via dashboard.py