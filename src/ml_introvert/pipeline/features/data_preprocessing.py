import pandas as pd 
from imblearn.over_sampling import RandomOverSampler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder
from ml_introvert.constant import (TRAIN_FILENAME,TEST_FILENAME,PROCESSED_DATA_DIR,ENCODER_FILENAME,MODELS_DIR,SCALER_FILENAME
                                   ,CLEANED_DATA_DIR,CLEANED_DATA_FILENAME)
from ml_introvert.utils.common import reading_data,save_dataframe,save_bin
import os 



if __name__=='__main__':
    df =reading_data(path_dir=CLEANED_DATA_DIR,filename=CLEANED_DATA_FILENAME)
    X = df[df.columns[:-1]]
    y=df.Personality
    Xresample,yresample = RandomOverSampler().fit_resample(X,y)
    
    cat_features=Xresample.select_dtypes(include=['object','category']).columns.to_list()
    cat_data=pd.get_dummies(Xresample[cat_features]).astype('int')
    Xresample.drop(columns=cat_features,inplace=True)
    Xresample[cat_data.columns]=cat_data.values
    Xresample['Personality']=yresample.values
    train_data,test_data = train_test_split(Xresample,test_size=0.3,random_state=42)
    scaler = StandardScaler().fit(Xresample[Xresample.columns[:-1]])
    train_data[train_data.columns[:-1]]=scaler.transform(train_data[train_data.columns[:-1]])
    test_data[test_data.columns[:-1]]=scaler.transform(test_data[test_data.columns[:-1]])
    encoder=LabelEncoder()
    train_data[train_data.columns[-1]]=encoder.fit_transform(train_data[train_data.columns[-1]])
    test_data[test_data.columns[-1]]=encoder.transform(test_data[test_data.columns[-1]])
    save_bin(path_dir=MODELS_DIR,filename=SCALER_FILENAME,data=scaler)
    save_bin(path_dir=MODELS_DIR,filename=ENCODER_FILENAME,data=encoder)
    save_dataframe(df=train_data,path=os.path.join(PROCESSED_DATA_DIR,TRAIN_FILENAME))
    save_dataframe(df=test_data,path=os.path.join(PROCESSED_DATA_DIR,TEST_FILENAME))
    
    










