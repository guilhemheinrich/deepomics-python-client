
import requests

def api_compartments_constituents_amount_get_subresourceCompartmentSubresource(
    host
    # Path parameters
       , 
        path_id, path_constituents
       
    
    
    ,
    # Headers
    headers = None
):
    final_path = "/compartments/{id}/constituents/{constituents}/amount".format(
        id = path_id, constituents = path_constituents
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    