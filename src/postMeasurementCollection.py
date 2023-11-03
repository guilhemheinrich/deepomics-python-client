
import requests

def postMeasurementCollection(
    host
    
    
    # Body parameters
       , 
        body_location, body_project, body_operators, body_type, body_unit, body_monitoredMeasures, body_id
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "location": body_location, "project": body_project, "operators": body_operators, "type": body_type, "unit": body_unit, "monitoredMeasures": body_monitoredMeasures, "id": body_id
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

    