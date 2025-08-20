from pathlib import Path

DATA_FILENAME='data.csv'
CLEANED_DATA_FILENAME='cleaned_data.csv'
TRAIN_FILENAME='train_data.csv'
TEST_FILENAME='test_data.csv'


RAW_DATA_DIR=Path('data/raw')
CLEANED_DATA_DIR = Path('data/cleaned')
PROCESSED_DATA_DIR=Path('data/processed')

MODELS_DIR=Path("models")
ENCODER_FILENAME='encoder.pkl'
SCALER_FILENAME='scaler.pkl'
MODEL_FILENAME='model.pkl'

REPORTS_DIR=Path('reports')
FEATURE_IMPORTANCE_FILENAME='Features_Importance.png'
CONFUSION_MATRIX_FILENAME='cm.png'
ROC_FILENAME='roc.png'
METRICS_FILENAME='metrics.json'


