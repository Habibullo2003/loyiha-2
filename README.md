# 🏛️ Loyiha-2 — Madaniyat va Sportni Rivojlantirish Veb-ilovasi

## 📌 Tavsif
Loyiha-2 — madaniyat va sport sohalarini yanada rivojlantirishga qaratilgan veb-ilova. Ushbu tizim sport va madaniyat tashkilotlari faoliyatini boshqarish, tadbirlar rejasini tuzish, ishtirokchilarni ro‘yxatga olish va statistikani ko‘rish imkonini beradi.

## ⚙️ Texnologiyalar
- Python (Django)
- PostgreSQL (ma’lumotlar bazasi)
- HTML, CSS, JavaScript (frontend)

## 🚀 Asosiy funksiyalar
- Madaniyat va sport tadbirlarini boshqarish
- Tashkilotlar va ishtirokchilar ro‘yxatini yuritish
- Tadbirlar jadvalini tuzish va yangilash
- Statistik ma’lumotlarni ko‘rish

## 🖥️ Loyihani ishga tushirish
```bash
# 1. Loyihani klonlash
git clone https://github.com/Habibullo2003/loyiha-2.git
cd loyiha-2

# 2. Virtual muhit yaratish
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)

# 3. Kerakli kutubxonalarni o‘rnatish
pip install -r requirements.txt

# 4. Migratsiyalarni bajarish
python manage.py makemigrations
python manage.py migrate

# 5. Serverni ishga tushirish
python manage.py runserver
