## Flask project tutorial

### Project structure

```ignorelang
/PYTA_2/S8/ST2/
├── flaskr/                 # acesta este folderul proiectului propriu-zis (root)
│   ├── __init__.py         # fisier special care face acest folder sa fie un modul Python
│   ├── db.py               # aici avem configurarea/init/rularea bazei de date
│   ├── schema.sql          # aici se genereaza tabelele din db
│   ├── auth.py             # aici vom avea rutele care tin de modulul de auth
│   ├── blog.py             # aici vom avea rutele care tin de modulul de blog
│   ├── templates/          # aici vom avea template-urile HTML
│   │   ├── base.html       # baza site-ului nostru HTML, permite sa refolosim anumite elemente structurale (header, footer, etc)
│   │   ├── auth/           # folder pt templates de auth
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/           # folder pt templates de blog posts
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/             # aici vom avea fisierele de stil (CSS)
│       └── style.css
├── tests/                  # aici vom avea tot ce tine de teste (NU FACEM ACUM)
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── .venv/                  # virtual environment
├── requirements.txt        # dependintele proiectului          
└── README.ms               # fisierul curent, in care punem instructiuni de instalare si executie
```

### How to Markdown
- [Link 1](https://www.markdownguide.org/getting-started/)
- [Link 2](https://www.markdownguide.org/cheat-sheet/)