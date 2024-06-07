# portfolio

## Getting started

### Prerequisites

- Python 3.x
- pip
- virtualenv (optional but recommended)
- MySQL

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/natalja-tomasevica/portfolio.git
    cd portfolio
    ```

2. **Set up a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up MySQL database:**

    - Install MySQL.
    - Create a new database and user:

      ```sql
      CREATE DATABASE database_name;
      CREATE USER 'user_name'@'localhost' IDENTIFIED BY 'password';
      GRANT ALL PRIVILEGES ON database_name.* TO 'user_name'@'localhost';
      ```

5. **Generate a Django `SECRET_KEY`:**

    ```bash
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```

6. **Create an `.env` file:**

    Create `.env` file and fill in the required values.

    Replace placeholders with actual values; example:

    ```ini
    # Django settings
    SECRET_KEY='your_secret_key'
    DEBUG=True

    # Database settings
    DB_NAME='your_db_name'
    DB_USER='your_db_user'
    DB_PASSWORD='your_db_password'
    DB_HOST='your_db_host'
    DB_PORT='1234'

    ALLOWED_HOSTS=localhost, 127.0.0.1
    ```

7. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

8. **Create a superuser (optional):**

    ```bash
    python manage.py createsuperuser
    ```

9. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

Your project should now be running on `http://localhost:8000/`.
