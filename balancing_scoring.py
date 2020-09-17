## Scoring and labeling the tweets
# First calculate the overall polarity score
# Assume only positive and negative
# Classify via the number of neg/pos words and emoticons

# 'tweet is expected to be an integer iterable' 
def polarity_score(tweet):
  score = 0
  for feature in tweet:
    score += tweet[feature]
  return score

# 'pol_score' is expected to be a scalar
def determine_sentiment(pol_score):
  # Highly positive: +2 
  if pol_score >= 2 and pol_score <= 4:
    return 2 
  # Moderate positive: +1 
  elif pol_score > 0 and pol_score < 2:
    return 1
  # Moderate negative: -1 
  elif pol_score > -2 and pol_score < 0:
    return -1 
  # Highly negative: -2 
  elif pol_score >= -4 and pol_score <= -2:
    return -2
  else: return 0

## Testing the balancing and scoring
# Calculate the number of highly positive tweets
h_p = 0
for i in en_train_pos_tweets:
  score = polarity_score(i)
  sentiment = determine_sentiment(score)
  if sentiment == 2:
    ++h_p
print(f'Highly positive: {h_p}')
