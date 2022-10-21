import pandas as pd
import dvc.api as dvc
import io
import sys

class DataHandler:
    
    def __init__(self):
        pass
    
    def read_csv(self,path:str):
        try:
            return pd.read_csv(path)
        except:
            print("Error occured!")
            sys.exit(1)
    
    def write_csv(self,df:pd.DataFrame,path:str):
        try:
            df.to_csv(path)
            return True
        except:
            print("Error occured!")
            return False

    def read_from_dvc(self,path,repo,rev,low_memory=True):
       
        try:
            data = dvc.read(path=path,repo=repo, rev=rev)
            df = pd.read_csv(io.StringIO(data),low_memory=low_memory)
            return df
            
        except Exception as e:
            print("Something went wrong!",e)    
            sys.exit(1)

