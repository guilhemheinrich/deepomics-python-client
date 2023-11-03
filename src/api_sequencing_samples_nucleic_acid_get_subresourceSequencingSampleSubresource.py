
import requests

def api_sequencing_samples_nucleic_acid_get_subresourceSequencingSampleSubresource(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    # Headers
    headers = None
):
    final_path = "/sequencing_samples/{id}/nucleic_acid".format(
        id = path_id
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    