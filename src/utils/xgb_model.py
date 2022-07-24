import pandas as pd
import pickle
import xgboost


class XgbModel:
    """ Class to represent trained XGBoost xgb_model that predicts data on our board """

    def __init__(self):
        self.input_path = 'assets/data/test.csv'
        self.df = pd.read_csv(self.input_path)
        self.model = pickle.load(open('assets/xgb_model/xgboost_model.pkl', 'rb'))
        self.X_test = None
        self.y_test = None
        self.parse_input()
        self.predict_data()

    def parse_input(self):
        self.y_test = self.df['to_water']
        self.df = self.df.sample(frac=1)  # shuffle dataframe so as to randomize tiles
        self.df = self.df.drop('to_water', axis=1)
        self.X_test = pd.get_dummies(self.df)

    def predict_data(self):
        prediction = self.model.predict(self.X_test)
        # print(self.y_test[self.y_test != prediction])
        self.df['to_water'] = prediction

