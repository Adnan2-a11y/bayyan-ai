To upgrade Bayyan AI for better Arabic and English understanding, you should switch to a multilingual model. The all-MiniLM-L6-v2 you are using is mostly optimized for English.
Here are the direct code replacements for the best free alternatives:
## 1. The Pro Choice: paraphrase-multilingual-MiniLM-L12-v2
This is the multilingual "big brother" of your current model. It is small, fast, and understands both Arabic and English.

model_name = "paraphrase-multilingual-MiniLM-L12-v2"emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)

## 2. The Accuracy Choice: multilingual-e5-small
This is one of the highest-rated models for search tasks. It is excellent at matching an English query to the deep meaning of an Arabic verse.

model_name = "intfloat/multilingual-e5-small"emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)

## 3. The "State of the Art" Choice: bge-m3
If your Linux machine has at least 4GB of RAM, this is the best open-source model available for Arabic.

model_name = "BAAI/bge-m3"emb_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=model_name)

## ⚠️ Important Note on Changing Models:
Vector databases are model-dependent. If you change the model_name in your code, you must:

   1. Delete your old vector folder: rm -rf ./quran_vectordb
   2. Rerun your preprocess.py: This creates new vectors that match the new model's math.

Which one would you like to try? I recommend starting with paraphrase-multilingual-MiniLM-L12-v2 for the best balance of speed and accuracy.

#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
from groq import Groq
import os
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
models = client.models.list()
for model in models.data:
    print(model.id)
