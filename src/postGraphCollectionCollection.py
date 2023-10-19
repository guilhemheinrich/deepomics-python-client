
import requests

def postGraphCollectionCollection(
    host
    
    
    # Body parameters
       , 
        body_graphs, body_operation, body_id, body_name
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "graphs": body_graphs}, "operation": body_operation}, "id": body_id}, "name": body_name}
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

    