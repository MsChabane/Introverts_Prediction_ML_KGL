
from ml_introvert.constant import PROCESSED_DATA_DIR,TRAIN_FILENAME,REPORTS_DIR,FEATURE_IMPORTANCE_FILENAME,MODELS_DIR,MODEL_FILENAME
from ml_introvert.utils.common import reading_data,save_bin,read_params
import os 
import pandas as pd 
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt 

if __name__ =='__main__':
    params= read_params(key='training')
    df = reading_data(PROCESSED_DATA_DIR,TRAIN_FILENAME)
    X=df[df.columns[:-1]]
    y=df[df.columns[-1]]
    rfc=RandomForestClassifier(random_state=42,n_estimators=params['estimators'],bootstrap=params['bootstrap'],
                               criterion=params['criterion'],
                               )
    rfc.fit(X,y)
    featres_impor = pd.DataFrame(data=rfc.feature_importances_,index=X.columns,columns=['values']).sort_values(by='values',ascending=False)
    figure=plt.figure(figsize=(10,8))
    plt.barh(width=featres_impor['values'],y=featres_impor.index)
    plt.title(FEATURE_IMPORTANCE_FILENAME)
    plt.tight_layout()
    figure.savefig(os.path.join(REPORTS_DIR,FEATURE_IMPORTANCE_FILENAME))
    save_bin(MODELS_DIR,MODEL_FILENAME,data=rfc)


