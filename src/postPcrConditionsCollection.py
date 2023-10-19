
import requests

def postPcrConditionsCollection(
    host
    
    
    # Body parameters
       , 
        body_project, body_canDelete, body_id, body_measures, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "project": body_project}, "canDelete": body_canDelete}, "id": body_id}, "measures": body_measures}, "slug": body_slug}
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

    