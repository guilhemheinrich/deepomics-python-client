
import requests

def postMeasureTypeTagCollection(
    host
    
    
    # Body parameters
       , 
        body_measureTypes, body_id, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "measureTypes": body_measureTypes, "id": body_id, "slug": body_slug
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

    