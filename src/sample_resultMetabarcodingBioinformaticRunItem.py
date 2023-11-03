
import requests

def sample_resultMetabarcodingBioinformaticRunItem(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    # Headers
    headers = None
):
    final_path = "/metabarcoding_bioinformation_run/{id}/sample_result".format(
        id = path_id
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    