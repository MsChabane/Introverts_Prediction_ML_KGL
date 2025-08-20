import pandas as pd 
import os 
import joblib

def save_dataframe(df:pd.DataFrame,path:str):
    """
    save the dataframe into csv format .
    """
    df.to_csv(path,index=False)


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

def reading_data(path_dir:str,filename:str):
    """
    read a csv file as a dataframe
    """
    return pd.read_csv(os.path.join(path_dir,filename))

def save_bin(path_dir:str,filename:str,data:any):
    """
    save binary object into pkl file
    """
    print(joblib.dump(data,os.path.join(path_dir,filename)))