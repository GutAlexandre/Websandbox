import os

# Liste des bibliothèques à installer
libraries = [
    "httptools==0.5.0",
    "idna==3.4",
    "anyio==3.6.2",
    "click==8.1.3",
    "h11==0.14.0",
    "MarkupSafe==2.1.2",
    "Jinja2==3.1.2",
    "pydantic==1.10.7",
    "pyserial==3.5",
    "python-dotenv==1.0.0",
    "PyYAML",
    "sniffio==1.3.0",
    "starlette==0.26.1",
    "fastapi==0.95.0",
    "typing-extensions==4.5.0",
    "watchfiles==0.19.0",
    "websockets==11.0.3",
    "uvicorn==0.22.0",
    "phonetics==1.0.5",
    "psycopg2==2.9.1",
    "requests==2.28.2",
    "reportlab==4.0.0",
    "aiortc"
]

# Installer les bibliothèques avec pip
for library in libraries:
    print(f'Installation de {library}')
    os.system(f'pip install {library}')

print("Bibliothèques installées avec succès.")
