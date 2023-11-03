
import requests

def putStandardOperatingProcedureItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_canDelete, body_document, body_project, body_linkOrDOIOrDocumentNotNull, body_onlyUrlOrDOIO, body_comments, body_doi, body_url, body_id, body_name, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "/standard_operating_procedures/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "canDelete": body_canDelete, "document": body_document, "project": body_project, "linkOrDOIOrDocumentNotNull": body_linkOrDOIOrDocumentNotNull, "onlyUrlOrDOIO": body_onlyUrlOrDOIO, "comments": body_comments, "doi": body_doi, "url": body_url, "id": body_id, "name": body_name, "slug": body_slug
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

    