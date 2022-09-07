
import pandas as pd

import Log
from DataUtils import fill_using_mode

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
        data['WeekOfYear'] = pd.DatetimeIndex(data['Date']).weekofyear
        
        
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

    def create_isPromo2(self, data: pd.DataFrame) -> pd.DataFrame:

        a = data.copy()
        one = [1,4,7,10]
        two = [2,5,8,11]
        three = [3,6,9,12]

        val = []
        for i in range(a.shape[0]):
            if(a.loc[i, 'PromoInterval'] == 0):
                val.append(0)
            elif(a.loc[i, 'PromoInterval'] == 1 and (a.loc[i, 'Month'] in one) and a.loc[i, 'Year'] >= a.loc[i, 'Promo2SinceYear'] and a.loc[i, 'WeekOfYear'] >= a.loc[i, 'Promo2SinceWeek']):
                val.append(1)
            elif(a.loc[i, 'PromoInterval'] == 2 and (a.loc[i, 'Month'] in two) and a.loc[i, 'Year'] >= a.loc[i, 'Promo2SinceYear'] and a.loc[i, 'WeekOfYear'] >= a.loc[i, 'Promo2SinceWeek']):
                val.append(1)
            elif(a.loc[i, 'PromoInterval'] == 3 and (a.loc[i, 'Month'] in three) and a.loc[i, 'Year'] >= a.loc[i, 'Promo2SinceYear'] and a.loc[i, 'WeekOfYear'] >= a.loc[i, 'Promo2SinceWeek']):
                val.append(1)
            else:
                val.append(0)

        
        data['isPromo2'] = val
        Log.i("mapping data character to integers and ranges to integers")
        
        return data
        
    def drop_unwanted_columns(self, data: pd.DataFrame) -> pd.DataFrame:

        data.drop(columns=['Unnamed: 0'], inplace=True)
        
        return data
        

    def pipeline(self, df: pd.DataFrame) -> pd.DataFrame:
        '''
        this function run the data through the pipline
    
        args:
            df: DataFrame - the data frame to processed
            
        return:
            returns the cleaned dataframe
        '''
         
        
        df = self.drop_unwanted_columns(df)
        df = self.map_data(df)
        df = self.add_help_columns(df)
        df = self.convert_to_int(df)
        # df = self.create_isPromo2(df)
        df = fill_using_mode(df, ['Open'])
        
        
        Log.i("Data pipeline finished running")
        
        return df
        
    