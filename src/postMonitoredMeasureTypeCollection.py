
import requests

def postMonitoredMeasureTypeCollection(
    host
    
    
    # Body parameters
       , 
        body_type, body_unit, body_locations, body_measurements, body_operation, body_label, body_slug, body_symbolUnit, body_withUnit, body_defaultUnit, body_id
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "type": body_type, "unit": body_unit, "locations": body_locations, "measurements": body_measurements, "operation": body_operation, "label": body_label, "slug": body_slug, "symbolUnit": body_symbolUnit, "withUnit": body_withUnit, "defaultUnit": body_defaultUnit, "id": body_id
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

    