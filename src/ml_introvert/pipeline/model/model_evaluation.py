
from ml_introvert.constant import (MODELS_DIR,MODEL_FILENAME,PROCESSED_DATA_DIR,
                                   TEST_FILENAME
                                   ,CONFUSION_MATRIX_FILENAME,ROC_FILENAME,
                                   REPORTS_DIR,METRICS_FILENAME)
from ml_introvert.utils.common import reading_data
import joblib
import os 
import json
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.metrics import (
    accuracy_score,precision_score,recall_score,f1_score,precision_recall_curve,confusion_matrix,ConfusionMatrixDisplay,roc_auc_score,roc_curve
)



if __name__=='__main__':
    df =reading_data(path_dir=PROCESSED_DATA_DIR,filename=TEST_FILENAME)
    model=joblib.load(os.path.join(MODELS_DIR,MODEL_FILENAME))
    X=df[df.columns[:-1]]
    y=df[df.columns[-1]]
    prediction = model.predict(X)
    probabilty= model.predict_proba(X)
    eval ={metric.__name__ :metric(y,prediction) for metric in [accuracy_score,precision_score,f1_score,recall_score]}
    fpr, tpr, thresholds = roc_curve(y, probabilty[:,1])
    
    fig=plt.figure(figsize=(8,6))
    plt.plot(fpr, tpr, marker='.', label="ROC Curve")
    plt.plot([0, 1], [0, 1], linestyle="--", color="gray", label="Random Guess")  
    plt.xlabel("False Positive Rate (FPR)")
    plt.ylabel("True Positive Rate (TPR)")
    plt.title("Receiver Operating Characteristic (ROC) Curve")
    plt.legend()
    plt.grid()
    fig.savefig(os.path.join(REPORTS_DIR,ROC_FILENAME))
    fig,ax=plt.subplots()
    ConfusionMatrixDisplay(confusion_matrix(y,prediction),display_labels=['EXTROVERT','INTROVERT'])\
        .plot(ax=ax,colorbar=False,cmap='magma')
    plt.tight_layout()
    plt.title('Confusion Matrix')
    fig.savefig(os.path.join(REPORTS_DIR,CONFUSION_MATRIX_FILENAME))
    with open(os.path.join(REPORTS_DIR,METRICS_FILENAME),'w') as f:
        json.dump(eval,f,indent=4)





    



