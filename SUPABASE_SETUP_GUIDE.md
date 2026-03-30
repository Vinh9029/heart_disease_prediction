# 🔐 Supabase Setup Guide for Heart Disease Predictor

## 📋 Quick Summary

| Item | Local | Streamlit Cloud |
|------|-------|-----------------|
| Secrets Location | `~/.streamlit/secrets.toml` | Dashboard → Settings → Secrets |
| Credentials | `SUPABASE_URL` + `SUPABASE_KEY` | Same format |
| Table | Auto-created via SQL | Must pre-create |
| Database | Supabase PostgreSQL | Same |

---

## 🚀 Step 1: Create Supabase Project

### 1.1 Sign Up/Login
```
1. Go to https://supabase.com/dashboard
2. Sign up or login with GitHub/Google
3. Click "New project"
```

### 1.2 Create New Project
```
- Project name: heart-disease-predictor
- Database password: ⬇️ SAVE THIS! (you'll need it)
- Region: Singapore / Tokyo (pick closest to you)
- Click "Create new project"
```

**⏳ Wait 2-3 minutes for project initialization**

---

## 🗄️ Step 2: Create Database Table

### 2.1 Open SQL Editor
```
1. Dashboard → Project
2. Left sidebar → SQL Editor
3. Click "New Query"
```

### 2.2 Create Table Schema
Copy & paste this SQL:

```sql
-- Create predictions history table
CREATE TABLE predictions_history (
    id BIGSERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT NOW(),
    prediction TEXT NOT NULL CHECK (prediction IN ('HIGH RISK', 'LOW RISK')),
    risk_score TEXT NOT NULL,
    age INTEGER NOT NULL,
    sex INTEGER NOT NULL,
    cp INTEGER NOT NULL,
    trestbps INTEGER NOT NULL,
    chol INTEGER NOT NULL,
    fbs INTEGER NOT NULL,
    restecg INTEGER NOT NULL,
    thalach INTEGER NOT NULL,
    exang INTEGER NOT NULL,
    oldpeak FLOAT NOT NULL,
    slope INTEGER NOT NULL,
    ca INTEGER NOT NULL,
    thal INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Create indexes for better performance
CREATE INDEX idx_predictions_timestamp ON predictions_history(timestamp DESC);
CREATE INDEX idx_predictions_prediction ON predictions_history(prediction);
CREATE INDEX idx_predictions_created_at ON predictions_history(created_at DESC);

-- Enable Row Level Security (optional - for future multi-user support)
ALTER TABLE predictions_history ENABLE ROW LEVEL SECURITY;
```

### 2.3 Execute Query
```
Click "Run" or Ctrl+Enter
Result: ✓ Success
```

---

## 🔑 Step 3: Get Supabase Credentials

### 3.1 Get URL and Keys
```
1. Dashboard → Project Settings (⚙️ icon, bottom-left)
2. Tab: "API"
3. Copy these TWO things:

   A. SUPABASE_URL:
      - Look for "URL"
      - Looks like: https://xxxxx.supabase.co
      
   B. SUPABASE_KEY (anon/public):
      - Look for "Project API keys"
      - Under "anon public" section
      - Looks like: eyJhbGciOiJI...
```

### ⚠️ Security Notes
- ✅ `anon public` key is SAFE to commit (client-side only)
- ❌ `service_role` key is SECRET (server-only)
- ❌ Database password is SECRET (do NOT commit)

---

## 💻 Step 4: Setup Local Development Secrets

### 4.1 Create `.streamlit/secrets.toml`

**On Windows PowerShell:**
```powershell
# Already created by the setup script
# File: C:\Users\YourUsername\Downloads\DataMining\.streamlit\secrets.toml
```

### 4.2 Fill in Credentials

Edit `.streamlit/secrets.toml`:

```toml
# Supabase Configuration
SUPABASE_URL = "https://xxxxxxxxxxxxx.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6yourprojectidxxxxxxxx..."
```

### 4.3 Save and Test

```bash
# Install Supabase client
pip install -r requirements.txt

# Test connection
streamlit run streamlit_heart_disease_app.py

# Go to: http://localhost:8501
# Try making a prediction - should save to database!
```

