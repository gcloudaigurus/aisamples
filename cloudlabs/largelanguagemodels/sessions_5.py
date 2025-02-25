
# Import necessary libraries.  You'll need to install them if you don't have them already: pip install transformers sentence-transformers
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from sentence_transformers import SentenceTransformer, util

# Initialize question answering pipeline.  This uses a pre-trained model for question answering.
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Initialize summarization pipeline. This uses a pre-trained model for text summarization.  
#  Different models offer different strengths (length, style). Experiment to find what works best for your needs.
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Sample context (replace with your own text)
context = """
The Battle of Hastings was a pivotal battle fought on 14 October 1066, near Hastings, East Sussex, England.  It marked the Norman conquest of England. The Norman-French army, led by William, the Duke of Normandy, decisively defeated the English army under King Harold Godwinson.  The battle resulted in Harold's death and William's subsequent coronation as King of England. The battle was a significant turning point in English history, drastically altering the language, culture, and social structure of the country.
"""

# Sample question
question = "Who won the Battle of Hastings?"

# Perform question answering
result_qa = qa_pipeline(question=question, context=context)

# Print the answer
print(f"Question: {question}\nAnswer: {result_qa['answer']}\n")


# Sample long text for summarization (replace with your own text)
long_text = """
The quick brown rabbit jumps over the lazy frogs.  The frogs are green and slimy and enjoy sitting in the mud. The rabbit is fluffy and white and enjoys carrots.  One day, the rabbit was feeling mischievous and decided to play a trick on the frogs.  He hopped into the mud, startling the frogs. They all jumped away in surprise. The rabbit laughed and hopped away, leaving the surprised frogs in the mud.  The sun was shining brightly, and the day was warm and pleasant.  The end.
"""

# Perform summarization
result_summary = summarizer(long_text, max_length=130, min_length=30, do_sample=False)

# Print the summary
print(f"Original Text:\n{long_text}\n")
print(f"Summary:\n{result_summary[0]['summary_text']}\n")


#Example of semantic similarity using Sentence Transformers (useful for comparing text, finding similar questions etc)

# Load a Sentence Transformer model
model = SentenceTransformer('all-mpnet-base-v2')

# Sentences to encode and compare
sentences = ["This is an example sentence", "Each sentence is converted"]

#Encode sentences to get their embeddings
embeddings = model.encode(sentences, convert_to_tensor=True)

#Compute cosine-similarities for each sentence with each other sentence
cosine_scores = util.cos_sim(embeddings, embeddings)

#Output the similarity matrix
print("Similarity Matrix:")
print(cosine_scores)

#You can use the cosine_scores to find sentences that are semantically similar.  A score closer to 1 indicates higher similarity.


