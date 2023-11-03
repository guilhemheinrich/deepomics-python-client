
import requests

def api_reconstituted_household_wastes_measures_get_subresourceReconstitutedHouseholdWasteSubresource(
    host
    # Path parameters
       , 
        path_id
       
    # Query parameters
       , 
        query_page, query_pageSize, query_id, query_id_array
       
    
    ,
    # Headers
    headers = None
):
    final_path = "/reconstituted_household_wastes/{id}/measures".format(
        id = path_id
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers,
        params = {
            "page": query_page,
"pageSize": query_pageSize,
"id": query_id,
"id[]": query_id_array
        }           
    )

    return response

    