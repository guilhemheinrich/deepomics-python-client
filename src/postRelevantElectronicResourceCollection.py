
import requests

def postRelevantElectronicResourceCollection(
    host
    
    
    # Body parameters
       , 
        body_project, body_canDelete, body_comments, body_id, body_name, body_slug, body_urlOrDoiNotNull, body_doi, body_url
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "project": body_project, "canDelete": body_canDelete, "comments": body_comments, "id": body_id, "name": body_name, "slug": body_slug, "urlOrDoiNotNull": body_urlOrDoiNotNull, "doi": body_doi, "url": body_url
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

    