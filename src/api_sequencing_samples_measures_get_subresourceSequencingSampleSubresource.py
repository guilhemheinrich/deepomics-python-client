
import requests

def api_sequencing_samples_measures_get_subresourceSequencingSampleSubresource(
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
    final_path = "/sequencing_samples/{id}/measures".format(
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

    