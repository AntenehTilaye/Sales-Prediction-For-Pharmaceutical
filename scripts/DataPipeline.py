
import pandas as pd

import Log

class DataPipeline:
    
    def convert_to_int(self, data: pd.DataFrame) -> pd.DataFrame:
        
        data['StoreType'] = data['StoreType'].astype(int)
        data['Assortment'] = data['Assortment'].astype(int)
        data['StateHoliday'] = data['StateHoliday'].astype(int)
        data['PromoInterval'] = data['PromoInterval'].astype(int)
        
        
        Log.i("convert columns to integer")
        return data
    
    
    def add_help_columns(self, data: pd.DataFrame) -> pd.DataFrame:
    
        data['Year'] = pd.DatetimeIndex(data['Date']).year
        data['Month'] = pd.DatetimeIndex(data['Date']).month
        data['Day'] = pd.DatetimeIndex(data['Date']).day    
        data['QuadYear'] = pd.DatetimeIndex(data['Date']).quarter
        data['DayOfYear'] = pd.DatetimeIndex(data['Date']).day_of_year
        
        
        Log.i("Adding more columns to the DataFrame, year, month etc")
        return data

    def map_data(self, data: pd.DataFrame) -> pd.DataFrame:

        mappings = {'0':0, 'a':1, 'b':2, 'c':3, 'd':4}
        mappings2 = {'0':0, 'Jan,Apr,Jul,Oct':1, 'Feb,May,Aug,Nov':2, 'Mar,Jun,Sept,Dec':3}
        
        data.StoreType.replace(mappings, inplace=True)
        data.Assortment.replace(mappings, inplace=True)
        data.StateHoliday.replace(mappings, inplace=True)
        data.PromoInterval.replace(mappings2, inplace=True)
        
        
        Log.i("mapping data character to integers and ranges to integers")
        
        return data
        
        

    def pipeline(self, df: pd.DataFrame) -> pd.DataFrame:
        '''
        this function run the data through the pipline
    
        args:
            df: DataFrame - the data frame to processed
            
        return:
            returns the cleaned dataframe
        '''
         
        
        df = self.map_data(df)
        df = self.add_help_columns(df)
        df = self.convert_to_int(df)
        
        
        Log.i("Data pipeline finished running")
        
        return df
        
    