import pandas as pd
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from sklearn.model_selection import train_test_split
import category_encoders as ce
import json
import joblib
import os

class Preprocess:
    def __init__(self,filename,json_name):
        self.file_name=filename
        self.json_name=json_name

        self.oe_education = OrdinalEncoder(categories=[['High School', 'Undergraduate', 'Graduate']])
        self.oe_stress = OrdinalEncoder(categories=[['Low', 'Medium', 'High', 'Very High']])
        self.le_gender = LabelEncoder()
        self.target_encoder = ce.TargetEncoder(cols=['Most_Used_Platform', 'Purpose_Of_Use'])

    def load_data(self):
        
        #Loading data
        self.data=pd.read_csv(self.file_name)

        # Aapki list ke according HDI based classification file loading
        with open(self.json_name,'r')as f:
            map_data=json.load(f)

        #Encoding Country names in Tiers
        self.data['country_tier']=self.data['Country'].map(map_data)
        self.data['country_tier']=self.data['country_tier'].fillna(2)
        self.data = self.data.drop("Country", axis=1)

        # Ordinal encoding Academic_Level and Stress_Level
        self.data[['encode_Academic_Level']]=self.oe_education.fit_transform(self.data[['Academic_Level']])
        self.data[['encode_Stress_Level']]=self.oe_stress.fit_transform(self.data[['Stress_Level']])
        self.data=self.data.drop(['Academic_Level','Stress_Level'],axis=1)

        #label Encoding Gender
        self.data['Gender']=self.le_gender.fit_transform(self.data['Gender'])
       
    def splitting(self):

        #separating X and y
        X = self.data.drop('Mental_Health_Score', axis=1)
        y = self.data['Mental_Health_Score']

        #splitting trhe dataset
        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=42)

        # 4. FIT & TRANSFORM on Training Data (Model y_train se patterns seekhega)
        X_train_encoded = self.target_encoder.fit_transform(X_train, y_train)

        # 5. ONLY TRANSFORM on Testing Data (Leakage rokne ke liye)
        X_test_encoded = self.target_encoder.transform(X_test)

        return X_train_encoded,X_test_encoded,y_train,y_test

    def save_encoders(self,save_dir="artifacts"):
        os.makedirs(save_dir, exist_ok=True)
        joblib.dump(self.target_encoder, f'{save_dir}/target_encoder.pkl')
        joblib.dump(self.oe_education, f'{save_dir}/oe_education.pkl')
        joblib.dump(self.oe_stress, f'{save_dir}/oe_stress.pkl')
        joblib.dump(self.le_gender, f'{save_dir}/le_gender.pkl')




