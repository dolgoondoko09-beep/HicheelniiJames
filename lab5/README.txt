ЛАБ №5 - ГАРЫН АВЛАГА (MUSHOP ДИЗАЙН)
====================================

ХАМГИЙН ХЯЛБАР АРГА:
   start.bat дээр хоёр товшиж ажиллуулна.
   Энэ нь автоматаар:
   - Pillow суулгана
   - makemigrations + migrate хийнэ (ТИЙМ, хэрэгтэй - анх удаа)
   - 5 ангилал, 11 бараа (жинхэнэ зурагтай) оруулна
   - Серверийг http://127.0.0.1:8000/ дээр асаана

ГАРААР АЖИЛЛУУЛАХ:
   cd lab5\ecommerce
   py manage.py makemigrations store
   py manage.py migrate
   cmd /c "py manage.py shell < load_data.py"
   py manage.py runserver

АДМИН PANEL (шаардлагатай бол):
   py manage.py createsuperuser
   http://127.0.0.1:8000/admin/

ХУУДАС:
   /                         -> Home (hero banner, ангилал, бараа, promo, features)
   /store/                   -> Бүх бараа (sidebar ангилал, sort chip)
   /store/<slug>/            -> Ангиллаар шүүгдсэн бараа
   /store/?q=headphones      -> Нэрээр хайх (header дээрх search)
   /store/?sort=price_asc    -> Үнээр эрэмбэлэх (chip-үүд дээр дарна)

ДИЗАЙН (mushop.mn-ийн загвартай):
   - static/css/style.css нь MUSHOP дизайн системийг агуулна
     (primary blue #56a9e1, orange #f97c2f, Montserrat фонт).
   - Icons нь inline SVG тул Font Awesome фонт шаардлагагүй.
   - Bootstrap/jQuery хэрэглэхгүй (bootstrap.css, jquery файлууд
     одоо ашиглагдахгүй, устгавал ч болно).
   - Montserrat фонт Google Fonts-оос татагдана; интернэтгүй үед
     Arial руу шилжинэ (бүх зүйл хэвээр ажиллана).

АНХААРУУЛГА:
   - migrate/makemigrations нь зөвхөн АНХНЫ удаа эсвэл models.py
     өөрчилсөн үед хэрэгтэй. Өгөгдлийн сан (db.sqlite3) үүссэн бол
     дараагийн удаа шууд "py manage.py runserver" хангалттай.
