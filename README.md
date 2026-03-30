### ℹ️ About This Application

**Heart Disease Prediction System** is an AI-powered web application that uses
machine learning to assess the risk of heart disease based on clinical attributes.

#### 🎯 Project Goals

1. **Predict Heart Disease Risk** - Estimate likelihood of heart disease from clinical data  
2. **Support Medical Decision Making** - Provide AI-assisted risk assessment  
3. **Educate Users** - Demonstrate ML capabilities in healthcare  
4. **Enable Batch Analysis** - Process multiple patients efficiently  

#### 🛠️ Technology Stack

- **Framework:** Streamlit (Web UI)  
- **ML Library:** Scikit-learn  
- **Advanced Models:** XGBoost  
- **Visualization:** Plotly  
- **Data Processing:** Pandas, NumPy  

#### 📚 Dataset

- **Source:** UCI Machine Learning Repository (Heart Disease Dataset)  
- **Samples:** 1025 patient records  
- **Features:** 13 clinical attributes  
- **Target:** Binary (Heart Disease: Yes/No)  
- **Class Distribution:** 51% Negative, 49% Positive (Well-balanced)  

#### 🔬 Machine Learning Pipeline

1. **Data Preprocessing**
   - Handling missing values  
   - Feature scaling  
   - Categorical encoding  

2. **Model Training**
   - 11 different algorithms evaluated  
   - Hyperparameter tuning with GridSearchCV  
   - Cross-validation (5-fold)  

3. **Model Evaluation**
   - Accuracy, Precision, Recall, F1-Score  
   - ROC-AUC analysis  
   - Confusion matrix analysis  

4. **Model Selection**
   - Best model: XGBoost  
   - Performance: ~85–90% accuracy  

#### 📊 Features Used (13)

1. **Age** - Patient age in years  
2. **Sex** - Gender (1=Male, 0=Female)  
3. **Chest Pain Type** - 0–3 classification  
4. **Resting BP** - Resting blood pressure (mmHg)  
5. **Cholesterol** - Serum cholesterol (mg/dl)  
6. **Fasting BS** - Fasting blood sugar > 120  
7. **Resting ECG** - Resting electrocardiogram (0–2)  
8. **Max Heart Rate** - Maximum heart rate achieved  
9. **Exercise Angina** - Angina induced by exercise  
10. **ST Depression** - ST segment depression  
11. **ST Slope** - Slope of ST segment (0–2)  
12. **Major Vessels** - Fluoroscopy colored vessels (0–4)  
13. **Thalassemia Type** - Blood disorder type (0–3)  

#### 📈 Expected Accuracy

- Typical accuracy range: **80–90%**  
- F1-Score: **0.76–0.84**  
- ROC-AUC: **0.85–0.93**  

#### ⚠️ Important Notes

- This is an **educational tool**, not a clinical diagnostic system  
- **Always consult healthcare professionals** for medical decisions  
- Predictions should be used as **supportive information only**  
- Model performance varies based on input data quality  

#### 👨‍💻 Development

- **Language:** Python 3.7+  
- **Platform:** Streamlit (Web-based)  
- **Model Format:** Joblib (Serialized)  
- **Deployment:** Local or Cloud  

#### 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run streamlit_heart_disease_app.py

# Open browser to http://localhost:8501
```

#### 📞 Contact & Resources

- **Dataset:** https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction/data  
- **Streamlit Docs:** https://docs.streamlit.io/  
- **Scikit-learn:** https://scikit-learn.org/  
- **XGBoost:** https://xgboost.readthedocs.io/  

---

**Status:** ✅ Production Ready  
**Version:** 1.0  
**Last Updated:** March 2026
