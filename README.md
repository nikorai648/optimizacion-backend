# API REST – Optimización y Logística

Este proyecto corresponde al Backend del sistema **Optimización y Logística**, desarrollado como una **API REST** utilizando **Django** y **Django REST Framework**.

La API gestiona la información relacionada con trabajadores, asistencias, accidentes laborales, eficiencia, desempeño y sueldos, y es consumida por aplicaciones Frontend desarrolladas en **React** y **Vue**.

---

## 🚀 Tecnologías Utilizadas

- Python 3
- Django
- Django REST Framework
- SQLite / PostgreSQL (según configuración)
- Token Authentication

---

## 📌 Funcionalidades Principales

- Autenticación de usuarios mediante token
- CRUD de Trabajadores
- CRUD de Asistencias
- CRUD de Accidentes
- CRUD de Eficiencia
- CRUD de Desempeño
- CRUD de Sueldos
- Protección de rutas mediante autenticación

---

## ⚙️ Instalación y Ejecución

1. Clonar el repositorio:
```bash
git clone https://github.com/nikorai648/optimizacion-backend.git

# API REST – Optimización y Logística

Este proyecto corresponde al Backend del sistema **Optimización y Logística**, desarrollado como una **API REST** utilizando **Django** y **Django REST Framework**.

La API gestiona la información relacionada con trabajadores, asistencias, accidentes laborales, eficiencia, desempeño y sueldos, y es consumida por aplicaciones Frontend desarrolladas en **React** y **Vue**.

---

## 🚀 Tecnologías Utilizadas

- Python 3
- Django
- Django REST Framework
- SQLite / PostgreSQL (según configuración)
- Token Authentication

---

## 📌 Funcionalidades Principales

- Autenticación de usuarios mediante token
- CRUD de Trabajadores
- CRUD de Asistencias
- CRUD de Accidentes
- CRUD de Eficiencia
- CRUD de Desempeño
- CRUD de Sueldos
- Protección de rutas mediante autenticación

---

## ⚙️ Instalación y Ejecución

1. Clonar el repositorio:
```bash
git clone https://github.com/nikorai648/optimizacion-backend.git

Crear entorno virtual e instalar dependencias:
pip install -r requirements.txt

Ejecutar migraciones:
python manage.py migrate

Iniciar el servidor:
python manage.py runserver

La API estará disponible en:
http://127.0.0.1:8000

🔐 Autenticación

La API utiliza Token Authentication.
El token se debe enviar en los headers de las peticiones:

Authorization: Token TU_TOKEN
