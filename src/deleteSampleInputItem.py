
import requests

def deleteSampleInputItem(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    # Headers
    headers = None
):
    final_path = "/sample_inputs/{id}".format(
        id = path_id
    )
    
    
    
    response = requests.delete(
        url = host + final_path,
        headers = headers           
    )

    return response

    