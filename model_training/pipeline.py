from data_processor import Preprocess
from model_trainer import Train


def run_pipeline():
    print("Starting Machine Learning Pipeline...")

    # --- 1. PREPROCESSING STAGE ---
    print("\n[1/4] Initializing Preprocessor and Loading Data...")
    # Dhyan rakhein ki dataset aur JSON config ka correct path dein
    processor = Preprocess(filename=r'data\data.csv', json_name=r'config\country_tiers.json')
    
    processor.load_data()
    print("Data loaded and categorical columns mapped/encoded.")

    # --- 2. DATA SPLITTING & TARGET ENCODING ---
    print("\n[2/4] Splitting Data and applying Target Encoding...")
    X_train_enc, X_test_enc, y_train, y_test = processor.splitting()
    
    # Preprocessor me banaya gaya save_encoders() method call karein
    processor.save_encoders(save_dir="artifacts")
    print("Data split completed and Preprocessing Encoders saved.")

    # --- 3. MODEL TRAINING & HYPERPARAMETER TUNING ---
    print("\n[3/4] Initializing Model Training and Grid Search...")
    trainer = Train(X_train_enc, X_test_enc, y_train, y_test)
    
    # Aapka training method call ho raha hai (GridSearchCV run hoga)
    trainer.training()
    print("Model training and evaluation completed.")

    # --- 4. SAVING THE MODEL ---
    print("\n[4/4] Saving the optimized model...")
    trainer.save_model(path="artifacts")
    print("Pipeline Finished Successfully! All artifacts are ready for FastAPI deployment.")

if __name__ == "__main__":
    run_pipeline()


