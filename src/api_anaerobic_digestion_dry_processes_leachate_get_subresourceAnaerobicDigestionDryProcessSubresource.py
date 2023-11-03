
import requests

def api_anaerobic_digestion_dry_processes_leachate_get_subresourceAnaerobicDigestionDryProcessSubresource(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    # Headers
    headers = None
):
    final_path = "/anaerobic_digestion_dry_processes/{id}/leachate".format(
        id = path_id
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    