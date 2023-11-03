
import requests

def putTemperatureCategoryItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_id, body_name
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "/temperature_categories/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "id": body_id, "name": body_name
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

    