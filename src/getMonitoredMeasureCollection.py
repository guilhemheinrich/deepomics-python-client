
import requests

def getMonitoredMeasureCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_measurement, query_measurement_array, query_id, query_id_array
       
    
    ,
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers,
        params = {
            "page": query_page,
"pageSize": query_pageSize,
"measurement": query_measurement,
"measurement[]": query_measurement_array,
"id": query_id,
"id[]": query_id_array
        }           
    )

    return response

    