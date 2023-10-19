
import requests

def putCompartmentItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_id, body_reactor, body_constituents, body_experimentalSeries, body_project, body_longSlug, body_locations, body_feedingType, body_displayFeedingType, body_canDelete, body_measures, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "/compartments/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "id": body_id}, "reactor": body_reactor}, "constituents": body_constituents}, "experimentalSeries": body_experimentalSeries}, "project": body_project}, "longSlug": body_longSlug}, "locations": body_locations}, "feedingType": body_feedingType}, "displayFeedingType": body_displayFeedingType}, "canDelete": body_canDelete}, "measures": body_measures}, "slug": body_slug}
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

    