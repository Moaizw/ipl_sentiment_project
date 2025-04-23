import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="IPL Player Sentiment Dashboard", layout="wide")

# Title
st.title("🏏 IPL Player Sentiment Leaderboard")
st.caption("Ranking youth cricket players based on how often they're mentioned and how positively they're talked about on Reddit")

# Load and cache the data
@st.cache_data
def load_data():
    return pd.read_csv("ranked_players.csv")

df = load_data()

# Sidebar: Filters
with st.sidebar:
    st.header("🔍 Filter Options")

    # Competition name search
    comp_search = st.text_input("Search Competition Name").lower()

    # Optional team search
    team_search = st.text_input("Search Team Name").lower()

    min_mentions = st.slider("Minimum Mentions", 1, int(df['total_mentions'].max()), 5)
    sort_option = st.selectbox("Sort Players By", ['sentiment_score', 'total_mentions'])

# Apply filters
filtered = df.copy()

if comp_search:
    filtered = filtered[filtered['Competition'].str.lower().str.contains(comp_search, na=False)]

if team_search:
    filtered = filtered[filtered['Team'].str.lower().str.contains(team_search, na=False)]

filtered = filtered[filtered['total_mentions'] >= min_mentions]

filtered = filtered.sort_values(by=sort_option, ascending=False).reset_index(drop=True)

# Main: Leaderboard Table
st.subheader("🏆 Sentiment-Based Player Rankings")
st.dataframe(
    filtered.rename(columns={"mentioned_players": "Player"})[[
        "Player", "Team", "Competition", "total_mentions", "sentiment_score"
    ]],
    use_container_width=True,
    height=500
)

# Main: Bar Chart
st.subheader(f"📊 Top 10 Players by {sort_option.replace('_', ' ').title()}")
top_10 = filtered.set_index("mentioned_players")[sort_option].head(10)
st.bar_chart(top_10)
