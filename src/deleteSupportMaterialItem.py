
import requests

def deleteSupportMaterialItem(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    # Headers
    headers = None
):
    final_path = "/support_materials/{id}".format(
        id = path_id
    )
    
    
    
    response = requests.delete(
        url = host + final_path,
        headers = headers           
    )

    return response

    