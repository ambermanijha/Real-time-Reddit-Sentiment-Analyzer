
# Social Media Sentiment Analysis

This project is a real-time social media sentiment analysis tool that leverages Reddit data and a fine-tuned DistilBERT model for sentiment classification. It uses the Reddit API (via PRAW) to stream posts from selected subreddits, applies a LoRA/PEFT adapter to a base DistilBERT model for inference, and displays the results in a Streamlit dashboard.



## Model Performance

The fine-tuned DistilBERT model (with LoRA/PEFT) was evaluated on a downstream sentiment analysis task with the following results:

- **Accuracy:** 90.00%
- **F1 Score:** 0.90
- **Precision:** 0.90
- **Recall:** 0.90

### Classification Report

|                  | Precision | Recall | F1-Score | Support |
|------------------|-----------|--------|----------|---------|
| **0.0**          | 0.86      | 0.95   | 0.90     | 383     |
| **1.0**          | 0.94      | 0.85   | 0.90     | 387     |
| **Accuracy**     |           |        | 0.90     | 770     |
| **Macro Avg**    | 0.90      | 0.90   | 0.90     | 770     |
| **Weighted Avg** | 0.90      | 0.90   | 0.90     | 770     |


## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/Social_Media_Sentiment_Analysis.git
   cd Social_Media_Sentiment_Analysis
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   *Ensure your `requirements.txt` includes packages such as:*
   - streamlit
   - pandas
   - torch
   - transformers
   - peft
   - praw

## Configuration

### Reddit API Credentials

Before running the scripts, update your Reddit API credentials in `reddit_stream.py`:

```python
CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
USER_AGENT = "myRedditApp/0.1 by u/YourRedditUsername"
```

### Model Adapter

Ensure that your LoRA/PEFT adapter checkpoint (e.g., `checkpoint-5000`) is located in the correct path as specified in `sentiment_analysis.py`:

```python
BASE_MODEL_NAME = "distilbert-base-uncased"
ADAPTER_PATH = ""  # Update this path if needed
```

## Running the Application

### 1. Start the Reddit Stream

Open a terminal and run:

```bash
python reddit_stream.py
```

This script will connect to Reddit, stream new posts from the configured subreddits (e.g., `news` and `worldnews`), process each post through the sentiment analysis model, and append the results to `reddit_posts.csv`.

### 2. Launch the Streamlit Dashboard

In another terminal, run:

```bash
streamlit run app.py
```

This will launch the dashboard in your browser, displaying the latest posts and their sentiment, along with a bar chart for sentiment distribution. You also have the option to input a post manually for testing.

## Troubleshooting

- **Model Loading Issues:**  
  If you encounter errors related to missing model checkpoint files (e.g., `pytorch_model.bin`), ensure that you have both the base model and the LoRA adapter. The code in `sentiment_analysis.py` first loads `distilbert-base-uncased` and then applies the adapter from your checkpoint.

- **DataFrame `append` Deprecation:**  
  The code uses `pd.concat()` instead of the deprecated `DataFrame.append()` method. Ensure your Pandas version is updated if you encounter any issues.

- **Reddit API Errors:**  
  Verify your Reddit credentials and user agent string are correctly configured.



## Acknowledgments

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [PEFT/LoRA](https://github.com/huggingface/peft)
- [PRAW (Python Reddit API Wrapper)](https://praw.readthedocs.io/)
- [Streamlit](https://streamlit.io/)
```

