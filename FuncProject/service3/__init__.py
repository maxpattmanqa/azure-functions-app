
import random
import azure.functions as func
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    randomlist = []
    for i in range(0,5):
        n = random.randint(0,9)
        randomlist.append(str(n))

    return_str = ''.join(randomlist)
    return func.HttpResponse(return_str,status_code=200)
