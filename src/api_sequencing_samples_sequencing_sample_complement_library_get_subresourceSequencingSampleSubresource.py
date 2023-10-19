
import requests

def api_sequencing_samples_sequencing_sample_complement_library_get_subresourceSequencingSampleSubresource(
    host
    # Path parameters
       , 
        path_id, path_sequencingSampleComplement
       
    
    
    ,
    headers = None
):
    final_path = "/sequencing_samples/{id}/sequencing_sample_complement/library".format(
        id = path_id, sequencingSampleComplement = path_sequencingSampleComplement
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    