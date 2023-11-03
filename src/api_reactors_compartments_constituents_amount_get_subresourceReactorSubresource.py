
import requests

def api_reactors_compartments_constituents_amount_get_subresourceReactorSubresource(
    host
    # Path parameters
       , 
        path_id, path_compartments, path_constituents
       
    
    
    ,
    # Headers
    headers = None
):
    final_path = "/reactors/{id}/compartments/{compartments}/constituents/{constituents}/amount".format(
        id = path_id, compartments = path_compartments, constituents = path_constituents
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    