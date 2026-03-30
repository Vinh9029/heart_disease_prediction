"""
Heart Disease Prediction GUI Application
=========================================
A professional GUI tool for predicting heart disease risk using a trained ML model.

Usage:
    python gui_heart_disease_predictor.py
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pandas as pd
import numpy as np
import joblib
import os
from pathlib import Path


class HeartDiseasePredictor:
    """GUI Application for Heart Disease Prediction"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("❤️ Heart Disease Risk Predictor")
        self.root.geometry("1000x750")
        self.root.resizable(True, True)
        
        # Style configuration
        self.root.configure(bg="#f0f0f0")
        style = ttk.Style()
        style.theme_use('clam')
        
        # Model loading
        self.model = None
        self.model_loaded = False
        self.load_model()
        
        # Create GUI
        self.create_widgets()
        
    def load_model(self):
        """Load the trained model"""
        model_paths = [
            "heart_disease_best_model.joblib",
            "./heart_disease_best_model.joblib",
            Path(__file__).parent / "heart_disease_best_model.joblib"
        ]
        
        for path in model_paths:
            if os.path.exists(path):
                try:
                    self.model = joblib.load(path)
                    self.model_loaded = True
                    print(f"✅ Model loaded from: {path}")
                    return
                except Exception as e:
                    print(f"❌ Error loading model: {e}")
        
        print("⚠️ Model not found. Please ensure 'heart_disease_best_model.joblib' is in the same directory.")
    
    def create_widgets(self):
        """Create GUI widgets"""
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = ttk.Label(
            main_frame,
            text="💓 Heart Disease Risk Prediction System",
            font=("Arial", 18, "bold")
        )
        title_label.pack(pady=10)
        
        # Status
        status_text = "✅ Model Loaded" if self.model_loaded else "❌ Model Not Loaded"
        status_color = "#28a745" if self.model_loaded else "#dc3545"
        status_label = ttk.Label(
            main_frame,
            text=f"Status: {status_text}",
            font=("Arial", 10, "italic"),
            foreground=status_color
        )
        status_label.pack(pady=5)
        
        # Patient data frame
        self.data_frame = ttk.LabelFrame(main_frame, text="Patient Information", padding="15")
        self.data_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Create input fields
        self.inputs = {}
        self.create_input_fields()
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=15)
        
        predict_btn = ttk.Button(
            button_frame,
            text="🔮 Predict",
            command=self.predict,
            width=15
        )
        predict_btn.pack(side=tk.LEFT, padx=5)
        
        reset_btn = ttk.Button(
            button_frame,
            text="🔄 Reset",
            command=self.reset_inputs,
            width=15
        )
        reset_btn.pack(side=tk.LEFT, padx=5)
        
        load_btn = ttk.Button(
            button_frame,
            text="📂 Load Sample",
            command=self.load_sample,
            width=15
        )
        load_btn.pack(side=tk.LEFT, padx=5)
        
        # Result frame
        self.result_frame = ttk.LabelFrame(main_frame, text="Prediction Result", padding="15")
        self.result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        self.result_label = ttk.Label(
            self.result_frame,
            text="Enter patient data and click 'Predict' to see results",
            font=("Arial", 11),
            justify=tk.CENTER
        )
        self.result_label.pack(pady=20)
        
        self.result_details = tk.Text(
            self.result_frame,
            height=8,
            width=70,
            font=("Courier", 10),
            state=tk.DISABLED,
            bg="#f9f9f9"
        )
        self.result_details.pack(pady=5)
    
    def create_input_fields(self):
        """Create input fields for patient data"""
        # Field definitions (name, label, default, type)
        fields = [
            ("age", "Age (years)", "55", "int"),
            ("sex", "Sex (1=Male, 0=Female)", "1", "int"),
            ("cp", "Chest Pain Type (0-3)", "2", "int"),
            ("trestbps", "Resting BP (mmHg)", "130", "int"),
            ("chol", "Cholesterol (mg/dl)", "250", "int"),
            ("fbs", "Fasting BS > 120 (1=Yes, 0=No)", "0", "int"),
            ("restecg", "Resting ECG (0-2)", "1", "int"),
            ("thalach", "Max Heart Rate Achieved", "150", "int"),
            ("exang", "Exercise Induced Angina (1=Yes, 0=No)", "0", "int"),
            ("oldpeak", "ST Depression (0-6.2)", "1.2", "float"),
            ("slope", "ST Slope (0-2)", "2", "int"),
            ("ca", "Num Major Vessels (0-4)", "0", "int"),
            ("thal", "Thal Type (0-3)", "2", "int"),
        ]
        
        # Create two columns
        left_frame = ttk.Frame(self.data_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        
        right_frame = ttk.Frame(self.data_frame)
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        
        for idx, (name, label, default, dtype) in enumerate(fields):
            current_frame = left_frame if idx < len(fields) // 2 else right_frame
            
            frame = ttk.Frame(current_frame)
            frame.pack(fill=tk.X, pady=5)
            
            label_widget = ttk.Label(frame, text=label, width=25)
            label_widget.pack(side=tk.LEFT)
            
            entry = ttk.Entry(frame, width=15)
            entry.insert(0, default)
            entry.pack(side=tk.LEFT, padx=5)
            
            self.inputs[name] = {
                "widget": entry,
                "type": dtype,
                "label": label
            }
    
    def load_sample(self):
        """Load sample patient data"""
        sample_data = {
            "age": "55",
            "sex": "1",
            "cp": "2",
            "trestbps": "130",
            "chol": "250",
            "fbs": "0",
            "restecg": "1",
            "thalach": "150",
            "exang": "0",
            "oldpeak": "1.2",
            "slope": "2",
            "ca": "0",
            "thal": "2"
        }
        
        for name, value in sample_data.items():
            self.inputs[name]["widget"].delete(0, tk.END)
            self.inputs[name]["widget"].insert(0, value)
        
        messagebox.showinfo("Sample Data", "Sample data loaded successfully!")
    
    def reset_inputs(self):
        """Reset all input fields"""
        default_values = {
            "age": "55", "sex": "1", "cp": "2", "trestbps": "130",
            "chol": "250", "fbs": "0", "restecg": "1", "thalach": "150",
            "exang": "0", "oldpeak": "1.2", "slope": "2", "ca": "0", "thal": "2"
        }
        
        for name, value in default_values.items():
            self.inputs[name]["widget"].delete(0, tk.END)
            self.inputs[name]["widget"].insert(0, value)
        
        self.result_details.config(state=tk.NORMAL)
        self.result_details.delete(1.0, tk.END)
        self.result_details.config(state=tk.DISABLED)
        self.result_label.config(text="Enter patient data and click 'Predict' to see results")
    
    def predict(self):
        """Make prediction based on input data"""
        if not self.model_loaded:
            messagebox.showerror("Error", "Model is not loaded. Please check the model file.")
            return
        
        try:
            # Collect input data
            patient_data = {}
            for name, info in self.inputs.items():
                try:
                    value = info["widget"].get()
                    if info["type"] == "int":
                        patient_data[name] = int(value)
                    else:
                        patient_data[name] = float(value)
                except ValueError:
                    messagebox.showerror("Input Error", f"Invalid value for {info['label']}")
                    return
            
            # Create DataFrame
            input_df = pd.DataFrame([patient_data])
            
            # Make prediction
            prediction = self.model.predict(input_df)[0]
            probability = self.model.predict_proba(input_df)[0][1]
            
            # Display results
            self.display_results(prediction, probability, patient_data)
            
        except Exception as e:
            messagebox.showerror("Prediction Error", f"Error during prediction:\n{str(e)}")
    
    def display_results(self, prediction, probability, patient_data):
        """Display prediction results"""
        risk_level = "HIGH RISK ⚠️" if prediction == 1 else "LOW RISK ✅"
        risk_color = "red" if prediction == 1 else "green"
        risk_percentage = probability * 100
        
        # Update result label
        result_text = f"{risk_level}\nRisk Score: {risk_percentage:.2f}%"
        self.result_label.config(text=result_text, foreground=risk_color)
        
        # Update details
        details = f"""
{'='*70}
PREDICTION REPORT
{'='*70}

Patient Information:
{'-'*70}
"""
        for name, value in patient_data.items():
            details += f"  {name:15} = {value:>10}\n"
        
        details += f"""
{'='*70}
DIAGNOSIS RESULT
{'='*70}

Risk Classification : {risk_level}
Risk Probability    : {risk_percentage:.2f}%
Confidence Score    : {max(probability, 1-probability)*100:.2f}%

{'='*70}
INTERPRETATION:
{'-'*70}"""
        
        if prediction == 1:
            details += f"""
This patient shows HIGH RISK of heart disease.
Risk Score: {risk_percentage:.2f}%

⚠️  RECOMMENDATIONS:
  • Schedule urgent consultation with cardiologist
  • Consider advanced cardiac tests (ECG, stress test, angiography)
  • Review and manage risk factors (diet, exercise, stress)
  • Monitor vital signs regularly
  • Consider preventive medication if recommended by doctor
"""
        else:
            details += f"""
This patient shows LOW RISK of heart disease.
Risk Score: {risk_percentage:.2f}%

✅ RECOMMENDATIONS:
  • Continue regular health check-ups
  • Maintain healthy lifestyle (diet & exercise)
  • Monitor blood pressure and cholesterol
  • Avoid risk factors (smoking, excessive stress)
  • Schedule follow-up in 6-12 months
"""
        
        details += f"\n{'='*70}\n"
        
        # Display in text widget
        self.result_details.config(state=tk.NORMAL)
        self.result_details.delete(1.0, tk.END)
        self.result_details.insert(1.0, details)
        self.result_details.config(state=tk.DISABLED)


def main():
    """Main entry point"""
    root = tk.Tk()
    app = HeartDiseasePredictor(root)
    root.mainloop()


if __name__ == "__main__":
    main()
