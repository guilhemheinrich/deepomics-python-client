
import requests

def putModecomItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_type, body_percent, body_id
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "/modecoms/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "type": body_type}, "percent": body_percent}, "id": body_id}
    }
    json_content = {
        **optional_json_content,
        **required_body_content           
    }
    
    response = requests.put(
        url = host + final_path,
        headers = headers,
        json = json_content           
    )

    return response

    