from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import joblib
from preprocess import Preprocess
import os


class Train:
    def __init__(self,X_train_encoded,X_test_encoded,y_train,y_test):
        self.X_train_encoded=X_train_encoded
        self.X_test_encoded=X_test_encoded
        self.y_train=y_train
        self.y_test=y_test

    def training(self):

        
        # 1. Parameter Grid define karein
        # Ye XGBoost ke sabse critical parameters hain overfitting rokne ke liye
        param_grid = {
            'n_estimators': [100, 200, 300],        # Kitne trees banenge
            'learning_rate': [0.01, 0.05, 0.1],     # Model kitni jaldi seekhega (Low is better but slower)
            'max_depth': [3, 5, 7],                 # Tree kitna gehra hoga (Default 6 hota hai, 3-5 best hai)
            'subsample': [0.8, 1.0],                # Har tree kitna % data dekhega (0.8 adds randomness)
            'colsample_bytree': [0.8, 1.0]          # Har tree kitne % columns dekhega
        }

        # 2. Base Model initialize karein
        xgb_base = XGBRegressor(random_state=42)

        # 3. GridSearchCV setup karein
        # cv=3 matlab 3-fold cross-validation, n_jobs=-1 matlab CPU ke saare cores use honge
        grid_search = GridSearchCV(
            estimator=xgb_base,
            param_grid=param_grid,
            scoring='r2',           # Humara main goal R2 maximize karna hai
            cv=3,
            n_jobs=-1,
            verbose=1               # Progress print karne ke liye
        )

        # 4. Grid Search ko data par Fit karein (Isme thoda time lag sakta hai)
        print("Starting Grid Search... this might take a few minutes.")
        grid_search.fit(self.X_train_encoded, self.y_train)

        # 5. Best Parameters aur Best Model extract karein
        print("\nBest Parameters Found:")
        print(grid_search.best_params_)

        self.best_xgb = grid_search.best_estimator_

        # 6. Test Data par Evaluate karein
        best_preds = self.best_xgb.predict(self.X_test_encoded)

        r2_tuned = r2_score(self.y_test, best_preds)
        rmse_tuned = np.sqrt(mean_squared_error(self.y_test, best_preds))

        print(f"\n--- Tuned XGBoost Results ---")
        print(f"R2 Score: {r2_tuned:.4f}")
        print(f"RMSE: {rmse_tuned:.4f}")

    def save_model(self,path="artifacts"):
        os.makedirs(path, exist_ok=True)
        joblib.dump(self.best_xgb,f"{path}/Xgb_model.pkl")
