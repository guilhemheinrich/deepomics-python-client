
import requests

def deleteMonitoredMeasureTypeItem(
    host
    # Path parameters
       , 
        path_id
       
    
    
    ,
    # Headers
    headers = None
):
    final_path = "/monitored_measure_types/{id}".format(
        id = path_id
    )
    
    
    
    response = requests.delete(
        url = host + final_path,
        headers = headers           
    )

    return response

    