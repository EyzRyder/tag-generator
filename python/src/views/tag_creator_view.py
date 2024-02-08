from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse


class TagCreaterView:
    '''
    responsability for interacting with HTTP

    '''

    def validate_and_creat(self,http_request:HttpRequest) -> HttpResponse:
        body: http_request.body
        pruduct_code = body["product_code"]

        print('View')

        return HttpResponse(status_code=200,body={"Name":"DOe"})
