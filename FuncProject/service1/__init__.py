import logging
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    string1 = requests.get('https://functionrgapp.azurewebsites.net/api/service2?code=7WuNXHWzaeH0CLVESHo3Z9NKeSzuJf9FlZ4TOdLWLmwyot08cg57OQ==')
    string2 = requests.get('https://functionrgapp.azurewebsites.net/api/service3?code=r4A2e8SdUyroopFBNpb90AxZa5r6qOzDYLONcX1o9LHNvOnGupK87A==')

    a = string1.text.split()
    b = string2.text.split()
    c = ""
    for i in range(len(a)) :
        c += a[i] 
        c += b[i]
    
    if c:
        return func.HttpResponse(f"Hello, new random user name is : {c}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )


#service 2 url = https://functionrgapp.azurewebsites.net/api/service2?code=7WuNXHWzaeH0CLVESHo3Z9NKeSzuJf9FlZ4TOdLWLmwyot08cg57OQ==
# service 3 url =  https://functionrgapp.azurewebsites.net/api/service3?code=r4A2e8SdUyroopFBNpb90AxZa5r6qOzDYLONcX1o9LHNvOnGupK87A==