
import requests

def putSiteItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_project, body_processes, body_operators, body_operatorsDisplayName, body_campaigns, body_syndicate, body_region, body_coordinates, body_canDelete, body_city, body_country, body_id, body_name, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "/sites/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "project": body_project, "processes": body_processes, "operators": body_operators, "operatorsDisplayName": body_operatorsDisplayName, "campaigns": body_campaigns, "syndicate": body_syndicate, "region": body_region, "coordinates": body_coordinates, "canDelete": body_canDelete, "city": body_city, "country": body_country, "id": body_id, "name": body_name, "slug": body_slug
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

    