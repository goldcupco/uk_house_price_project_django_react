
start the venv:
cd new_venv_311
source ./bin/activate
cd ..

in the backend directory :

Clone the repository to your local machine
git clone  https://github.com/goldcupco/uk_house_price_project_django_react.git

Navigate to the project directory


Set up a virtual environment for Python

Activate the virtual environment


Install the required Python packages by running:
text
pip install -r requirements.txt

Navigate to the backend directory

Run database migrations:
python manage.py migrate

Start the Django development server:

python manage.py runserver