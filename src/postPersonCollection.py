
import requests

def postPersonCollection(
    host
    
    
    # Body parameters
       , 
        body_displayName, body_firstname, body_lastname, body_email, body_phoneNumber, body_slug, body_id
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "displayName": body_displayName, "firstname": body_firstname, "lastname": body_lastname, "email": body_email, "phoneNumber": body_phoneNumber, "slug": body_slug, "id": body_id
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

    