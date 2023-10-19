
import requests

def putMeasureTypeCategoryItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_children, body_parent, body_types, body_ancestry, body_id, body_name
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "/measure_type_categories/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "children": body_children}, "parent": body_parent}, "types": body_types}, "ancestry": body_ancestry}, "id": body_id}, "name": body_name}
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

    