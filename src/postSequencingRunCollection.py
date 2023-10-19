
import requests

def postSequencingRunCollection(
    host
    
    
    # Body parameters
       , 
        body_samples, body_sequencer, body_status, body_run, body_date, body_user, body_sequencingProcedure, body_project, body_files, body_sequencingProcedureDisplaySlug, body_sequencerDisplayName, body_userDisplayName, body_samplesCount, body_id
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "samples": body_samples}, "sequencer": body_sequencer}, "status": body_status}, "run": body_run}, "date": body_date}, "user": body_user}, "sequencingProcedure": body_sequencingProcedure}, "project": body_project}, "files": body_files}, "sequencingProcedureDisplaySlug": body_sequencingProcedureDisplaySlug}, "sequencerDisplayName": body_sequencerDisplayName}, "userDisplayName": body_userDisplayName}, "samplesCount": body_samplesCount}, "id": body_id}
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

    