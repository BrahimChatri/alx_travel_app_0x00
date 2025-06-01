
   # ALX Travel App 0x00

   ## Setup Instructions

   1. **Clone the repository:**

      ```bash
      git clone https://github.com/BrahimChatri/alx_travel_app_0x00.git
      cd alx_travel_app_0x00

   2. **Create and activate a virtual environment:**

      ```bash
      python -m venv env
      source env/bin/activate  # On Windows use `env\Scripts\activate`
      ```

   3. **Install dependencies:**

      ```bash
      pip install -r requirements.txt
      ```

   4. **Apply migrations:**

      ```bash
      python manage.py makemigrations
      python manage.py migrate
      ```

   5. **Seed the database with sample data:**

      ```bash
      python manage.py seed
      ```

   6. **Run the development server:**

      ```bash
      python manage.py runserver
      ```

   ## Project Structure

   * `listings/models.py`: Contains the `Listing`, `Booking`, and `Review` models.
   * `listings/serializers.py`: Serializers for `Listing` and `Booking` models.
   * `listings/management/commands/seed.py`: Custom management command to seed the database with sample data.

   ## Dependencies

   * Django
   * Django REST Framework
   * Faker

   ## License

   This project is licensed under the MIT License.
