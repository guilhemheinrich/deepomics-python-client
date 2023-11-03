
import requests

def api_supports_measures_get_subresourceSupportSubresource(
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
    final_path = "/supports/{id}/measures".format(
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

    