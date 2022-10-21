import pandas as pd

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
    
    def calculate_duration(df:pd.DataFrame,start_col_name,end_col_name):
        """
        calculate the time difference between two columns and append a new column (duration) to the dataframe
        """
        df["duration"]= (df[end_col_name] - df[start_col_name]).astype('timedelta64[m]')
        return df