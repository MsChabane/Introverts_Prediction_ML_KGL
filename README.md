# 🧠 Personality Prediction: Introverts vs. Extroverts

> Predict whether a person is an **Introvert (0)** or **Extrovert (1)** using machine learning with a fully reproducible **DVC** pipeline.

**Dataset (Kaggle Playground S5E7):**  
https://www.kaggle.com/competitions/playground-series-s5e7

---

## ✨ Highlights

- Reproducible end-to-end ML pipeline with **DVC**
- Clean separation of **Preprocess → Train → Evaluate**
- Centralized hyperparams in **`params.yaml`**
- Experiment tracking with **`dvc exp`**

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **pandas, numpy, scikit-learn**
- **xgboost / lightgbm** (optional)
- **matplotlib / seaborn** for visualization
- **DVC**, **Git**

---
## ⚡ Quickstart

### 1) Clone and enter
```bash
git clone https://github.com/MsChabane/Introverts_Prediction_ML_KGL.git
cd Introverts_Prediction_ML_KGL
```
### 2) Create env & install deps
```
python -m venv .venv
source venv/bin/activate   
venv\Scripts\activate
pip install -r requirements.txt
```

### 3) Initialize DVC and set remote (optional but recommended)
```
dvc init
```
### 5) Reproduce the pipeline
```
dvc repro
```

### 6) Show metrics / experiments
```
dvc metrics show
dvc exp show --no-pager
```

## 🎈 More
+ To run the server use the command : 

```bash 
python app.py 
```
+ To run the streamlit app use the command : 
```bash
streamlit run app.py 
```

