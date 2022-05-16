# Django Data Conversion

A webapp that receives a .txt file through a form and parse/save the data into a PostgreSQL database. Made using Django 3.2.

To run on Docker, you need to have Docker Desktop installed. Once you have it, execute the following commands on CMD:
    - docker compose up --build (build up the container)
    - docker compose down (shut down the server)
    - docker compose exec web python manage.py migrate (do the migrations)
    - docker compose up (the project is live at your localhost)

