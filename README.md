# IndianBankFinder

IndianBankFinder is a Web Application designed to help people find the Branches of the Bank. It allows user to search by City as well as IFSC code.
The project IndianBankFinder is live on Heroku and can be accessed by this link :
    https://tranquil-spire-92438.herokuapp.com/
    
## Technologies used:
  * Django-REST Framework
  * PostgreSQL Database
  * HTML with Bootstrap4 and JQuery for front-end
  
## Usage:
 * Clone the repository into your machine using "git clone" command.
 * Install virtualenv if not installed already(recommended but optional)
 * Install PostgreSQL into your system if not installed already.
 * Run the command "pip install -r requirements.txt"
 * From PSQL shell, create a new database and dump the "indian_banks.sql" into it.
 * Now , change the "DATABASE" settings from Settings.py
 * Run "python manage.py makemigrations indianbankapp" and "python manage.py migrate" from the command line (You should be in the same folder where manage.py lives)
 * Run "python manage.py runserver"
 * Congratulations! App should be working locally.
