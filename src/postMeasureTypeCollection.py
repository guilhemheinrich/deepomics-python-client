
import requests

def postMeasureTypeCollection(
    host
    
    
    # Body parameters
       , 
        body_allowedUnits, body_defaultUnit, body_category, body_tags, body_withUnit, body_id, body_name, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "allowedUnits": body_allowedUnits}, "defaultUnit": body_defaultUnit}, "category": body_category}, "tags": body_tags}, "withUnit": body_withUnit}, "id": body_id}, "name": body_name}, "slug": body_slug}
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

    