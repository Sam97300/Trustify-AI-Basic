import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load static facts
with open("data/facts.json", "r", encoding="utf-8") as f:
    FACTS = json.load(f)

def verify_text(user_text):
    user_vector = model.encode([user_text])

    best_score = 0
    best_fact = None

    for fact in FACTS:
        fact_vector = model.encode([fact["headline"]])
        score = cosine_similarity(user_vector, fact_vector)[0][0]

        if score > best_score:
            best_score = score
            best_fact = fact

    confidence = round(best_score * 100, 2)

    if best_score >= 0.70:
        verdict = best_fact["verdict"]
        source = best_fact["source"]
    else:
        verdict = "Unverified"
        source = "No matching verified fact found"

    return {
        "verdict": verdict,
        "confidence": confidence,
        "source": source
    }

