
import requests

def api_anaerobic_digestion_dry_processes_leachate_measures_get_subresourceAnaerobicDigestionDryProcessSubresource(
    host
    # Path parameters
       , 
        path_id, path_leachate
       
    # Query parameters
       , 
        query_page, query_pageSize, query_id, query_id_array
       
    
    ,
    # Headers
    headers = None
):
    final_path = "/anaerobic_digestion_dry_processes/{id}/leachate/measures".format(
        id = path_id, leachate = path_leachate
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

    