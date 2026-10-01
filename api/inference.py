import json
import joblib
import pandas as pd

class Inference:
    def __init__(self):
        self.load_models()

    def load_models(self):
        self.le_gender=joblib.load('artifacts/le_gender.pkl')
        self.oe_education=joblib.load('artifacts/oe_education.pkl')
        self.oe_stress=joblib.load('artifacts/oe_stress.pkl')
        self.target_encoder=joblib.load('artifacts/target_encoder.pkl')
        self.Xgb_model=joblib.load('artifacts/Xgb_model.pkl')

        with open('config/country_tiers.json','r')as f:
            self.mapping_data=json.load(f)
    def encode_data(self,input_data):
        
        dict_data=input_data.model_dump()
        df_data=pd.DataFrame([dict_data])

        df_data['country_tier']=df_data['Country'].map(self.mapping_data)

        df_data[['encode_Academic_Level']]=self.oe_education.transform(df_data[['Academic_Level']])
        df_data[['encode_Stress_Level']]=self.oe_stress.transform(df_data[['Stress_Level']])

        df_data['Gender']=self.le_gender.transform(df_data['Gender'])

        df_data=df_data.drop(['Country','Academic_Level','Stress_Level'],axis=1)

        df_data= self.target_encoder.transform(df_data)

        return df_data

    def run_model(self,encoded_data):

        input_data=encoded_data
        output_prediction=self.Xgb_model.predict(input_data)
        return round(float(output_prediction[0]),2)
