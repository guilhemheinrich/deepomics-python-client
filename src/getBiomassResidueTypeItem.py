
import requests

def getBiomassResidueTypeItem(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    headers = None
):
    final_path = "/biomass_residue_types/{id}".format(
        id = path_id
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    