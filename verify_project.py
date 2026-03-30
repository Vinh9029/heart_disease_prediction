#!/usr/bin/env python
"""
TESTING & VERIFICATION SCRIPT
==============================
Run this script to verify the entire project is set up correctly.
Usage: python verify_project.py
"""

import os
import sys
from pathlib import Path


class ProjectVerifier:
    """Verify Heart Disease Prediction project setup"""
    
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.errors = []
        self.warnings = []
        self.successes = []
    
    def check_files(self):
        """Check if all required files exist"""
        print("\n📂 Checking Files...")
        print("-" * 50)
        
        required_files = {
            "heart_disease_midterm_project.ipynb": "Jupyter notebook with ML pipeline",
            "gui_heart_disease_predictor.py": "Professional GUI application",
            "gui_simple_heart_disease_predictor.py": "Lightweight GUI (optional)",
            "requirements.txt": "Python dependencies",
            "README.md": "Documentation",
            "QUICK_START.txt": "Quick reference guide",
            "data/heart.csv": "Dataset",
        }
        
        for filepath, description in required_files.items():
            full_path = self.project_root / filepath
            if full_path.exists():
                self.successes.append(f"✅ {filepath} - {description}")
                print(f"✅ {filepath}")
            else:
                error_msg = f"❌ {filepath} - MISSING! {description}"
                self.errors.append(error_msg)
                print(error_msg)
    
    def check_python_version(self):
        """Check Python version"""
        print("\n🐍 Checking Python Version...")
        print("-" * 50)
        
        version = sys.version_info
        if version.major >= 3 and version.minor >= 7:
            msg = f"✅ Python {version.major}.{version.minor}.{version.micro}"
            self.successes.append(msg)
            print(msg)
        else:
            msg = f"❌ Python {version.major}.{version.minor} (need 3.7+)"
            self.errors.append(msg)
            print(msg)
    
    def check_dependencies(self):
        """Check if required packages can be imported"""
        print("\n📦 Checking Dependencies...")
        print("-" * 50)
        
        packages = {
            "pandas": "Data manipulation",
            "numpy": "Numerical computing",
            "matplotlib": "Visualization",
            "seaborn": "Advanced visualization",
            "sklearn": "Machine Learning (scikit-learn)",
            "joblib": "Model serialization",
            "xgboost": "XGBoost classifier",
            "mlxtend": "Pattern mining",
        }
        
        for package, description in packages.items():
            try:
                __import__(package)
                self.successes.append(f"✅ {package} - {description}")
                print(f"✅ {package}")
            except ImportError:
                self.warnings.append(f"⚠️ {package} - NOT INSTALLED: {description}")
                print(f"⚠️ {package} (optional for some features)")
    
    def check_model(self):
        """Check if trained model exists"""
        print("\n🤖 Checking Trained Model...")
        print("-" * 50)
        
        model_path = self.project_root / "heart_disease_best_model.joblib"
        if model_path.exists():
            size_mb = model_path.stat().st_size / (1024 * 1024)
            msg = f"✅ Model found ({size_mb:.2f} MB)"
            self.successes.append(msg)
            print(msg)
        else:
            self.warnings.append("⚠️ Model not found. Run notebook to train model.")
            print("⚠️ Model not found. Run notebook first to train and save model.")
    
    def check_dataset(self):
        """Check dataset statistics"""
        print("\n📊 Checking Dataset...")
        print("-" * 50)
        
        try:
            import pandas as pd
            data_path = self.project_root / "data" / "heart.csv"
            if not data_path.exists():
                self.errors.append("❌ Dataset not found at data/heart.csv")
                print("❌ Dataset not found")
                return
            
            df = pd.read_csv(data_path)
            msg = f"✅ Dataset loaded: {df.shape[0]} rows × {df.shape[1]} columns"
            self.successes.append(msg)
            print(msg)
            
            # Check for required columns
            expected_cols = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 
                           'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
            missing_cols = [c for c in expected_cols if c not in df.columns]
            if missing_cols:
                self.warnings.append(f"⚠️ Missing columns: {missing_cols}")
                print(f"⚠️ Warning: Missing columns: {missing_cols}")
            else:
                self.successes.append("✅ All 13 required features present")
                print("✅ All 13 required features present")
            
            # Check missing values
            missing_pct = (df.isnull().sum().sum()) / (df.shape[0] * df.shape[1]) * 100
            print(f"   Missing values: {missing_pct:.2f}%")
        
        except Exception as e:
            self.errors.append(f"❌ Error reading dataset: {str(e)}")
            print(f"❌ Error: {str(e)}")
    
    def print_summary(self):
        """Print summary report"""
        print("\n" + "="*50)
        print("VERIFICATION SUMMARY")
        print("="*50)
        
        print(f"\n✅ Successes: {len(self.successes)}")
        for item in self.successes[:5]:
            print(f"   {item}")
        if len(self.successes) > 5:
            print(f"   ... and {len(self.successes) - 5} more")
        
        if self.warnings:
            print(f"\n⚠️ Warnings: {len(self.warnings)}")
            for item in self.warnings:
                print(f"   {item}")
        
        if self.errors:
            print(f"\n❌ Errors: {len(self.errors)}")
            for item in self.errors:
                print(f"   {item}")
        
        print("\n" + "="*50)
        
        if not self.errors:
            print("✅ PROJECT READY! You can proceed with:")
            print("   1. jupyter notebook heart_disease_midterm_project.ipynb")
            print("   2. python gui_heart_disease_predictor.py")
        else:
            print("❌ SETUP INCOMPLETE - Fix errors above first")
            print("\nQuick fixes:")
            print("   pip install -r requirements.txt")
    
    def run(self):
        """Run all verifications"""
        print("\n" + "="*50)
        print("❤️  HEART DISEASE PREDICTION PROJECT")
        print("     VERIFICATION SCRIPT")
        print("="*50)
        
        self.check_python_version()
        self.check_files()
        self.check_dependencies()
        self.check_model()
        self.check_dataset()
        self.print_summary()
        
        return len(self.errors) == 0


def main():
    """Main entry point"""
    verifier = ProjectVerifier()
    success = verifier.run()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
