from pprint import pprint
import dvc.api

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_squared_error, r2_score

import mlflow
import mlflow.sklearn
from sklearn.pipeline import Pipeline
import pandas as pd
import os, sys

import io 

path_parent = os.path.dirname(os.getcwd())
os.chdir(path_parent)
sys.path.insert(0, path_parent+'/scripts')


path="data/train_data.csv"
repo="C:/Users/user/Desktop/TenAcademy/Sales-Prediction-For-Pharmaceutical/"
version="v4-train"

path2="data/test_data.csv"
repo2="C:/Users/user/Desktop/TenAcademy/Sales-Prediction-For-Pharmaceutical/"
version2="v4-train"

train_data = dvc.api.read(
    path=path,
    repo=repo,
    rev=version,
)

test_data = dvc.api.read(
    path=path2,
    repo=repo2,
    rev=version2,
)

mlflow.set_experiment('forecast_randomforest')

# def eval_metrics(actual, pred):
#     rmse = np.sqrt(mean_squared_error(actual, pred))
#     mae = mean_absolute_error(actual, pred)
#     r2 = r2_score(actual, pred)
    
#     return rmse, mae, r2

def main():
    # prepare example dataset
    train_ = pd.read_csv(io.StringIO(train_data), sep=",")
    
    inputs_test = pd.read_csv(io.StringIO(test_data), sep=",")
    print(train_.columns)
    
    # rf_pipeline = Pipeline(steps=[
    #     ('impute', ),
    #     ('scale', MinMaxScaler())
    # ])
    
    #log data params
    mlflow.log_param('train_data_version', version)
    mlflow.log_param('input_rows', train_.shape[0])
    mlflow.log_param('input_colums', train_.shape[1])
    
    mlflow.log_param('test_data_version', version2)
    mlflow.log_param('test_input_rows', inputs_test.shape[0])
    mlflow.log_param('test_input_colums', inputs_test.shape[1])
    
    train_.drop(columns=['Unnamed: 0'], inplace=True)
    inputs_test.drop(columns=['Unnamed: 0'], inplace=True)
    
    inputs = train_.drop(['Sales'], axis=1)
    targets = train_[['Sales']]
    
    lr = RandomForestRegressor()
    
    lr.fit(inputs, targets)
    
    # score = lr.score(X_test, y_test)
    
    # print("Score: %s" % score)
    # mlflow.log_metric("score", score)
    mlflow.sklearn.log_model(lr, "model")
    print("Model saved in run %s" % mlflow.active_run().info.run_uuid)


if __name__ == "__main__":
    main()