## Please follow the steps below to run my portfolio on your computer

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/natalja-tomasevica/portfolio.git
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

4. **Generate a Django `SECRET_KEY`:**

    ```bash
    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
    ```

5. **Create an `.env` file:**

    Create `.env` file and fill in the required values.

    Replace placeholders with actual values; example:

    ```ini
    # Django settings
    SECRET_KEY='your_secret_key'
    ```

6. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```
