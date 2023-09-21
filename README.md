<!-- python3 -m venv venv
. venv/bin/activate

pip install -r requirements.txt

export FLASK_APP=main.py
export FLASK_ENV=development
flask run

deactivate -->

## TO run locally
`gunicorn --bind 0.0.0.0:8080 app:app`

## To run locally using docker image 
`docker run --name flask-app -p 8080:8080 flask-app:v1`

## Build docker image
`docker build --platform=linux/amd64 -t flask-app:v1 .`
