
import requests

def postMembraneCollection(
    host
    
    
    # Body parameters
       , 
        body_type, body_displayType, body_startUpDate, body_reactor, body_compartementLeft, body_compartementRight, body_reference, body_id, body_measures
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "type": body_type, "displayType": body_displayType, "startUpDate": body_startUpDate, "reactor": body_reactor, "compartementLeft": body_compartementLeft, "compartementRight": body_compartementRight, "reference": body_reference, "id": body_id, "measures": body_measures
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

    