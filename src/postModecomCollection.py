
import requests

def postModecomCollection(
    host
    
    
    # Body parameters
       , 
        body_type, body_percent, body_id
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "type": body_type}, "percent": body_percent}, "id": body_id}
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

    