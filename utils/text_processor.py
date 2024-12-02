# For text processing (e.g., tokenization, cleaning)
# Cleans and tokenizes text into a list of keywords.
import re

def preprocess_text(text):
    text = text.lower()
    
    # Remove special characters
    text = re.sub(r"[^\w\s]", "", text)
    words = text.split()
    
    # Remove stop words
    stop_words = {"and", "the", "is", "in", "to", "of", "a"}
    keywords = [word for word in words if word not in stop_words]
    
    return keywords
