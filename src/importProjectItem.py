
import requests

def importProjectItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_participants, body_participantsDisplayName, body_allParticipants, body_observers, body_observersDisplayName, body_startDate, body_endDate, body_experimentalSeries, body_campaigns, body_allLocations, body_coordinator, body_coordinatorDisplayName, body_contact, body_contactDisplayName, body_summary, body_sites, body_samples, body_inputs, body_documents, body_articles, body_status, body_reference, body_canDelete, body_comments, body_id, body_name, body_slug, body_tags, body_tagsName, body_url
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "/project/{id}/import/{type}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "participants": body_participants, "participantsDisplayName": body_participantsDisplayName, "allParticipants": body_allParticipants, "observers": body_observers, "observersDisplayName": body_observersDisplayName, "startDate": body_startDate, "endDate": body_endDate, "experimentalSeries": body_experimentalSeries, "campaigns": body_campaigns, "allLocations": body_allLocations, "coordinator": body_coordinator, "coordinatorDisplayName": body_coordinatorDisplayName, "contact": body_contact, "contactDisplayName": body_contactDisplayName, "summary": body_summary, "sites": body_sites, "samples": body_samples, "inputs": body_inputs, "documents": body_documents, "articles": body_articles, "status": body_status, "reference": body_reference, "canDelete": body_canDelete, "comments": body_comments, "id": body_id, "name": body_name, "slug": body_slug, "tags": body_tags, "tagsName": body_tagsName, "url": body_url
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

    