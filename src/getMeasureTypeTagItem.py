
import requests

def getMeasureTypeTagItem(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    headers = None
):
    final_path = "/measure_type_tags/{id}".format(
        id = path_id
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    