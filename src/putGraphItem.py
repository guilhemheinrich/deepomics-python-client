
import requests

def putGraphItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_monitoredMeasureTypes, body_locations, body_graphCollection, body_operation, body_id, body_name
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "/graphs/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "monitoredMeasureTypes": body_monitoredMeasureTypes, "locations": body_locations, "graphCollection": body_graphCollection, "operation": body_operation, "id": body_id, "name": body_name
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

    