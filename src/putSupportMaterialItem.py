
import requests

def putSupportMaterialItem(
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
    headers = None
):
    final_path = "/support_materials/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "id": body_id}, "name": body_name}
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

    