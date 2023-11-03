
import requests

def putMixingItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_type, body_speedCategory, body_id, body_measures
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "/mixings/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "type": body_type, "speedCategory": body_speedCategory, "id": body_id, "measures": body_measures
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

    