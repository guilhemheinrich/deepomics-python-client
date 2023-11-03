
import requests

def postBioinformaticWorkflowProcedureCollection(
    host
    
    
    # Body parameters
       , 
        body_document, body_displayDocument, body_canDelete, body_linkOrDOIOrDocumentNotNull, body_onlyUrlOrDOIO, body_comments, body_doi, body_id, body_name, body_project, body_status, body_correctStatusAndProject, body_slug, body_url
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "document": body_document, "displayDocument": body_displayDocument, "canDelete": body_canDelete, "linkOrDOIOrDocumentNotNull": body_linkOrDOIOrDocumentNotNull, "onlyUrlOrDOIO": body_onlyUrlOrDOIO, "comments": body_comments, "doi": body_doi, "id": body_id, "name": body_name, "project": body_project, "status": body_status, "correctStatusAndProject": body_correctStatusAndProject, "slug": body_slug, "url": body_url
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

    