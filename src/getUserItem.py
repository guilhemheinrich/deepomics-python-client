
import requests

def getUserItem(
    host
    # Path parameters
       , 
        path_subject
       
    
    
    ,
    headers = None
):
    final_path = "/users/{subject}".format(
        subject = path_subject
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    