
import requests

def putMeasureTypeItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_allowedUnits, body_defaultUnit, body_category, body_tags, body_withUnit, body_id, body_name, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "/measure_types/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "allowedUnits": body_allowedUnits, "defaultUnit": body_defaultUnit, "category": body_category, "tags": body_tags, "withUnit": body_withUnit, "id": body_id, "name": body_name, "slug": body_slug
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

    