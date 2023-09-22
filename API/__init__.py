try:
    from flask import Flask
    from flask_cors import CORS
    from flask_restful import Api
    from apispec import APISpec
    from apispec.ext.marshmallow import MarshmallowPlugin
    from flask_apispec.extension import FlaskApiSpec
    from API.views import ScrapperController

except Exception as e:
    print("__init Modules are Missing {}".format(e))

app = Flask(__name__)  # Flask app instance initiated
api = Api(app)  # Flask restful wraps Flask app around it.
CORS(app, origins=["*"])
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Scrapper API',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})

docs = FlaskApiSpec(app)