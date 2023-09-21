from dotenv import load_dotenv
load_dotenv()

try:
    from API import (app,
                     api,
                     ScrapperController,
                     docs
                     )
except Exception as e:
    print("Modules are Missing : {} ".format(e))

scrapper_controller = ScrapperController()

api.add_resource(scrapper_controller, '/scrapper', endpoint='scrappercontroller')
docs.register(ScrapperController)