import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize

nltk.download("punkt")

class QASystem:
    def __init__(self, content):
        """Initialize with extracted text content."""
        self.text = content
        self.sentences = sent_tokenize(content)  # Sentence tokenization
        self.vectorizer = TfidfVectorizer(stop_words="english")  # TF-IDF vectorizer

        # Fit the vectorizer with sentences
        self.sentence_vectors = self.vectorizer.fit_transform(self.sentences)

    def answer_question(self, question):
        """Finds the most relevant sentence from the text."""
        if not self.sentences:
            return "No content available to answer."

        # Transform question into TF-IDF vector
        question_vector = self.vectorizer.transform([question])

        # Compute similarity between question and text sentences
        similarities = cosine_similarity(question_vector, self.sentence_vectors).flatten()
        best_match_index = similarities.argmax()

        return self.sentences[best_match_index] if similarities[best_match_index] > 0 else "No relevant answer found."
