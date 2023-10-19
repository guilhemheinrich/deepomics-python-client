
import requests

def postNucleicAcidExtractionProcedureCollection(
    host
    
    
    # Body parameters
       , 
        body_canDelete, body_document, body_project, body_linkOrDOIOrDocumentNotNull, body_onlyUrlOrDOIO, body_comments, body_doi, body_url, body_id, body_name, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "canDelete": body_canDelete}, "document": body_document}, "project": body_project}, "linkOrDOIOrDocumentNotNull": body_linkOrDOIOrDocumentNotNull}, "onlyUrlOrDOIO": body_onlyUrlOrDOIO}, "comments": body_comments}, "doi": body_doi}, "url": body_url}, "id": body_id}, "name": body_name}, "slug": body_slug}
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

    