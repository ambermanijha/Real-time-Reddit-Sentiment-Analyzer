import streamlit as st
import pandas as pd
import time
from sentiment_analysis import predict_sentiment

# CSV file used to store Reddit posts and sentiment data
DATA_FILE = "reddit_posts.csv"

@st.cache_data
def load_data():
    try:
        return pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["post", "sentiment", "confidence"])

def update_data(new_post):
    df = load_data()
    sentiment, conf = predict_sentiment(new_post)
    label = "Positive" if sentiment == 1 else "Negative"
    new_row = {"post": new_post, "sentiment": label, "confidence": conf}
    # Convert the new_row dictionary to a DataFrame
    new_row_df = pd.DataFrame([new_row])
    # Use pd.concat to combine the existing DataFrame with the new row
    df = pd.concat([df, new_row_df], ignore_index=True)
    df.to_csv(DATA_FILE, index=False)
    return df


st.title("Real-time Reddit Sentiment Analyzer")
st.write("This dashboard shows Reddit posts and their predicted sentiment.")

# Option to input a post manually for testing
user_input = st.text_input("Enter a Reddit post title:")
if st.button("Analyze"):
    if user_input:
        df = update_data(user_input)  # Update and return new DataFrame
        st.success("Post processed!")
        st.subheader("Updated Posts with Sentiment")
        st.write(df.tail(10))  # Show last 10 posts
    else:
        st.warning("Please enter a post.")


# Display data
df = load_data()
if not df.empty:
    st.subheader("Latest Posts with Sentiment")
    st.write(df.tail(10))

    # Refresh every 60 seconds
    st.write("Auto-refreshing every 60 seconds...")
    time.sleep(60)
    st.experimental_rerun()


# Visualize sentiment distribution
if not df.empty:
    sentiment_counts = df["sentiment"].value_counts()
    st.subheader("Sentiment Distribution")
    st.bar_chart(sentiment_counts)

# Auto-refresh for real-time updates
st.write("Auto-refresh every 60 seconds for new data.")
time.sleep(60)
st.experimental_rerun()
