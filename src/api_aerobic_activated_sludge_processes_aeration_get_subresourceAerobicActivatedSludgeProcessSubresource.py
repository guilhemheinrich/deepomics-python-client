
import requests

def api_aerobic_activated_sludge_processes_aeration_get_subresourceAerobicActivatedSludgeProcessSubresource(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    # Headers
    headers = None
):
    final_path = "/aerobic_activated_sludge_processes/{id}/aeration".format(
        id = path_id
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    