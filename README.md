# 🧑‍💼 Curriculum Vitae & Portfolio Backend

Este proyecto es una aplicación **backend desarrollada con Django** que permite la **creación, gestión y visualización de currículums y portafolios profesionales**.  
Su objetivo es ofrecer una base sólida para construir una plataforma donde los usuarios puedan registrar su información profesional, proyectos, habilidades y experiencia laboral.

---

## 🚀 Características principales

- Registro y autenticación de usuarios.
- Creación y edición de currículums (CV) personalizados.
- Gestión de información profesional:
  - Datos personales.
  - Experiencia laboral.
  - Educación.
  - Habilidades y certificaciones.
- Módulo de portafolio con proyectos asociados.
- API REST para consumo desde frontend o aplicaciones externas.
- Panel de administración con Django Admin.
- Estructura escalable y modular para futuros componentes.

---

## 🧰 Tecnologías utilizadas

- **Python 3.10+**
- **Django 4.x**
- **Django REST Framework (DRF)**
- **SQLite / PostgreSQL** (según configuración)
- **Docker** (opcional, para despliegue)
- **Git & GitHub Actions** (para control de versiones e integración continua)

---

## ⚙️ Instalación y configuración

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/fabioCordoba/curriculum_vitae.git
cd curriculum_vitae
```
### 2️⃣ Crear y activar entorno virtualg

```bash
python -m venv venv
source venv/bin/activate   # En Linux / Mac
venv\Scripts\activate      # En Windows
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```
### 4️⃣ Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```
### 5️⃣ Crear usuario administrador

```bash
python manage.py createsuperuser
```

### 6️⃣ Ejecutar el servidor
```bash
python manage.py runserver
```

El servidor estará disponible en:
👉 http://localhost:8000

## 🧩 Endpoints principales (ejemplo)

| Método | Endpoint               | Descripción                     |
| :----: | :--------------------- | :------------------------------ |
| `POST` | `/api/users/register/` | Registro de nuevos usuarios     |
| `POST` | `/api/auth/login/`     | Inicio de sesión                |
|  `GET` | `/api/cv/`             | Listar currículums del usuario  |
| `POST` | `/api/cv/`             | Crear nuevo currículum          |
|  `GET` | `/api/portfolio/`      | Listar proyectos del portafolio |

📁 Estructura del proyecto (resumen)

```bash
curriculum_vitae/
├── manage.py
├── requirements.txt
├── README.md
├── apps/                 # Apps para gestión de CV
|   ├── core/
|   ├── contact/
|   ├── curriculum/
|   ├── education/
|   ├── portfolio/
|   ├── skill/
|   ├── users/
|   └── work_experience/
├── curriculum_vitae/     # App principal del proyecto
├── docker_prod/          # docker compose de proyecto
├── static/               # Archivos estaticos
└── ...

```
