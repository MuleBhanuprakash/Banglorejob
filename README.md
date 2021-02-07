Instuctions to this project

step1
  download or clone this project into local system

step 2
  install all dependencies as mentioned in requirements.txt
    pip install requirements.txt
step 3
  run commands in terminal
     py manage.py makemigrations                # for creating tables for models
     py manage.py migrate                       # for creating necessary tables required for our project
     py manage.py sql migrate app1 001          # for importing our models into the Database sqlite3
step 4
  create a super user and provide details as required
    py manage.py createsuperuser
step 5
  run the server locally
    py manage.py runserver
step 6
   After the you directed to home.html page in this you can upload your excel file as you required. I provide a sample file in the directory level as AddressSample.xlsx
   you should upload thgis file and you can see on Admin panel
step 6
  now you enter or type the view as i mentioned in the project( t http://127.0.0.1:8000/export) to download updated file
step 7
you can go to the downloaded folder and you can able to see updated file

Please Remember:
      in models.py you can enter your API key in the api key field and use  GOOGLE Geocode to get the coordinates
  
 
