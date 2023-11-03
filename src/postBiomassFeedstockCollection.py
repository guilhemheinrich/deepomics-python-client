
import requests

def postBiomassFeedstockCollection(
    host
    
    
    # Body parameters
       , 
        body_nativeBiomassTypes, body_commonName, body_scientificName, body_residueTypes, body_infoBiomass, body_taxidGenus, body_taxidStrainOrSpecies, body_descriptionForSample, body_inputCategory, body_project, body_samples, body_documents, body_slugForSample, body_comments, body_id, body_measures, body_name, body_labeledElements, body_labeledElementForSample
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "nativeBiomassTypes": body_nativeBiomassTypes, "commonName": body_commonName, "scientificName": body_scientificName, "residueTypes": body_residueTypes, "infoBiomass": body_infoBiomass, "taxidGenus": body_taxidGenus, "taxidStrainOrSpecies": body_taxidStrainOrSpecies, "descriptionForSample": body_descriptionForSample, "inputCategory": body_inputCategory, "project": body_project, "samples": body_samples, "documents": body_documents, "slugForSample": body_slugForSample, "comments": body_comments, "id": body_id, "measures": body_measures, "name": body_name, "labeledElements": body_labeledElements, "labeledElementForSample": body_labeledElementForSample
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

    