
import requests

def putPcrConditionsItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_project, body_canDelete, body_id, body_measures, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "/pcr_conditions/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "project": body_project, "canDelete": body_canDelete, "id": body_id, "measures": body_measures, "slug": body_slug
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

    