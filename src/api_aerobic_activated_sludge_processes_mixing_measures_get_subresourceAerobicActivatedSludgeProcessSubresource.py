
import requests

def api_aerobic_activated_sludge_processes_mixing_measures_get_subresourceAerobicActivatedSludgeProcessSubresource(
    host
    # Path parameters
       , 
        path_id, path_mixing
       
    # Query parameters
       , 
        query_page, query_pageSize, query_id, query_id_array
       
    
    ,
    # Headers
    headers = None
):
    final_path = "/aerobic_activated_sludge_processes/{id}/mixing/measures".format(
        id = path_id, mixing = path_mixing
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

    