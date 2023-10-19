
import requests

def putMeasureItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_magnetude, body_type, body_unit, body_id
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "/measures/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "magnetude": body_magnetude}, "type": body_type}, "unit": body_unit}, "id": body_id}
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

    