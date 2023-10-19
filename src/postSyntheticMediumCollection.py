
import requests

def postSyntheticMediumCollection(
    host
    
    
    # Body parameters
       , 
        body_ph, body_carbonateAdded, body_genericName, body_recipe, body_descriptionForSample, body_inputCategory, body_project, body_samples, body_documents, body_slugForSample, body_comments, body_id, body_measures, body_name
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "ph": body_ph}, "carbonateAdded": body_carbonateAdded}, "genericName": body_genericName}, "recipe": body_recipe}, "descriptionForSample": body_descriptionForSample}, "inputCategory": body_inputCategory}, "project": body_project}, "samples": body_samples}, "documents": body_documents}, "slugForSample": body_slugForSample}, "comments": body_comments}, "id": body_id}, "measures": body_measures}, "name": body_name}
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

    