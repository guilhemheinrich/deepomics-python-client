
import requests

def getReconstituedReferenceNameItem(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    headers = None
):
    final_path = "/reconstitued_reference_names/{id}".format(
        id = path_id
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    