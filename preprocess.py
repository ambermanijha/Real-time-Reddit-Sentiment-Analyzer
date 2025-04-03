import re

def clean_text(text):
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+', '', text)     # Remove mentions
    text = re.sub(r'#\w+', '', text)      # Remove hashtags
    text = re.sub(r'[^A-Za-z0-9\s]+', '', text)  # Remove special characters
    text = text.strip()
    return text

# Example usage:
if __name__ == "__main__":
    sample = "Check out https://example.com @user #hashtag!"
    print(clean_text(sample))
