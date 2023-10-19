
import requests

def putAerationItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_systemType, body_comments, body_id, body_measures
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "/aerations/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "systemType": body_systemType}, "comments": body_comments}, "id": body_id}, "measures": body_measures}
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

    