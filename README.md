# Analyzing Public Sentiment on Twitter During Mali's 2021 Coup d’État

This repository contains the LaTeX source for our conference paper analyzing French-language Twitter data around Mali’s May 2021 coup. We combine sentiment analysis, topic modeling, stance classification, and network clustering to understand how online discourse evolved in response to key political events.

---
## Authors
Azza Osman, Carnegie Mellon University Africa

Oswaldo Camille Grimaud, Carnegie Mellon University Africa

Leonard Twagirayezu, Carnegie Mellon University Africa

## Supervisor
Emily Aiken, Carnegie Mellon University Africa

## Abstract
Social media platforms --- particularly Twitter --- have become vital tools for analyzing political discourse and understanding how public opinion evolves in response to key events. While numerous studies have leveraged Twitter to investigate political and social dynamics in the Global North, the online political dynamics of the African context --- especially Francophone West Africa --- are  underexplored. This study focuses on the Twitter discourse surrounding the May 2021 coup d’état in Mali. We show that Twitter users respond to coup-related events with changes in Tweet frequency and sentiment, and find that most users in the Malian Twittersphere demonstrate an on-average neutral to positive stance towards the coup. We find little evidence of polarization between pro-junta and anti-junta camps on Twitter.   Our findings contribute to the growing body of research on political communication in underrepresented regions and highlight the potential of social media for real-time sociopolitical analysis.

## Data and Methodology
### Data
The dataset used in this study was sourced from Schroeder et al. (2023), who identified 56,000 Twitter accounts likely belonging to Malian users by analyzing metadata, self-declared locations, language preferences, and network connections. From these accounts, they collected over 10 million tweets spanning January 2009 to June 2022. For our analysis, we focused exclusively on French-language tweets, which represent 69% of the original dataset.

To narrow the scope to content relevant to Mali’s May 2021 coup d’état, we applied keyword filtering using terms and hashtags associated with the event, including references to key figures, descriptive terms, and commonly used tags (e.g., “Assimi Goïta,” “coup d’État,” “#MaliCoup”). We further limited the timeframe to tweets posted between May 2021 and June 2022. After filtering, our final dataset consisted of 29,059 tweets.

### Sentiment and Stance Classification
We employed two models for tweet classification:

Sentiment Analysis: Using the distilcamembert-base-sentiment model (a fine-tuned variant of CamemBERT), we assigned each tweet a sentiment score on a 5-point scale, from very negative to very positive.

Stance Classification: To classify political orientation, we used the Mistral French language model via Ollama. Tweets were categorized as “pro-junta,” “anti-junta,” or “neutral” based on contextual prompts and examples.

Both models were evaluated on a manually labeled sample of 500 tweets. The sentiment classifier achieved 84% accuracy, while the stance classifier reached 63%, with most errors involving misclassification of neutral tweets.
### Network Analysis
To analyze interaction dynamics, we constructed a follower network among users who posted at least ten coup-related tweets during the study period. After excluding users with no followers in this subgraph, we retained 393 users. Each user was assigned average sentiment and stance scores based on their tweets. Standard social network analysis techniques were applied to examine structural patterns and detect clusters of politically aligned users, using metrics such as degree centrality, clustering coefficients, and modularity.

## Results
### Dataset Overview
Our final dataset includes 29,059 French-language tweets from 3,393 users, posted between May 2021 and June 2022. These tweets were filtered using a curated list of keywords related to Mali’s 2021 coup. Notably, 73% of the tweets originate from outside Mali, highlighting the significant influence of diaspora and international communities in shaping the online discourse.

### Reaction to Political Events
Tweet volume and sentiment closely tracked key political events. Significant spikes in activity occurred around:

* May 24, 2021 (the coup itself)

* ECOWAS sanctions

* The French troop withdrawal in 2022

Sentiment scores peaked positively following the coup, but dipped during periods of international tension or security crises (e.g., the ECOWAS sanctions and arrival of the Wagner group), suggesting a responsive and emotionally dynamic online discourse.

### Sentiment and Stance Analysis
Sentiment: 75% of tweets were neutral to positive.

Stance: 62% of tweets were classified as pro-junta. At the user level (among those with followers), 67% were pro-junta, 25% neutral, and only 8% anti-junta.
These findings indicate that the Malian Twittersphere was largely supportive or tolerant of the military-led transition during this period.

### Network Dynamics
To examine online polarization, we analyzed the follower relationships among 393 active users. The results showed:

* Low polarization: Users followed accounts across political lines, with only slight preference toward like-minded users.

* Dense interaction: The follower network exhibited no clear echo chambers or segregated communities by stance.

These results suggest that while pro-junta sentiment dominated, the online conversation remained relatively interconnected, lacking the extreme polarization observed in other geopolitical contexts.

## How to run
1. Download the dataset from https://osf.io/mj2qt/
2. Set up a Python environment and install dependencies (requirements.txt provided)
3. Run the scripts to preprocess data, conduct sentiment analysis, and visualize results.


## Refrences
T. Schroeder, M. de Bruijn, L. Bruls, M. A. Moges, S. D. Badji, N. Fritz, M. G. Cisse,
J. Langguth, B. Mutsvairo, and K. S. Orgeret. Social media in the global south: a network
dataset of the malian twittersphere. Journal of Data Mining & Digital Humanities, 2023,
2023
## 

