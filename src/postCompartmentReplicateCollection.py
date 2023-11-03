
import requests

def postCompartmentReplicateCollection(
    host
    
    
    # Body parameters
       , 
        body_compartment, body_reactorReplicate, body_slug, body_reactorSlug, body_compartmentSlug, body_displayName, body_longSlug, body_parentSlug, body_parentId, body_events, body_project, body_monitoredMeasureTypes, body_measurements, body_id
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "compartment": body_compartment, "reactorReplicate": body_reactorReplicate, "slug": body_slug, "reactorSlug": body_reactorSlug, "compartmentSlug": body_compartmentSlug, "displayName": body_displayName, "longSlug": body_longSlug, "parentSlug": body_parentSlug, "parentId": body_parentId, "events": body_events, "project": body_project, "monitoredMeasureTypes": body_monitoredMeasureTypes, "measurements": body_measurements, "id": body_id
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

    