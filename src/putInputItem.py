
import requests

def putInputItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_inputCategory, body_project, body_samples, body_documents, body_slugForSample, body_comments, body_id, body_measures, body_name
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "/inputs/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "inputCategory": body_inputCategory}, "project": body_project}, "samples": body_samples}, "documents": body_documents}, "slugForSample": body_slugForSample}, "comments": body_comments}, "id": body_id}, "measures": body_measures}, "name": body_name}
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

    