
import requests

def api_sequencing_sample_complements_library_get_subresourceSequencingSampleComplementSubresource(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    headers = None
):
    final_path = "/sequencing_sample_complements/{id}/library".format(
        id = path_id
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    