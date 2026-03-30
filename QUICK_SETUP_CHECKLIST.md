# ✅ SUPABASE SETUP CHECKLIST

## 🔧 Những Gì Tôi Đã Tạo Cho Bạn

✅ **File modules:**
- `supabase_client.py` - Database helper (tất cả logic Supabase ở đây)
- `.streamlit/secrets.toml` - Template secrets (cần điền credentials)
- `SUPABASE_SETUP_GUIDE.md` - Chi tiết hướng dẫn

✅ **Code updates:**
- `streamlit_heart_disease_app.py` - Cập nhật dùng Supabase
- `requirements.txt` - Thêm `supabase` library
- `.gitignore` - Bảo vệ secrets khỏi GitHub

---

## 🎯 Việc Bạn Cần Làm

### BƯỚC 1️⃣: Tạo Supabase Project
- [ ] Vào https://supabase.com/dashboard
- [ ] Click "New project"
- [ ] Tên project: `heart-disease-predictor`
- [ ] Chọn region gần bạn
- [ ] **LƯU MẬT KHẨU DATABASE** (sử dụng sau)
- [ ] Chờ 2-3 phút initialize

**⏱️ Estimated time: 5-10 phút**

---

### BƯỚC 2️⃣: Tạo Database Table
- [ ] Vào Dashboard → SQL Editor
- [ ] Click "New Query"
- [ ] Copy SQL từ `SUPABASE_SETUP_GUIDE.md` (phần Step 2)
- [ ] Click "Run"
- [ ] Kiểm tra: `✓ Success`

**⏱️ Estimated time: 2 phút**

---

### BƯỚC 3️⃣: Lấy Credentials
- [ ] Vào Dashboard → Project Settings
- [ ] Tab "API"
- [ ] Copy `SUPABASE_URL` (cái URL)
- [ ] Copy `SUPABASE_KEY` (anon public key)

**⏱️ Estimated time: 2 phút**

---

### BƯỚC 4️⃣: Điền Secrets cho Local Development
- [ ] Mở file: `.streamlit/secrets.toml`
- [ ] Thay thế `SUPABASE_URL` (từ bước 3)
- [ ] Thay thế `SUPABASE_KEY` (từ bước 3)
- [ ] Save file

**File sẽ trông như này:**
```toml
SUPABASE_URL = "https://your-project-id.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIU..."
```

**⏱️ Estimated time: 2 phút**

---

### BƯỚC 5️⃣: Install Dependencies
```bash
pip install -r requirements.txt
```

**⏱️ Estimated time: 3-5 phút (tùy network)**

---

### BƯỚC 6️⃣: Test Locally
```bash
streamlit run streamlit_heart_disease_app.py
```

Sau đó:
- [ ] Vào trang "🔮 Predict"
- [ ] Điền dữ liệu patient
- [ ] Click "🔮 Predict"
- [ ] Kiểm tra message: `✅ Prediction automatically saved to database!`
- [ ] Vào trang "📜 History"
- [ ] Kiểm tra dữ liệu hiển thị ✨

**⏱️ Estimated time: 5 phút**

---

### BƯỚC 7️⃣ (Optional): Verify in Supabase Dashboard
- [ ] Vào https://supabase.com/dashboard
- [ ] Project → Table Editor
- [ ] Select `predictions_history` table
- [ ] Kiểm tra rows bạn tạo

---

### BƯỚC 8️⃣ (Optional): Deploy lên Streamlit Cloud
- [ ] Push code lên GitHub
  ```bash
  git add .
  git commit -m "Add Supabase integration"
  git push origin main
  ```

- [ ] Vào https://share.streamlit.io
- [ ] Click "New app"
- [ ] Link với repo GitHub của bạn
- [ ] Vào App Settings → Secrets
- [ ] Paste 2 dòng (SUPABASE_URL + SUPABASE_KEY)
- [ ] Click Save

---

## 🆘 Nếu Gặp Lỗi

| Lỗi | Giải pháp |
|-----|----------|
| `ModuleNotFoundError: No module named 'supabase'` | Chạy: `pip install supabase` |
| `Supabase credentials not found` | Kiểm tra: `.streamlit/secrets.toml` có tồn tại không |
| `Table 'predictions_history' does not exist` | Chạy SQL từ SUPABASE_SETUP_GUIDE.md Step 2 |
| `Invalid API key` | Copy lại key từ Dashboard (anon public) |
| Không có dữ liệu ở History | Kiểm tra: prediction có message `✅ saved` không |

**Chi tiết: Xem `SUPABASE_SETUP_GUIDE.md` phần Troubleshooting**

---

## 📊 Kết Quả Sau Setup

✅ Khi predict:
- Dữ liệu tự động lưu vào Supabase (không cần button)
- Message: `✅ Prediction automatically saved to database!`

✅ Ở History page:
- Xem tất cả predictions từ database
- Pie chart, timeline chart
- Export CSV, Clear history

✅ Ở Supabase Dashboard:
- Quản lý dữ liệu trực tiếp
- Thêm/xóa/sửa records

---

## 🎓 Kiến Thức Bạn Học Được

✅ **Secrets Management**: Cách an toàn lưu credentials
✅ **Supabase Integration**: PostgreSQL database backend
✅ **Production Deployment**: GitHub + Streamlit Cloud
✅ **Best Practices**: `.gitignore`, environment variables

---

## 📞 Questions?

Refer to:
- [`SUPABASE_SETUP_GUIDE.md`](./SUPABASE_SETUP_GUIDE.md) - Chi tiết step-by-step
- [`supabase_client.py`](./supabase_client.py) - Code comments
- `.streamlit/secrets.toml` - Template & notes

---

**Chúc bạn setup thành công! 🚀❤️**
