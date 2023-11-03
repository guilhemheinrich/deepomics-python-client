
import requests

def putSupportItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_material, body_type, body_id, body_measures
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "/supports/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "material": body_material, "type": body_type, "id": body_id, "measures": body_measures
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

    