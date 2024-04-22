import os
import math
from collections import defaultdict
import pickle
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Function to read HTML content from files in a directory
def read_html_files(directory):
    documents = []
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            with open(os.path.join(directory, filename), "r", encoding="utf-8") as f:
                title = filename.split(".")[0]  # Extract title from filename
                content = f.read()  # Read content from file
                documents.append((title, content))  # Append tuple of title and content
    return documents

# Function to preprocess text
def preprocess(text):
    tokens = word_tokenize(text.lower())  # Tokenization and lowercase
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]  # Remove stopwords and non-alphanumeric characters
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]  # Stemming
    return tokens

def merge_blocks(block_files):
    """Merges inverted blocks from disk into a single inverted index."""
    inverted_index = defaultdict(list)
    for block_file in block_files:
        with open(block_file, "rb") as f:
            block = pickle.load(f)
            for token, postings in block.items():
                inverted_index[token].extend(postings)

    return inverted_index

# Step 4: Create a function to process documents in batches and build the inverted index
def process_batch_and_invert(documents, batch_size, output_dir):
    """Processes documents in batches, creates inverted blocks, and merges them."""
    inverted_index = defaultdict(list)
    doc_id = 0
    doc_freq = defaultdict(int)

    os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists

    for i in range(0, len(documents), batch_size):
        batch = documents[i:i+batch_size]
        for doc_title, doc_content in batch:
            tokenized_doc = preprocess(doc_content)
            doc_freq_for_doc = {}

            for term in tokenized_doc:
                doc_freq_for_doc[term] = doc_freq_for_doc.get(term, 0) + 1

            for term, freq in doc_freq_for_doc.items():
                tf = freq / len(tokenized_doc)
                doc_freq[term] += 1

                # Calculate TF-IDF score
                tf_idf_score = tf * math.log(len(documents) / doc_freq[term])
                inverted_index[term].append((doc_id, doc_title, tf_idf_score))

            doc_id += 1

        block_file = f"{output_dir}/block_{i}.pkl"
        with open(block_file, "wb") as f:
            pickle.dump(inverted_index, f)

        inverted_index = defaultdict(list)  # Reset for the next batch

    # Merge blocks into a single inverted index
    block_files = [f"{output_dir}/block_{i}.pkl" for i in range(0, len(documents), batch_size)]
    merged_index = merge_blocks(block_files)

    # Combine TF-IDF scores with inverted index
    for term, title, scores in inverted_index.items():
        for doc_id, score in scores:
            merged_index[term].append((doc_id, title, score))

    return merged_index


# Define batch size and output directory (adjust as needed)
batch_size = 1000
output_dir = "C:/index/"
index_directory = "C:/index/"

# Read HTML content from directory
website_content_directory = "C:/website_content"
documents = read_html_files(website_content_directory)

# Create the inverted index using block-based processing
inverted_index = process_batch_and_invert(documents, batch_size, output_dir)

# Move the inverted index file to the index directory
# Store the inverted index in the output directory
os.makedirs(output_dir, exist_ok=True)
index_file = os.path.join(output_dir, "inverted_index.pkl")
with open(index_file, "wb") as f:
    pickle.dump(inverted_index, f)

