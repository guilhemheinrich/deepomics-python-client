
import requests

def postMetabarcodingBioinformaticRunCollection(
    host
    
    
    # Body parameters
       , 
        body_sequencingSamples, body_project, body_bioinformaticWorkflow, body_displayBioinformaticWorkflow, body_biomFile, body_metricsFile, body_nwkFile, body_logFiles, body_metricsFileReport, body_biomFileReport, body_canDelete, body_comments, body_id, body_name, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "sequencingSamples": body_sequencingSamples, "project": body_project, "bioinformaticWorkflow": body_bioinformaticWorkflow, "displayBioinformaticWorkflow": body_displayBioinformaticWorkflow, "biomFile": body_biomFile, "metricsFile": body_metricsFile, "nwkFile": body_nwkFile, "logFiles": body_logFiles, "metricsFileReport": body_metricsFileReport, "biomFileReport": body_biomFileReport, "canDelete": body_canDelete, "comments": body_comments, "id": body_id, "name": body_name, "slug": body_slug
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

    