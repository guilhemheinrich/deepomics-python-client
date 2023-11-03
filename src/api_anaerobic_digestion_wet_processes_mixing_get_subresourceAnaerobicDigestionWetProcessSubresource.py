
import requests

def api_anaerobic_digestion_wet_processes_mixing_get_subresourceAnaerobicDigestionWetProcessSubresource(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    # Headers
    headers = None
):
    final_path = "/anaerobic_digestion_wet_processes/{id}/mixing".format(
        id = path_id
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    