# With You API


## Girls in Tech Hackathon 2020: Create Tech Solutions to Unify Against Breast Cancer

An API for the With You application.

"With You is a project that hopes to accompany you during the process of getting appointments, diagnosis and treatment for breast cancer.

Let's find together an specialist or clinic near you, while giving you support against systemic racism and discrimination.

Our purpose is to make you feel secure, visible and respected."

## Setup Instructions:

### In your terminal:
- Clone down repository: `git clone git@github.com:sampita/withyouAPI.git`
- `cd` into the project folder
- Create a virtual environment (A virtual environment allows you to install packages in the scope of this project without polluting global, system package installations):
   ```
   python -m venv WithYouEnv
   source ./WithYouEnv/bin/activate
   ```
- Use pip to install all of the packages needed for this project:
   `pip install -r requirements.txt`
- Create the Django table: `python manage.py migrate`
- Run the server: `python manage.py runserver`
- If you now go to your browser, type in `http://127.0.0.1:8000/` and hit Enter, you should see a page with *Django Rest Framework* at the top followed by:
   ```
   GET /
   HTTP 200 OK
   Allow: GET, HEAD, OPTIONS
   Content-Type: application/json
   Vary: Accept
   
   {}
   ```

### Database Management

You can use whichever tool you prefer, but to test the database while in development I used the free cross-platform tool [TablePlus](https://tableplus.com/).

To get setup with TablePlus:
- Open TablePlus
- Click 'Create New Connection'
- Select SQLite
- Give a name to your connection (It can be anything-- I just used "withyou")
- Select the database file you want to connect to (Project Folder > db.sqlite3)
- Click "Connect" and you should see all the tables, including the built-in Django REST tables (beginning with "django_") and the WithYou tables (beginning with "withyouapi_")

____________

### Link to the With You front-end repository: https://github.com/gabiguarini/withyouapp
