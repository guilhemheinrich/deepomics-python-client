
import requests

def api_reactors_compartments_constituents_get_subresourceReactorSubresource(
    host
    # Path parameters
       , 
        path_id, path_compartments
       
    # Query parameters
       , 
        query_page, query_pageSize, query_input_id, query_input_id_array, query_id, query_id_array
       
    
    ,
    headers = None
):
    final_path = "/reactors/{id}/compartments/{compartments}/constituents".format(
        id = path_id, compartments = path_compartments
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers,
        params = {
            "page": query_page,
"pageSize": query_pageSize,
"input.id": query_input_id,
"input.id[]": query_input_id_array,
"id": query_id,
"id[]": query_id_array
        }           
    )

    return response

    