import pandas as pd
import re
import sys
import numpy as np
from datetime import datetime,timedelta,date
from geopy.geocoders import Nominatim
from geopy import distance
import holidays

class DataCleaner:
    
    def __init__(self):
        self.geolocator = Nominatim(user_agent="gokada")
        self.nigeria_holiday= holidays.Nigeria()
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
    
    def calculate_duration(self,df:pd.DataFrame,start_col_name,end_col_name,duration_col_name:str="duration_min"):
        """
        calculate the time difference between two columns and append a new column (duration) to the dataframe
        """
        df[duration_col_name]= (df[end_col_name] - df[start_col_name]).astype('timedelta64[m]')
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
        
        df[start_col].fillna(fill_values,inplace=True)
        return df 

    def fill_end_time(self,df:pd.DataFrame,start_col:str,end_col:str,duration_col):
        """
        fill null/na end time values by adding duration to the start time
        """
        fill_values=  df.apply(lambda x:x[start_col] + pd.Timedelta(minutes=x[duration_col]),axis=1)
        
        df[end_col].fillna(fill_values,inplace=True)
        return df 
    def remove_space(self,df:pd.DataFrame):
        columns = df.columns
        for col in columns:
            no_space=re.sub(' +', '_', col.lower().strip())
            df.rename(columns={col:no_space},inplace=True)
        return df
    def reverse_location(self,df:pd.DataFrame,lat_col_name:str="latitude",lng_col_name:str="longitude",loc_col_name:str="location"):
        locator = self.geolocator
        df[loc_col_name] = df.apply(lambda x:str(locator.reverse(str(x[lat_col_name])+","+str(x[lng_col_name]))),axis=1)
        df[loc_col_name] = df[loc_col_name].apply(lambda x:self.spliter(x))
        return df

    def spliter(self,text:str,ind:int=-4):
        try:
            text=text.split(',')[ind]
            return text 
        except Exception:
            if ind > 1:
                print("Error occured")
                sys.exit(1)
            else:
                ind+=1
                return self.spliter(text,ind)

    def find_distance(self,df:pd.DataFrame,distance_col_name:str="distance",trip_origin_col_names:list=["trip_origin"],trip_destination_col_names:list=["trip_destination"]):
        if len(trip_destination_col_names) > 1 and len(trip_origin_col_names) > 1:
            df[distance_col_name]=df.apply(lambda x:distance.distance((x[trip_origin_col_names[0]],x[trip_origin_col_names[1]]), (x[trip_destination_col_names[0]],x[trip_destination_col_names[1]])).km,axis=1)
        else:
            df[distance_col_name]=df.apply(lambda x:distance.distance((x[trip_origin_col_names[0]]), (x[trip_destination_col_names[0]])).km,axis=1)
        return df

    def check_holiday(self,order_time:datetime):
        return order_time.date() in self.nigeria_holiday

    def add_holiday_feature(self,df:pd.DataFrame,date_col:str="trip_start_time"):
        df["holiday"]=df[date_col].apply(lambda x:self.check_holiday(x))
        return df


