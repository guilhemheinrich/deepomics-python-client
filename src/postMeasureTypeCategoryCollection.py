
import requests

def postMeasureTypeCategoryCollection(
    host
    
    
    # Body parameters
       , 
        body_children, body_parent, body_types, body_ancestry, body_id, body_name
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "children": body_children, "parent": body_parent, "types": body_types, "ancestry": body_ancestry, "id": body_id, "name": body_name
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

    