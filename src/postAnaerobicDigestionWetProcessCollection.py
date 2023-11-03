
import requests

def postAnaerobicDigestionWetProcessCollection(
    host
    
    
    # Body parameters
       , 
        body_temperature, body_support, body_mixing, body_processCategory, body_site, body_siteName, body_siteSlug, body_displayName, body_longSlug, body_canDelete, body_parentSlug, body_parentId, body_events, body_slug, body_project, body_monitoredMeasureTypes, body_measurements, body_id, body_comments, body_name, body_measures
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "temperature": body_temperature, "support": body_support, "mixing": body_mixing, "processCategory": body_processCategory, "site": body_site, "siteName": body_siteName, "siteSlug": body_siteSlug, "displayName": body_displayName, "longSlug": body_longSlug, "canDelete": body_canDelete, "parentSlug": body_parentSlug, "parentId": body_parentId, "events": body_events, "slug": body_slug, "project": body_project, "monitoredMeasureTypes": body_monitoredMeasureTypes, "measurements": body_measurements, "id": body_id, "comments": body_comments, "name": body_name, "measures": body_measures
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

    