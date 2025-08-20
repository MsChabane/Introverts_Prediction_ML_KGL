from ml_introvert.constant import RAW_DATA_DIR,DATA_FILENAME,CLEANED_DATA_DIR,CLEANED_DATA_FILENAME

from ml_introvert.utils.common import reading_data,save_dataframe,fill_missnig_data
import pandas as pd 
import os 



if __name__ =='__main__':
    df = reading_data(path_dir=RAW_DATA_DIR,filename=DATA_FILENAME)
    if "id" in df.columns:
        df.drop(columns=['id'],inplace=True)

    df =fill_missnig_data(df)
    print(df.isna().sum())
    save_dataframe(df=df,path=os.path.join(CLEANED_DATA_DIR,CLEANED_DATA_FILENAME))









