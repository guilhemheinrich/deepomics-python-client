
import requests

def deleteSequencingSampleResultItem(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    # Headers
    headers = None
):
    final_path = "/sequencing_sample_results/{id}".format(
        id = path_id
    )
    
    
    
    response = requests.delete(
        url = host + final_path,
        headers = headers           
    )

    return response

    