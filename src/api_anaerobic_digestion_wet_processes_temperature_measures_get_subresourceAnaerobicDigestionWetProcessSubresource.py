
import requests

def api_anaerobic_digestion_wet_processes_temperature_measures_get_subresourceAnaerobicDigestionWetProcessSubresource(
    host
    # Path parameters
       , 
        path_id, path_temperature
       
    # Query parameters
       , 
        query_page, query_pageSize, query_id, query_id_array
       
    
    ,
    headers = None
):
    final_path = "/anaerobic_digestion_wet_processes/{id}/temperature/measures".format(
        id = path_id, temperature = path_temperature
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

    