---

## ☁️ Step 5: Deploy to Streamlit Cloud

### 5.1 Connect GitHub Repository

```
1. Push your code to GitHub:
   - Make sure .streamlit/secrets.toml is in .gitignore ✅
   - Commit other files
   
2. Go to https://share.streamlit.io
3. Click "New app"
4. Select your GitHub repo and file
```

### 5.2 Add Secrets on Streamlit Cloud

```
1. After linking repo, go to App settings
2. Click "Secrets" (bottom left)
3. Paste your secrets:

   SUPABASE_URL = "https://xxxxx.supabase.co"
   SUPABASE_KEY = "eyJhbGciOi..."

4. Click "Save"
5. App will auto-redeploy ✨
```

### 5.3 Troubleshooting Deployment

If you get "secrets not found" error:

```
1. Check .gitignore includes: .streamlit/secrets.toml
2. Re-add secrets on Streamlit Cloud
3. Click "Redeploy" button
4. Check logs for errors
```

---

## 🧪 Step 6: Test Everything

### 6.1 Local Testing

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run app
streamlit run streamlit_heart_disease_app.py

# 3. Test workflow:
#    - Go to "Predict" page
#    - Fill in patient data
#    - Click "Predict"
#    - Should see ✅ "Prediction automatically saved to database!"
#    - Go to "History" page
#    - Should see your prediction in the table
```

### 6.2 Verify in Supabase Dashboard

```
1. Go to https://supabase.com/dashboard
2. Project → Table Editor
3. Select "predictions_history" table
4. You should see your saved predictions ✨
```

---

## 📁 File Structure

```
DataMining/
├── .streamlit/
│   └── secrets.toml          ← Local secrets (GITIGNORE!)
├── supabase_client.py         ← Database helper module
├── streamlit_heart_disease_app.py  ← Main app (updated)
├── requirements.txt           ← Updated with supabase
├── .gitignore                 ← Updated
└── [other files...]
```

---

## 🔧 Troubleshooting

### ❌ Error: "Supabase credentials not found!"

**Solution:**
```
1. Check file exists: .streamlit/secrets.toml
2. Verify it has correct format (TOML, not JSON)
3. Restart Streamlit: Ctrl+C, then run again
4. For Streamlit Cloud: add via dashboard Secrets
```

### ❌ Error: "Table 'predictions_history' does not exist"

**Solution:**
```
1. Go to Supabase Dashboard
2. SQL Editor → Run the CREATE TABLE SQL (from Step 2)
3. Verify table appears in Table Editor
```

### ❌ Error: "Invalid API key"

**Solution:**
```
1. Go to Project Settings → API
2. Copy FULL key from "anon public" section
3. Make sure NO extra spaces/quotes
4. Re-enter in .streamlit/secrets.toml
```

### ❌ No data appears in History page

**Solution:**
```
1. Make sure you ran Step 2 (created table)
2. Check predictions show ✅ "saved successfully" message
3. Go to Supabase Dashboard → Table Editor
4. Verify data is actually there
5. If nothing: might be permission issue (RLS)
```

---

## 📊 What Gets Stored

Each prediction saves:
```
✅ timestamp      - When prediction was made
✅ prediction     - "HIGH RISK" or "LOW RISK"
✅ risk_score     - Probability percentage (e.g., "75.3%")
✅ age to thal    - All 13 medical parameters
✅ created_at     - Database record creation time
```

---

## 🚀 Next Steps

After setup works:

1. **Customize** the Streamlit app further
2. **Add user authentication** (Supabase Auth)
3. **Create dashboards** with aggregated stats
4. **Export reports** to PDF/Excel
5. **Scale to multi-user** production

---

## 📞 Support

Error messages? Check:
- ✅ [Supabase Docs](https://supabase.com/docs)
- ✅ [Streamlit Secrets](https://docs.streamlit.io/streamlit-community-cloud/deploy-your-app/secrets-management)
- ✅ [supabase_client.py](./supabase_client.py) code comments

---

**Happy Predicting! ❤️**
