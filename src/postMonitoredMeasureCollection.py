
import requests

def postMonitoredMeasureCollection(
    host
    
    
    # Body parameters
       , 
        body_measurement, body_dateTime, body_magnetude, body_unit, body_id
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "measurement": body_measurement, "dateTime": body_dateTime, "magnetude": body_magnetude, "unit": body_unit, "id": body_id
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

    