
import requests

def postLeachateCollection(
    host
    
    
    # Body parameters
       , 
        body_id, body_measures
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "id": body_id}, "measures": body_measures}
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

    