import os
import shutil
from fastapi import FastAPI, Request, Form, File, UploadFile
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Yuklangan rasmlarni saqlash uchun papka yaratamiz
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Rasmlarni brauzerda ko'rsatish uchun statik papka sifatida ulaymiz
app.mount("/uploads", StaticFiles(directory=UPLOAD_DIR), name="uploads")

# Shablonlar papkasini ulaymiz
templates = Jinja2Templates(directory="templates")

# Kategoriya va Xizmatlar
SERVICES_DB = {
    "Maishiy texnika": {
        "Kir yuvish mashinasiga gigiyenik xizmat ko'rsatish va tozalash": [
            ("Nodir Abdullayev", 4.9, 210, "1.0 km"),
            ("Rustam Jo'rayev", 4.7, 130, "3.2 km")
        ],
        "Gaz plitasi va pech (duhovka) ta'miri": [
            ("Davron Valiyev", 4.8, 88, "2.1 km"),
            ("Shoxrux Qosmonov", 4.6, 54, "4.3 km")
        ],
        "Rakovina va santexnika tizimlari": [
            ("Jasur Santexnik", 4.9, 310, "0.5 km"),
            ("Ilhom Zokirov", 4.8, 175, "1.8 km")
        ],
        "Muzlatgich va sovutish tizimlari": [
            ("Anvar Xolodilshik", 4.9, 190, "1.2 km")
        ],
        "Konditsioner tozalash va freon quyish": [
            ("Bekzod KOND", 4.7, 145, "2.7 km")
        ]
    },
    "Elektronika va Gadjetlar": {
        "Smartfonlar va Mobil telefonlar": [
            ("Jasurbek Aliyev (iPhone master)", 4.9, 320, "1.2 km"),
            ("Sardor Qodirov (Android master)", 4.7, 185, "2.5 km")
        ],
        "Planshetlar va iPad qurilmalari": [
            ("Bobur Usmonov", 4.8, 95, "3.1 km"),
            ("Aziz Masharipov", 4.9, 140, "1.1 km")
        ],
        "Aqlli soatlar (Smartwatch / Apple Watch)": [
            ("Farrux Gadget", 4.8, 76, "2.0 km")
        ],
        "Noutbuk va Kompyuter texnikasi": [
            ("Aziz Rahimov", 4.9, 240, "0.8 km"),
            ("Otabek Ismoilov", 4.6, 60, "2.0 km")
        ]
    }
}

BRANDS = ["Apple", "Samsung", "Xiaomi", "LG", "Bosch", "Beko", "Artel", "Lenovo", "HP", "Boshqa brend"]

WORKER_REVIEWS_DB = {
    "Jasurbek Aliyev (iPhone master)": [
        {"client": "Murod", "comment": "Ekranini 20 daqiqada almashtirib berdi, super!", "rating": 5, "photo": None}
    ],
