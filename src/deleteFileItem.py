
import requests

def deleteFileItem(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    # Headers
    headers = None
):
    final_path = "/files/{id}".format(
        id = path_id
    )
    
    
    
    response = requests.delete(
        url = host + final_path,
        headers = headers           
    )

    return response

    