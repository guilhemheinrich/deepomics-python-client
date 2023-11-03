
import requests

def putUnitItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_symbol, body_measureTypes, body_id, body_name, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "/units/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "symbol": body_symbol, "measureTypes": body_measureTypes, "id": body_id, "name": body_name, "slug": body_slug
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

    