# Movie-Recommendation-System
🎬 A content-based movie recommendation system built with Python &amp; Streamlit — pick a movie, get 5 similar suggestions instantly using cosine similarity.

---

## 🛠️ Tools & Technologies

**Python** was used as the core programming language for building the recommendation logic. **Streamlit** powers the interactive web interface, allowing users to select a movie and receive instant suggestions. Movie data is stored and loaded via **Pickle**, while the precomputed similarity matrix is handled using **Joblib** for efficient serialization. The recommendation engine is built on **cosine similarity** from **Scikit-learn**, computing content-based similarity scores across the entire movie dataset.

---

## 📊 How It Works

1. User selects a movie from the dropdown
2. The app fetches the movie's index from the dataset
3. Cosine similarity scores are computed against all other movies
4. Top 5 most similar movies are returned and displayed

---

## 📁 Project Structure

```
Movie-Recommendation-System/
│
├── app.py                  # Main Streamlit application
├── movies.pickle           # Preprocessed movie dataset
├── similarity.joblib       # Precomputed cosine similarity matrix
├── requirements.txt        # Project dependencies
└── README.md
```

> **Note:** `similarity.joblib` exceeds GitHub's 25MB file limit and is managed via **Git LFS**. If LFS is unavailable, regenerate it locally by running the preprocessing script.

---

## ⚙️ Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/kaurmanmeet-ctrl/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

---

## 📦 Requirements

```
streamlit
pandas
scikit-learn
joblib
```

---

## 🧠 Skills Demonstrated

- Content-based filtering using cosine similarity
- Data serialization with Pickle and Joblib
- Building and deploying interactive ML apps with Streamlit
- End-to-end ML project structure and deployment readiness

---

