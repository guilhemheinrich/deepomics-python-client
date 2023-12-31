
import requests

def postTagCollection(
    host
    
    
    # Body parameters
       , 
        body_deprecated, body_isDeprecated, body_id, body_name, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "deprecated": body_deprecated, "isDeprecated": body_isDeprecated, "id": body_id, "name": body_name, "slug": body_slug
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

    