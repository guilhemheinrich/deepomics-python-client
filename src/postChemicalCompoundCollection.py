
import requests

def postChemicalCompoundCollection(
    host
    
    
    # Body parameters
       , 
        body_state, body_purity, body_grade, body_brand, body_linearFormula, body_linearFormulaIsotope, body_cas, body_descriptionForSample, body_inputCategory, body_project, body_samples, body_documents, body_slugForSample, body_comments, body_id, body_measures, body_name, body_labeledElements, body_labeledElementForSample
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "state": body_state}, "purity": body_purity}, "grade": body_grade}, "brand": body_brand}, "linearFormula": body_linearFormula}, "linearFormulaIsotope": body_linearFormulaIsotope}, "cas": body_cas}, "descriptionForSample": body_descriptionForSample}, "inputCategory": body_inputCategory}, "project": body_project}, "samples": body_samples}, "documents": body_documents}, "slugForSample": body_slugForSample}, "comments": body_comments}, "id": body_id}, "measures": body_measures}, "name": body_name}, "labeledElements": body_labeledElements}, "labeledElementForSample": body_labeledElementForSample}
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

    