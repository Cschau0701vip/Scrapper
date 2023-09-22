# from dotenv import load_dotenv
# load_dotenv()

try:
    from flask import Blueprint
    from flask_restplus import Api
    from API.ScrapperNamespace import api as ns1
    
    # from API import (app,
    #                  api,
    #                  ScrapperController,
    #                  docs
    #                  )
except Exception as e:
    print("Modules are Missing : {} ".format(e))

blueprint = Blueprint('main', __name__)

main = Api(blueprint)

main.add_namespace(ns1)

# scrapper_controller = ScrapperController()

# api.add_resource(scrapper_controller, '/scrapper', endpoint='scrappercontroller')
# docs.register(ScrapperController)