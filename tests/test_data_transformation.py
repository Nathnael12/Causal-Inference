import unittest
import pandas as pd
import sys
import os
from datetime import datetime
cwd = os.getcwd()
sys.path.append(f'{cwd}/scripts')
from data_cleaner import DataCleaner 
cleaner = DataCleaner()
class TestCleaner(unittest.TestCase):
    
    def test_remove_col_space(self):
        test_df=pd.DataFrame(columns=["col one","col_two"])
        test_df_cols=list(test_df.columns.values)
        new_cols=list(cleaner.remove_space(test_df).columns.values)
        self.assertFalse(test_df_cols == new_cols)
    
    def test_remove_col_space(self):
        test_df=pd.DataFrame(columns=["col one","col_two"])
        no_space_cols=["col_one","col_two"]
        new_cols=list(cleaner.remove_space(test_df).columns.values)
        self.assertEqual(no_space_cols , new_cols)
    
    def test_reverse_location(self):
        location = (8.987664535755162, 38.789648739472355)
        test_df=pd.DataFrame(data=[[8.987664535755162, 38.789648739472355]],columns=["latitude","longitude"])
        self.assertEqual(cleaner.reverse_location(test_df).location.values[0].strip(),"አዲስ አበባ / Addis Ababa")
    
    def test_holiday(self):
        # new year
        day = datetime(2022,1,1) 
        
        self.assertTrue(cleaner.check_holiday(day))

if __name__ == "__main__":
    unittest.main()
