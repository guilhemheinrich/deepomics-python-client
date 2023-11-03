
import requests

def putMultiplexIdentifierItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_sequencingSampleComplement, body_sequence, body_id, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "/multiplex_identifiers/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "sequencingSampleComplement": body_sequencingSampleComplement, "sequence": body_sequence, "id": body_id, "slug": body_slug
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

    