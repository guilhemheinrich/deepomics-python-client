
import requests

def postOperationCollection(
    host
    
    
    # Body parameters
       , 
        body_launchDate, body_monitoredMeasureTypes, body_samples, body_summary, body_operators, body_operatorsDisplayName, body_referent, body_referentDisplayName, body_graphCollection, body_schemes, body_procedures, body_data, body_documents, body_allLocations, body_project, body_measurements, body_comments, body_id, body_name, body_slug, body_tags, body_tagsName
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "launchDate": body_launchDate}, "monitoredMeasureTypes": body_monitoredMeasureTypes}, "samples": body_samples}, "summary": body_summary}, "operators": body_operators}, "operatorsDisplayName": body_operatorsDisplayName}, "referent": body_referent}, "referentDisplayName": body_referentDisplayName}, "graphCollection": body_graphCollection}, "schemes": body_schemes}, "procedures": body_procedures}, "data": body_data}, "documents": body_documents}, "allLocations": body_allLocations}, "project": body_project}, "measurements": body_measurements}, "comments": body_comments}, "id": body_id}, "name": body_name}, "slug": body_slug}, "tags": body_tags}, "tagsName": body_tagsName}
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

    