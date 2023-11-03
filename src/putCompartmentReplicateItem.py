
import requests

def putCompartmentReplicateItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_compartment, body_reactorReplicate, body_slug, body_reactorSlug, body_compartmentSlug, body_displayName, body_longSlug, body_parentSlug, body_parentId, body_events, body_project, body_monitoredMeasureTypes, body_measurements, body_id
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "/compartment_replicates/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "compartment": body_compartment, "reactorReplicate": body_reactorReplicate, "slug": body_slug, "reactorSlug": body_reactorSlug, "compartmentSlug": body_compartmentSlug, "displayName": body_displayName, "longSlug": body_longSlug, "parentSlug": body_parentSlug, "parentId": body_parentId, "events": body_events, "project": body_project, "monitoredMeasureTypes": body_monitoredMeasureTypes, "measurements": body_measurements, "id": body_id
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

    