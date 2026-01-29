#  Brain.com.ua Product Parser (Django + Selenium)

A Django-based application for automatic parsing of smartphones from **Brain.com.ua**.  
The project uses **Selenium WebDriver** to collect data, stores it in **PostgreSQL**, and supports exporting results to **CSV** with proper UTF-8 encoding for Excel.

---

## Features

### Data Parsing
- Product name
- Price
- Discount price (if available)
- Product code (SKU)
- Number of reviews
- Image links
- Main characteristics (color, memory, display, etc.)
- Full list of technical specifications

---

## 🛠 Technologies

- Python 3.10+
- Django 5.x
- Selenium WebDriver (Chrome)
- PostgreSQL
- webdriver-manager

---

##  Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/NK-TS-DEV/Selenium_task.git
cd Parser_selenium
```

---

### 2. Create a virtual environment

```bash
python -m venv .venv
```

**Windows**
```bash
.venv\Scripts\activate
```

**Mac / Linux**
```bash
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install django selenium webdriver-manager psycopg2-binary
```

---

## 🗄 Database Setup (PostgreSQL)

The project uses a dedicated database user and database.

```PostgreSQL
CREATE USER postgres_selenium WITH PASSWORD '1234';
CREATE DATABASE brain_db_selenium OWNER postgres_selenium;
GRANT ALL PRIVILEGES ON DATABASE brain_db_selenium TO postgres_selenium;
```

Make sure the database connection settings in `settings.py` are correct.

---

##  Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Usage

All commands must be executed from the directory containing `manage.py`.

---

### 1. Run the Selenium parser

Opens a browser, searches for a product (e.g. *iPhone 15*), collects data, and saves it to the database.

```bash
python manage.py selenium_parse
```

Command file:
```
Selenium_parser_prod/management/commands/selenium_parse.py
```

---

### 2. Export data to CSV

Fetches data from the database and creates `brain_products.csv` in the project root.

```bash
python manage.py export_to_csv
```

Command file:
```
Selenium_parser_prod/management/commands/export_to_csv.py
```


##  Project Structure

```
Parser_selenium/
│
├── manage.py
│
├── Parser_selenium/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── Selenium_parser_prod/
│   ├── models.py
│   ├── services/
│   │   ├── parser.py
│   │   └── exportFile_to_csv.py
│   │
│   └── management/
│       └── commands/
│           ├── selenium_parse.py
│           └── export_to_csv.py
│
└── brain_products.csv
```
