# Trustify-AI-Basic 🛡️

A **minimal, beginner-friendly prototype** for verifying textual claims against a **static fact dataset**.  
This project is designed as the **foundation** for a larger AI-assisted misinformation detection system.

> ⚠️ This is a **basic / educational version** — no live news APIs, no ML models, no embeddings yet.

---

## ✨ What This Project Does

- Takes a **textual claim** as input  
- Compares it against a **predefined set of factual statements**
- Determines whether the claim is:
  - ✅ **Supported**
  - ❌ **Contradicted**
  - ⚠️ **Unknown / Not found**
- Displays results through a **simple Flask web interface**

---

## 🧱 Why This Version Exists

This project follows a **block-by-block development philosophy**:

1. Start with **static data**
2. Implement **deterministic logic**
3. Understand the full pipeline
4. Then scale to:
   - semantic similarity
   - embeddings
   - APIs
   - real-world news verification

This makes the system:
- easier to debug
- easier to explain
- easier to extend later

---

## 🗂️ Project Structure

```
trustify-basic/
│
├── app.py                  # Flask entry point
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
│
├── data/
│   └── facts.json          # Static factual dataset
│
├── services/
│   └── text_verifier.py    # Core verification logic
│
├── templates/
│   ├── index.html          # Input form UI
│   └── result.html         # Result display UI
│
└── env/                    # Virtual environment (ignored)
```

---

## 🧠 How Verification Works (Current Logic)

1. User submits a claim
2. Claim text is normalized
3. It is compared against known facts in `facts.json`
4. A verdict is returned based on:
   - exact or near-exact textual match
   - known truth values in the dataset

> No AI, ML, or embeddings are used **in this version**.

---

## 🚀 Getting Started

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Sam97300/Trustify-AI-Basic.git
cd Trustify-AI-Basic
```

### 2️⃣ Create & activate a virtual environment
```bash
python -m venv env
env\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the app
```bash
python app.py
```

Open your browser at:
```
http://127.0.0.1:5000
```

---

## 🛣️ Planned Future Enhancements

- 🔍 Semantic similarity (TF-IDF / embeddings)
- 🧠 ML-based claim verification
- 🌐 Live news and search APIs
- 🗃️ Database-backed fact storage
- 📊 Confidence scoring
- 🧪 Better test coverage

---

## 🎓 Educational Use Case

This project is ideal for:
- academic mini-projects
- system design demonstrations
- understanding verification pipelines
- gradual AI system evolution

---

## ⚖️ Disclaimer

This tool **does not guarantee factual correctness**.  
It only verifies claims **against its internal dataset**.

Do **not** rely on it for real-world decision making.

---

## 👤 Author

**Sam**  
Computer Engineering Student  
Exploring AI, verification systems, and scalable architectures.

---

## 📜 License

This project is open for **educational and non-commercial use**.


