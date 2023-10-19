
import requests

def putReactorItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_experimentalSeries, body_operation, body_compartments, body_project, body_dimensions, body_containerShape, body_membranes, body_typeOfOperation, body_allLocations, body_replicates, body_measurements, body_canDelete, body_comments, body_id, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "/reactors/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "experimentalSeries": body_experimentalSeries}, "operation": body_operation}, "compartments": body_compartments}, "project": body_project}, "dimensions": body_dimensions}, "containerShape": body_containerShape}, "membranes": body_membranes}, "typeOfOperation": body_typeOfOperation}, "allLocations": body_allLocations}, "replicates": body_replicates}, "measurements": body_measurements}, "canDelete": body_canDelete}, "comments": body_comments}, "id": body_id}, "slug": body_slug}
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

    