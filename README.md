# Hood Watch
Neighborhood watch django application.
This application let's users join neighborhoods listed in it, become a member and can explore different facilities available.

# Requirements
- Python3
- Code editor 
- PostgreSQL
- Understanding of Django

# Setup
Open Vs Code, create a directory and make a directory inside::
```bash
git clone https://github.com/Willbeckh/ubuntu.git 

cd ubuntu

# make env
pipenv shell

pipenv install Pipfile
```

create .env file && set the following config vars for the application


```bash 
DB_USER = <username >
DB_PASSWORD = <password >
DB_HOST = <host >
DB_PORT = <port >
DB_NAME = <dbname >
SECRET_KEY = <secret_key >
MODE = 'dev'

CLOUDINARY_CLOUD_NAME = <cloud_name >
CLOUDINARY_API_KEY = <api_key >
CLOUDINARY_API_SECRET = <api_secret >
```


# Running
Migrate all the db models: 
`./manage.py migrate`

Running the application use:
```sh
./manage.py runserver

# terminal output
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 22, 2022 - 05:42:12
Django version 4.0.4, using settings 'guard_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

### Running Tests
```sh
./manage test
```

# Watching the project
If you track any bug or have an improvement: 
- Open [issue](https://github.com/Willbeckh/ubuntu/issues/new/choose) or a [PR](https://github.com/Willbeckh/ubuntu/compare).


## Author
**Willbeckh** : fullstack developer, a wizard at his craft. 

~made with ❤️ by willbeckh~

🐦 [Twitter](https://twitter.com/billyndirangu)

## Licence
Project license under the MIT free license.
> [MIT](LICENSE)

## cREDITS
To my IDE, stackoverflow, &Technical Mentor