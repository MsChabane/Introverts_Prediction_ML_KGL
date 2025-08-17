# 🧠 Personality Prediction: Introverts vs. Extroverts

> Predict whether a person is an **Introvert (0)** or **Extrovert (1)** using machine learning with a fully reproducible **DVC** pipeline.

## **Dataset (Kaggle Playground S5E7):**  
https://www.kaggle.com/competitions/playground-series-s5e7



### Quick Summary Table

| Feature                     | Type         | Description                                          |
|-----------------------------|--------------|------------------------------------------------------|
| `id`                        | Integer      | Unique identifier for each record                    |
| `Time_spent_Alone`          | Numerical    | Hours spent alone                                    |
| `Stage_fear`                | Categorical  | Fear of performing on stage (Yes/No)                 |
| `Social_event_attendance`   | Numerical    | Frequency of attending social events                 |
| `Going_outside`             | Numerical    | Frequency of going outside                           |
| `Drained_after_socializing` | Categorical  | Feeling drained post-socializing (Yes/No)            |
| `Friends_circle_size`       | Numerical    | Size of social circle                                |
| `Post_frequency`            | Numerical    | Social media post frequency                          |
| `Personality`               | Categorical  | Target variable: Introvert or Extrovert              |

### Features Description

#### 1. `id`
- **Type**: Integer  
- **Description**: Unique identifier for each record.  

#### 2. `Time_spent_Alone`
- **Type**: Numerical  
- **Description**: Number of hours a person spends alone.  

#### 3. `Stage_fear`
- **Type**: Categorical (Yes/No)  
- **Description**: Indicates fear of performing on stage.  

#### 4. `Social_event_attendance`
- **Type**: Numerical  
- **Description**: Frequency of attending social events.  

#### 5. `Going_outside`
- **Type**: Numerical  
- **Description**: How often a person goes outside (per day/week).  

#### 6. `Drained_after_socializing`
- **Type**: Categorical (Yes/No)  
- **Description**: Whether the person feels drained after socializing.  

#### 7. `Friends_circle_size`
- **Type**: Numerical  
- **Description**: Size of the person’s friend group.  

#### 8. `Post_frequency`
- **Type**: Numerical  
- **Description**: Frequency of posting on social media platforms.  

#### 9. `Personality` (Target)
- **Type**: Categorical  
- **Description**: Target variable with two classes:  
  - `Introvert`  
  - `Extrovert`  

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

