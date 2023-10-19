
import requests

def putPhysicalStateItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_id, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "/physical_states/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "id": body_id}, "slug": body_slug}
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

    