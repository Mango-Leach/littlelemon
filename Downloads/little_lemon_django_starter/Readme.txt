Little Lemon Django REST Framework - Starter Scaffold

IMPORTANT
This is a learning scaffold, not a finished capstone submission. Complete all TODOs,
run the tests, verify the MySQL connection, and ensure you understand your code before
submitting. Follow your course's honor code.

SETUP (Windows PowerShell)
1. Create and activate a virtual environment:
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1

2. Install dependencies:
   pip install -r requirements.txt

3. (Optional local scaffold) Run with SQLite:
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver

4. To use MySQL, create a database, then set environment variables before running:
   $env:DB_NAME="littlelemon"
   $env:DB_USER="root"
   $env:DB_PASSWORD="your_mysql_password"
   $env:DB_HOST="127.0.0.1"
   $env:DB_PORT="3306"
   Then run migrations.

API PATHS FOR PEER REVIEW
GET/POST       /api/menu/
GET/PUT/PATCH/DELETE /api/menu/<id>/
GET/POST       /api/bookings/
GET/PUT/PATCH/DELETE /api/bookings/<id>/
POST           /api/users/     (registration: TODO)
POST           /api/token/     (token issue: TODO)
GET            /api-auth/login/ (DRF browsable API login)

AUTHENTICATION
Booking endpoints require authentication. Implement registration and token issuance
in restaurant/views.py, then test using Insomnia with:
Authorization: Token <your_token>

TODO CHECKLIST
[ ] Implement registration validation and user creation.
[ ] Implement token issuance after validating credentials.
[ ] Set suitable permissions on menu writes.
[ ] Verify booking list visibility and access rules are appropriate.
[ ] Add unit tests for booking CRUD and auth failures/successes.
[ ] Configure and test MySQL, not just SQLite.
[ ] Test GET, POST, PUT/PATCH, DELETE in Insomnia.
[ ] Commit and push this file and all project code to GitHub.
