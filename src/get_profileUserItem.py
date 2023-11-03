
import requests

def get_profileUserItem(
    host
    # Path parameters
       , 
        path_subject
       
    
    
    ,
    # Headers
    headers = None
):
    final_path = "/users/myself".format(
        subject = path_subject
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    