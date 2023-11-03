
import requests

def putSequencingSampleResultItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_submittedToInsdc, body_accession, body_fileName, body_reverseFileName, body_libReadsSeqd, body_meanRawReadLength, body_correctAccession, body_id
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "/sequencing_sample_results/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "submittedToInsdc": body_submittedToInsdc, "accession": body_accession, "fileName": body_fileName, "reverseFileName": body_reverseFileName, "libReadsSeqd": body_libReadsSeqd, "meanRawReadLength": body_meanRawReadLength, "correctAccession": body_correctAccession, "id": body_id
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

    