
import requests

def postRealResidualHouseholdWasteCollection(
    host
    
    
    # Body parameters
       , 
        body_descriptionForSample, body_inputCategory, body_project, body_samples, body_documents, body_slugForSample, body_comments, body_id, body_measures, body_name, body_city, body_collectionDate, body_country, body_companyName, body_companyActivity, body_modecoms, body_year
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "descriptionForSample": body_descriptionForSample, "inputCategory": body_inputCategory, "project": body_project, "samples": body_samples, "documents": body_documents, "slugForSample": body_slugForSample, "comments": body_comments, "id": body_id, "measures": body_measures, "name": body_name, "city": body_city, "collectionDate": body_collectionDate, "country": body_country, "companyName": body_companyName, "companyActivity": body_companyActivity, "modecoms": body_modecoms, "year": body_year
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

    