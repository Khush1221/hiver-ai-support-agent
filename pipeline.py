import pandas as pd

print("Loading dataset...")
df = pd.read_csv('AppleSupport_tweets.csv', low_memory=False)

print("Running evaluation harness on golden set...")
golden_df = pd.read_csv('golden_evaluation_set.csv')


def mock_ai_agent(tweet):
  tweet_lower = str(tweet).lower()
  if 'refund' in tweet_lower or 'charge' in tweet_lower:
    return {'intent': 'Billing', 'should_escalate': True}
  else:
    return {'intent': 'Technical / General', 'should_escalate': False}


results = []
for idx, row in golden_df.iterrows():
  pred = mock_ai_agent(row['tweet_text'])
  results.append(pred)

print(f'Pipeline executed successfully! Total evaluated: {len(results)}')
