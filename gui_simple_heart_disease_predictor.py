#!/usr/bin/env python
"""
Alternative Simple GUI for Heart Disease Prediction
Uses PySimpleGUI for a more lightweight interface
Install: pip install PySimpleGUI

Run: python gui_simple_heart_disease_predictor.py
"""

import PySimpleGUI as sg
import pandas as pd
import joblib
import os

# Set theme
sg.theme('DarkBlue3')

class SimpleHeartDiseaseGUI:
    def __init__(self):
        self.model = self.load_model()
        self.window = None
        
    def load_model(self):
        """Load the trained model"""
        if os.path.exists('heart_disease_best_model.joblib'):
            try:
                return joblib.load('heart_disease_best_model.joblib')
            except Exception as e:
                print(f"Error loading model: {e}")
                return None
        return None
    
    def create_layout(self):
        """Create GUI layout"""
        layout = [
            [sg.Text('❤️ Heart Disease Predictor', font=('Arial', 18, 'bold'))],
            [sg.Text('Enter patient information:', font=('Arial', 12))],
            [sg.Text('_' * 50)],
            
            # Input fields - 2 columns
            [
                [sg.Column([
                    [sg.Text('Age:', size=(15, 1)), sg.InputText(default_text='55', size=(15, 1), key='age')],
                    [sg.Text('Sex (1=M, 0=F):', size=(15, 1)), sg.InputText(default_text='1', size=(15, 1), key='sex')],
                    [sg.Text('Chest Pain (0-3):', size=(15, 1)), sg.InputText(default_text='2', size=(15, 1), key='cp')],
                    [sg.Text('Rest BP (mmHg):', size=(15, 1)), sg.InputText(default_text='130', size=(15, 1), key='trestbps')],
                    [sg.Text('Cholesterol:', size=(15, 1)), sg.InputText(default_text='250', size=(15, 1), key='chol')],
                    [sg.Text('Fasting BS (0/1):', size=(15, 1)), sg.InputText(default_text='0', size=(15, 1), key='fbs')],
                    [sg.Text('Resting ECG (0-2):', size=(15, 1)), sg.InputText(default_text='1', size=(15, 1), key='restecg')],
                ]),
                sg.Column([
                    [sg.Text('Max Heart Rate:', size=(15, 1)), sg.InputText(default_text='150', size=(15, 1), key='thalach')],
                    [sg.Text('Exercise Angina (0/1):', size=(15, 1)), sg.InputText(default_text='0', size=(15, 1), key='exang')],
                    [sg.Text('ST Depression:', size=(15, 1)), sg.InputText(default_text='1.2', size=(15, 1), key='oldpeak')],
                    [sg.Text('ST Slope (0-2):', size=(15, 1)), sg.InputText(default_text='2', size=(15, 1), key='slope')],
                    [sg.Text('Major Vessels (0-4):', size=(15, 1)), sg.InputText(default_text='0', size=(15, 1), key='ca')],
                    [sg.Text('Thal (0-3):', size=(15, 1)), sg.InputText(default_text='2', size=(15, 1), key='thal')],
                ])]
            ],
            
            [sg.Text('_' * 50)],
            
            # Buttons
            [
                sg.Button('🔮 Predict', size=(12, 1)),
                sg.Button('🔄 Reset', size=(12, 1)),
                sg.Button('📂 Sample', size=(12, 1)),
                sg.Button('❌ Exit', size=(12, 1))
            ],
            
            # Result
            [sg.Multiline(size=(60, 10), key='result', disabled=True, 
                         font=('Courier', 10), background_color='#222222')],
        ]
        return layout
    
    def run(self):
        """Run the GUI"""
        if not self.model:
            sg.popup_error('Error', 'Model not found!\nPlace heart_disease_best_model.joblib in the same directory.')
            return
        
        self.window = sg.Window('Heart Disease Predictor', self.create_layout(), size=(700, 700))
        
        while True:
            event, values = self.window.read()
            
            if event == sg.WINDOW_CLOSED or event == '❌ Exit':
                break
            
            if event == '🔮 Predict':
                self.predict(values)
            
            if event == '🔄 Reset':
                self.reset()
            
            if event == '📂 Sample':
                self.load_sample()
        
        self.window.close()
    
    def predict(self, values):
        """Make prediction"""
        try:
            patient_data = {
                'age': int(values['age']),
                'sex': int(values['sex']),
                'cp': int(values['cp']),
                'trestbps': int(values['trestbps']),
                'chol': int(values['chol']),
                'fbs': int(values['fbs']),
                'restecg': int(values['restecg']),
                'thalach': int(values['thalach']),
                'exang': int(values['exang']),
                'oldpeak': float(values['oldpeak']),
                'slope': int(values['slope']),
                'ca': int(values['ca']),
                'thal': int(values['thal']),
            }
            
            df = pd.DataFrame([patient_data])
            pred = self.model.predict(df)[0]
            prob = self.model.predict_proba(df)[0][1]
            
            risk_level = "HIGH RISK ⚠️" if pred == 1 else "LOW RISK ✅"
            result_text = f"""
{'='*50}
PREDICTION RESULT
{'='*50}

Risk Classification: {risk_level}
Risk Score:         {prob*100:.2f}%
Confidence:         {max(prob, 1-prob)*100:.2f}%

{'='*50}
PATIENT DATA SUMMARY
{'='*50}
"""
            for k, v in patient_data.items():
                result_text += f"{k:15} : {v:>10}\n"
            
            self.window['result'].update(result_text)
        
        except ValueError as e:
            sg.popup_error('Input Error', f'Invalid input: {str(e)}')
    
    def reset(self):
        """Reset all fields"""
        default_vals = {
            'age': '55', 'sex': '1', 'cp': '2', 'trestbps': '130',
            'chol': '250', 'fbs': '0', 'restecg': '1', 'thalach': '150',
            'exang': '0', 'oldpeak': '1.2', 'slope': '2', 'ca': '0', 'thal': '2'
        }
        for key, val in default_vals.items():
            self.window[key].update(val)
        self.window['result'].update('')
    
    def load_sample(self):
        """Load sample data"""
        self.reset()
        sg.popup('Sample Data', 'Sample data loaded successfully!')


if __name__ == '__main__':
    app = SimpleHeartDiseaseGUI()
    app.run()
