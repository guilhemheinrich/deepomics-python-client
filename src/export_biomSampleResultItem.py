
import requests

def export_biomSampleResultItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_sequencingSample, body_displaySequencingSample, body_displaySample, body_metabarcodingBioinformaticRun, body_displayMetabarcodingBioinformaticRun, body_displayBioinformaticWorkflow, body_annotations, body_numberOfRawReads, body_postProcessReads, body_numberOfASV, body_totalAnnotationCount, body_id
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "/project/{id}/bioinfo/bio_sample_results/export/biom".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "sequencingSample": body_sequencingSample, "displaySequencingSample": body_displaySequencingSample, "displaySample": body_displaySample, "metabarcodingBioinformaticRun": body_metabarcodingBioinformaticRun, "displayMetabarcodingBioinformaticRun": body_displayMetabarcodingBioinformaticRun, "displayBioinformaticWorkflow": body_displayBioinformaticWorkflow, "annotations": body_annotations, "numberOfRawReads": body_numberOfRawReads, "postProcessReads": body_postProcessReads, "numberOfASV": body_numberOfASV, "totalAnnotationCount": body_totalAnnotationCount, "id": body_id
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

    