
import requests

def postTemperatureCollection(
    host
    
    
    # Body parameters
       , 
        body_temperatureCategory, body_regulation, body_id, body_measures
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "temperatureCategory": body_temperatureCategory, "regulation": body_regulation, "id": body_id, "measures": body_measures
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

    