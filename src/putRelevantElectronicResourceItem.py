
import requests

def putRelevantElectronicResourceItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_project, body_canDelete, body_comments, body_id, body_name, body_slug, body_urlOrDoiNotNull, body_doi, body_url
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "/relevant_electronic_resources/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "project": body_project}, "canDelete": body_canDelete}, "comments": body_comments}, "id": body_id}, "name": body_name}, "slug": body_slug}, "urlOrDoiNotNull": body_urlOrDoiNotNull}, "doi": body_doi}, "url": body_url}
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

    