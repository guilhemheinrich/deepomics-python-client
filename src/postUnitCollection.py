
import requests

def postUnitCollection(
    host
    
    
    # Body parameters
       , 
        body_symbol, body_measureTypes, body_id, body_name, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "symbol": body_symbol}, "measureTypes": body_measureTypes}, "id": body_id}, "name": body_name}, "slug": body_slug}
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

    