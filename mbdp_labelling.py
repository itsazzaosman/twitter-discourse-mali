import pandas as pd
from tqdm import tqdm 
from langchain_community.llms import Ollama

llm = Ollama(model="llama3.2")

# Load tweets from CSV
df = pd.read_csv('tweets_to_label.csv')  # assume column 'text'

# Define function to classify a tweet
def classify_tweet(tweet):
    prompt = f"""
You are a political analyst specializing in military affairs.
Classify the following tweet into exactly one category:
- Anti-junta
- Pro-junta
- Neutral

Tweet: "{tweet}"

Respond ONLY with the label: Anti-junta, Pro-junta, or Neutral.
"""
    try:
        label = llm.invoke(prompt).strip()
        return label
    except Exception as e:
        print(f"Error classifying tweet: {e}")
        return "Error"
tqdm.pandas()

# Apply to all tweets
df_sampled = df.head(10)
df_sampled['label_stance'] = df_sampled['cleaned_text'].progress_apply(classify_tweet)

# Save output
df_sampled.to_csv('tweets_labeled_with_ollama.csv', index=False)
print("Tweets classified and saved to 'tweets_labeled_with_ollama.csv'")
