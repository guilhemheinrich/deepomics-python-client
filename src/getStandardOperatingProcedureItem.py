
import requests

def getStandardOperatingProcedureItem(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    headers = None
):
    final_path = "/standard_operating_procedures/{id}".format(
        id = path_id
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    