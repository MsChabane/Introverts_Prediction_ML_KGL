from ml_introvert.constant import RAW_DATA_DIR,DATA_FILENAME,PROCESSED_DATA_DIR
from ml_introvert import logger
import pandas as pd 
import os 


def reading_data(path_dir:str,filename:str):
    """
    read a csv file as a dataframe
    """
    return pd.read_csv(os.path.join(path_dir,filename))

def fill_missnig_data(df:pd.DataFrame):
    """
    fill the messing by the mode and median for the categorical and numerical features
    """
    num_feat= df.select_dtypes(include=['int','float']).columns.to_list()
    cat_feat= df.select_dtypes(include=['object','category']).columns.to_list()
    for col in cat_feat:
        df[col]=df[col].fillna(df[col].mode()[0])
    for col in num_feat:
        df[col]=df[col].fillna(df[col].median()) 
    return df

def save_dataframe(df:pd.DataFrame,path:str):
    """
    save the dataframe into csv format .
    """
    df.to_csv(path,index=False)

if __name__ =='__main__':

    df = reading_data(path_dir=RAW_DATA_DIR,filename=DATA_FILENAME)
    if "id" in df.columns:
        df.drop(columns=['id'],inplace=True)

    df =fill_missnig_data(df)
    print(df.isna().sum())
    save_dataframe(df=df,path=os.path.join(PROCESSED_DATA_DIR,'processed_data.csv'))









