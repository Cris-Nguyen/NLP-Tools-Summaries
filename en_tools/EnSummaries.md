## Vietnamese Tools for NLP Tasks

### 1. Programming Language support
- NLTK: Python
- spaCy: Python(GPU support)
- StanfordCoreNLP: Java(included Python wrapper), not very efficient because of large model(~650MB)

### 2. Performance 
| Tasks                     | NLTK               | spaCy          |
| -------------             | -------------      | ------------       |
| Word segmentation         | 6482 sentence / 1s | 114 sentences / 1s |
| POS-Tagging               | 150 sentence / 1s  | 106 sentences / 1s |
| Dependency parsing        |                    | 113 sentences / 1s  |
| Named-Entity Recognition  | 122 sentences / 1s | 114 sentences / 1s |
| Machine Translation       |                    |                    |
| Text classification       |                    |                    |
| Sentiment Analysis        |                    |                    |