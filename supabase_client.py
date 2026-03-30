"""
❤️ Supabase Client Module
========================
Handles all Supabase database operations for Heart Disease Predictor
"""

import streamlit as st
import pandas as pd
from supabase import create_client, Client
from datetime import datetime


@st.cache_resource
def init_supabase() -> Client:
    """
    Initialize and cache Supabase client
    
    Returns:
        Client: Supabase client instance
        
    Raises:
        Exception: If credentials are missing or connection fails
    """
    try:
        # Lấy credentials từ Streamlit Secrets
        url = st.secrets.get("SUPABASE_URL")
        key = st.secrets.get("SUPABASE_KEY")
        
        # Validate credentials
        if not url or not key:
            st.error(
                "❌ **Supabase credentials not found!**\n\n"
                "**Local Setup:**\n"
                "1. Tạo file `.streamlit/secrets.toml`\n"
                "2. Điền `SUPABASE_URL` và `SUPABASE_KEY`\n\n"
                "**Streamlit Cloud:**\n"
                "1. Vào Settings → Secrets\n"
                "2. Paste credentials\n\n"
                "📖 Xem `.streamlit/secrets.toml` để biết chi tiết"
            )
            st.stop()
        
        # Create Supabase client
        supabase: Client = create_client(url, key)
        return supabase
        
    except Exception as e:
        st.error(f"❌ **Supabase Connection Error:**\n\n{str(e)}")
        st.stop()


def save_prediction_to_supabase(patient_data: dict, prediction: int, probability: float) -> bool:
    """
    Save prediction to Supabase database
    
    Args:
        patient_data (dict): Patient clinical data
        prediction (int): Prediction result (0 or 1)
        probability (float): Prediction probability
        
    Returns:
        bool: True if success, False otherwise
    """
    try:
        supabase = init_supabase()
        
        # Prepare record for database
        history_record = {
            'timestamp': datetime.now().isoformat(),
            'prediction': 'HIGH RISK' if prediction == 1 else 'LOW RISK',
            'risk_score': f"{probability*100:.1f}%",
            'age': int(patient_data.get('age')),
            'sex': int(patient_data.get('sex')),
            'cp': int(patient_data.get('cp')),
            'trestbps': int(patient_data.get('trestbps')),
            'chol': int(patient_data.get('chol')),
            'fbs': int(patient_data.get('fbs')),
            'restecg': int(patient_data.get('restecg')),
            'thalach': int(patient_data.get('thalach')),
            'exang': int(patient_data.get('exang')),
            'oldpeak': float(patient_data.get('oldpeak')),
            'slope': int(patient_data.get('slope')),
            'ca': int(patient_data.get('ca')),
            'thal': int(patient_data.get('thal')),
        }
        
        # Insert to Supabase
        response = supabase.table('predictions_history').insert(history_record).execute()
        
        if response.data:
            return True
        else:
            return False
            
    except Exception as e:
        st.error(f"❌ **Error saving to database:** {str(e)}")
        return False


def load_prediction_history(limit: int = 100) -> pd.DataFrame:
    """
    Load prediction history from Supabase
    
    Args:
        limit (int): Maximum number of records to fetch (default: 100)
        
    Returns:
        pd.DataFrame: Prediction history data
    """
    try:
        supabase = init_supabase()
        
        # Fetch data from Supabase (newest first)
        response = supabase.table('predictions_history') \
            .select("*") \
            .order('timestamp', desc=True) \
            .limit(limit) \
            .execute()
        
        if response.data and len(response.data) > 0:
            df = pd.DataFrame(response.data)
            # Convert timestamp to datetime
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            return df
        else:
            return pd.DataFrame()
            
    except Exception as e:
        st.error(f"❌ **Error loading history:** {str(e)}")
        return pd.DataFrame()


def get_history_stats() -> dict:
    """
    Get statistics from prediction history
    
    Returns:
        dict: Statistics including total predictions, high risk count, etc.
    """
    try:
        supabase = init_supabase()
        
        # Get total count
        total_response = supabase.table('predictions_history') \
            .select("*", count='exact') \
            .execute()
        total_count = total_response.count if hasattr(total_response, 'count') else 0
        
        # Get high risk count
        high_risk_response = supabase.table('predictions_history') \
            .select("*") \
            .eq('prediction', 'HIGH RISK') \
            .execute()
        high_risk_count = len(high_risk_response.data) if high_risk_response.data else 0
        
        return {
            'total': total_count,
            'high_risk': high_risk_count,
            'low_risk': total_count - high_risk_count,
            'high_risk_percentage': (high_risk_count / total_count * 100) if total_count > 0 else 0
        }
        
    except Exception as e:
        st.error(f"❌ **Error getting statistics:** {str(e)}")
        return {'total': 0, 'high_risk': 0, 'low_risk': 0, 'high_risk_percentage': 0}


def delete_all_history() -> bool:
    """
    Delete all prediction history
    
    Returns:
        bool: True if success, False otherwise
    """
    try:
        supabase = init_supabase()
        supabase.table('predictions_history').delete().neq('id', -1).execute()
        return True
    except Exception as e:
        st.error(f"❌ **Error deleting history:** {str(e)}")
        return False


# Health check function for debugging
def test_supabase_connection() -> bool:
    """
    Test Supabase connection
    
    Returns:
        bool: True if connection successful
    """
    try:
        supabase = init_supabase()
        response = supabase.table('predictions_history').select('*').limit(1).execute()
        return True
    except Exception as e:
        st.error(f"❌ Connection test failed: {str(e)}")
        return False
