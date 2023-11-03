
import requests

def uploadFileItem(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "/files/{id}".format(
        id = path_id
    )
    
    
    json_content = {
        **optional_json_content           
    }
    
    response = requests.patch(
        url = host + final_path,
        headers = headers,
        json = json_content           
    )

    return response

    