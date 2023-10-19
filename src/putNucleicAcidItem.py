
import requests

def putNucleicAcidItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_nucleicAcidDosageMethods, body_displayNucleicAcidDosageMethods, body_nucleicAcidExtractionMethods, body_displayNucleicAcidExtractionMethods, body_nucleicAcidExtraction, body_displayNucleicAcidExtraction, body_id, body_measures
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "/nucleic_acids/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "nucleicAcidDosageMethods": body_nucleicAcidDosageMethods}, "displayNucleicAcidDosageMethods": body_displayNucleicAcidDosageMethods}, "nucleicAcidExtractionMethods": body_nucleicAcidExtractionMethods}, "displayNucleicAcidExtractionMethods": body_displayNucleicAcidExtractionMethods}, "nucleicAcidExtraction": body_nucleicAcidExtraction}, "displayNucleicAcidExtraction": body_displayNucleicAcidExtraction}, "id": body_id}, "measures": body_measures}
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

    