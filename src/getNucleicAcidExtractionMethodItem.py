
import requests

def getNucleicAcidExtractionMethodItem(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    # Headers
    headers = None
):
    final_path = "/nucleic_acid_extraction_methods/{id}".format(
        id = path_id
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    