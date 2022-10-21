import pandas as pd
import re

class DataCleaner:
    
    def __init__(self):
        pass

    def get_uniqueness(self,df:pd.DataFrame):
        """
        Accepts pandas.DataFrame
        
        Returns:
            a pandas DataFrame: (the input dataframe) with their respective unique value percentages

        """
        percentage = round(df.nunique()*100/df.shape[0],2)
        percentage_df=pd.DataFrame(percentage,columns=["Unique %"])
        return percentage_df
    
    def convert_to_date(self,df:pd.DataFrame,columns:list):
        """
        convert the values in each columns to datetime
        """
        for column in columns:
            df[column] = pd.to_datetime(df[column])
        return df
    
    def calculate_duration(self,df:pd.DataFrame,start_col_name,end_col_name):
        """
        calculate the time difference between two columns and append a new column (duration) to the dataframe
        """
        df["duration"]= (df[end_col_name] - df[start_col_name]).astype('timedelta64[m]')
        return df

    def fill_missing(self,df: pd.DataFrame, method: str,columns: list) -> pd.DataFrame:
        """
        fill missing values with specified method "mean" or "median"
        """
        if method == "mean":
            for col in columns:
                df[col].fillna(df[col].mean(), inplace=True)

        elif method == "median":
            for col in columns:
                df[col].fillna(df[col].median(), inplace=True)
        else:
            print("Method unknown")
        
        return df

    def fill_start_time(self,df:pd.DataFrame,start_col:str,end_col:str,duration_col):
        """
        fill null/na start time values by subtracting duration from the end time
        """
        fill_values=  df.apply(lambda x:x[end_col] - pd.Timedelta(minutes=x[duration_col]),axis=1)
        # return fill_values
        df[start_col].fillna(fill_values,inplace=True)
        return df 

    def fill_end_time(self,df:pd.DataFrame,start_col:str,end_col:str,duration_col):
        """
        fill null/na end time values by adding duration to the start time
        """
        fill_values=  df.apply(lambda x:x[start_col] + pd.Timedelta(minutes=x[duration_col]),axis=1)
        # return fill_values
        df[end_col].fillna(fill_values,inplace=True)
        return df 
    def remove_space(self,df:pd.DataFrame):
        columns = df.columns
        for col in columns:
            no_space=re.sub(' +', '_', col.lower().strip())
            df.rename(columns={col:no_space},inplace=True)
        return df