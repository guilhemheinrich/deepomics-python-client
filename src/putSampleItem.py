
import requests

def putSampleItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_description, body_type, body_typeLabel, body_comment, body_project, body_locationDetails, body_sequencingSamples, body_sequencingRunSlug, body_displaySampleResults, body_date, body_location, body_operator, body_locationSlug, body_id, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "/samples/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "description": body_description}, "type": body_type}, "typeLabel": body_typeLabel}, "comment": body_comment}, "project": body_project}, "locationDetails": body_locationDetails}, "sequencingSamples": body_sequencingSamples}, "sequencingRunSlug": body_sequencingRunSlug}, "displaySampleResults": body_displaySampleResults}, "date": body_date}, "location": body_location}, "operator": body_operator}, "locationSlug": body_locationSlug}, "id": body_id}, "slug": body_slug}
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

    