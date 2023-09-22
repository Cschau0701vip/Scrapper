from flask_restplus import Namespace


try:
    from flask import request, jsonify, Response
    from flask_apispec import use_kwargs, doc
    from marshmallow import fields
    from flask_restful import Resource
    from flask_apispec.views import MethodResource
    from Services.filtration_scrapper import compare_and_flag_urls
    print("All imports are ok............")
except Exception as e:
    print("Error: {} ".format(e))
    
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}
api = Namespace('scrapper', authorizations=authorizations)

scrapper_request = api.model('scrapper_request', {
    "providerSignature": fields.String('Provider Signature'),
    "dealerUrlsList": fields.String('Dealer URLs List')
})

@api.route('/scrapper')
class ScrapperController(MethodResource, Resource):
    @doc(description='This is health check endpoint', tags=['Health Endpoint'])
    def get(self):
        _ = {'message': 'APIs are working fine'}
        print(str(_))
        return _
    
    # @doc(description='This is download output file endpoint', tags=['Scrapper Endpoint'])
    # def get(self, id):
    #     with open(f"export_dataframe{id}.csv") as fp:
    #         csv = fp.read()
    #     return Response(
    #         csv,
    #         mimetype="text/csv",
    #         headers={"Content-disposition": f"attachment; filename=export_dataframe{id}.csv"})

    # @use_kwargs({'providerSignature': fields.Str(), 'dealerUrlsList': fields.Str()})
    @api.expect(scrapper_request)
    @doc(description='This is Scrapper endpoint. It requires api-key as header parameter to authenticate serp api.', tags=['Scrapper Endpoint'])
    def post(self, **kwargs):
        response = {
            "success": False,
            "error": None,
            "data": None,
            "status_code": None
        }
        if request.data:
            data = request.get_json()
            api_key = request.headers.get('api-key')
            provider_signature = data.get('providerSignature')
            dealer_urls_list = data.get('dealerUrlsList')

            if provider_signature and dealer_urls_list:
                results = compare_and_flag_urls(provider_signature, dealer_urls_list, api_key)
                response["data"] = results
                response["success"] = True
                response["status_code"] = 200
            else:
                response["error"] = "Invalid request data"
                response["status_code"] = 400
        else:
            response["error"] = "Request must be JSON"
            response["status_code"] = 415

        return jsonify(response)
