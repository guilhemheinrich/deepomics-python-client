
import requests

def postPermissionCollection(
    host
    
    
    # Body parameters
       , 
        body_id, body_iri, body_action, body_isGranted
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "id": body_id, "iri": body_iri, "action": body_action, "isGranted": body_isGranted
    }
    json_content = {
        **optional_json_content,
        **required_body_content           
    }
    
    response = requests.post(
        url = host + final_path,
        headers = headers,
        json = json_content           
    )

    return response

    