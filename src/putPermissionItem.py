
import requests

def putPermissionItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_id, body_iri, body_action, body_isGranted
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "/permissions/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "id": body_id, "iri": body_iri, "action": body_action, "isGranted": body_isGranted
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

    