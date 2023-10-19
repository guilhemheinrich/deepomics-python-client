
import requests

def api_real_residual_household_wastes_modecoms_get_subresourceRealResidualHouseholdWasteSubresource(
    host
    # Path parameters
       , 
        path_id
       
    # Query parameters
       , 
        query_page, query_pageSize, query_id, query_id_array
       
    
    ,
    headers = None
):
    final_path = "/real_residual_household_wastes/{id}/modecoms".format(
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

    