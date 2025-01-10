import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
from datasets import load_metric

nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import string


def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word not in stop_words and word not in string.punctuation]
    return " ".join(filtered_words)


def textrank_summarizer(document, top_n=3):
    with open(document, 'r') as f:
        file_contents = f.read()

    sentences = sent_tokenize(file_contents)
    preprocessed_sentences = [preprocess_text(sentence) for sentence in sentences]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(preprocessed_sentences)
    similarity_matrix = cosine_similarity(tfidf_matrix)
    graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(graph)
    ranked_sentences = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    summary = " ".join([ranked_sentences[i][1] for i in range(min(top_n, len(ranked_sentences)))])
    return summary


def evaluate_summary(generated_summary, reference_summary):
    rouge = load_metric("rouge")
    scores = rouge.compute(predictions=[generated_summary], references=[reference_summary])
    return scores


if __name__ == "__main__":
    document = 'summary.txt'
    reference_summary = "reference_summary.txt"
    generated_summary = textrank_summarizer(document, top_n=2)
    print("Generated Summary:")
    print(generated_summary)
    rouge_scores = evaluate_summary(generated_summary, reference_summary)
    print("\nROUGE Scores:")
    print(rouge_scores)
