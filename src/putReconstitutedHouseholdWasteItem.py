
import requests

def putReconstitutedHouseholdWasteItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_referenceName, body_recipe, body_descriptionForSample, body_inputCategory, body_project, body_samples, body_documents, body_slugForSample, body_comments, body_id, body_measures, body_name, body_modecoms, body_year
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "/reconstituted_household_wastes/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "referenceName": body_referenceName}, "recipe": body_recipe}, "descriptionForSample": body_descriptionForSample}, "inputCategory": body_inputCategory}, "project": body_project}, "samples": body_samples}, "documents": body_documents}, "slugForSample": body_slugForSample}, "comments": body_comments}, "id": body_id}, "measures": body_measures}, "name": body_name}, "modecoms": body_modecoms}, "year": body_year}
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

    