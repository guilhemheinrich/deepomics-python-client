
import requests

def getAnaerobicDigestionDryProcessItem(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    headers = None
):
    final_path = "/anaerobic_digestion_dry_processes/{id}".format(
        id = path_id
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    