
import requests

def postSoftwareCollection(
    host
    
    
    # Body parameters
       , 
        body_softwareName, body_displaySoftwareName, body_version, body_parameters, body_id, body_name, body_project, body_status, body_correctStatusAndProject, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "softwareName": body_softwareName}, "displaySoftwareName": body_displaySoftwareName}, "version": body_version}, "parameters": body_parameters}, "id": body_id}, "name": body_name}, "project": body_project}, "status": body_status}, "correctStatusAndProject": body_correctStatusAndProject}, "slug": body_slug}
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

    