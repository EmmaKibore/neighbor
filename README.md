# Neighborhood
This is an application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meetingS, announcements or even alerts.

## App
![Screenshot from 2019-06-06 09-42-37](https://user-images.githubusercontent.com/47333363/59012779-0afb3d80-8841-11e9-9309-0555c396fc8e.png)

![Screenshot from 2019-06-06 09-42-49](https://user-images.githubusercontent.com/47333363/59012880-4e55ac00-8841-11e9-8049-47af1ddae491.png)

## User stories
The user should be able to:

Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Prerequisites
 Python3.6

## Installation
To install, follow the following instructions;

    $ git clone https://github.com/EmmaKibore/neighbor.git
    $ cd HoodWatch
    $ source virtual/bin/activate
    Install all the necessary requirements by running pip install -r requirements.txt (Python 3.6).
    $ ./manager.py runserver

## How to Prepare enviroment variables
Since one needs a virtual enviroment, Create a virtual file and add the following configutions to it

    SECRET_KEY= #secret key will be added by default
    DEBUG= #set to false in production
    DB_NAME= #database name
    DB_USER= #database user
    DB_PASSWORD=#database password
    DB_HOST="127.0.0.1"
    MODE= # dev or prod , set to prod during production
    ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'


## Technologies used
Python3.6
Django 1.11
Heroku
Bootstrap

## License (MIT License)
This project is licensed under the MIT Open Source license, (c) Emma Kibore    