from google import genai
import numpy as np

documents = [
    "Python is a high-level programming language used for web development, data science, and AI.",
    "Machine Learning is a subset of AI where computers learn from data without being explicitly programmed.",
    "Deep Learning uses neural networks with many layers to learn complex patterns from data.",
    "Streamlit is an open-source Python framework used to build and deploy web apps for ML projects.",
    "Natural Language Processing (NLP) is a branch of AI that deals with understanding human language.",
    "A black hole is a region in space where gravity is so strong that nothing, not even light, can escape.",
    "Data Science involves collecting, cleaning, analyzing, and visualizing large amounts of data.",
    "Neural networks are computing systems inspired by the biological neural networks in human brains.",
    "The Milky Way is a barred spiral galaxy that contains our Solar System.",
]

def get_embedding(client, text):
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )
    return result.embeddings[0].values

def cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def get_relevant_context(client, user_question, top_k=2):
    question_embedding = get_embedding(client, user_question)

    similarities = []
    for doc in documents:
        doc_embedding = get_embedding(client, doc)
        score = cosine_similarity(question_embedding, doc_embedding)
        similarities.append((score, doc))

    similarities.sort(reverse=True)
    top_docs = [doc for _, doc in similarities[:top_k]]

    return "\n".join(top_docs)