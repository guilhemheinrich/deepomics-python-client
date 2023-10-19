
import requests

def api_sequencing_samples_sequencing_sample_complement_get_subresourceSequencingSampleSubresource(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    headers = None
):
    final_path = "/sequencing_samples/{id}/sequencing_sample_complement".format(
        id = path_id
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    