import random
import azure.functions as func
import string

def main(req: func.HttpRequest) -> func.HttpResponse:
    
    randomlist = []
    for i in range(0,5):
        n = random.choice(string.ascii_letters)
        randomlist.append(n)

    return_str = ''.join(randomlist)



    return func.HttpResponse(return_str, status_code=200)
