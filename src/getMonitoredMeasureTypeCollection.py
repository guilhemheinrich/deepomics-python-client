
import requests

def getMonitoredMeasureTypeCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_operation_id, query_operation_id_array, query_locations, query_locations_array, query_id, query_id_array
       
    
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
"operation.id": query_operation_id,
"operation.id[]": query_operation_id_array,
"locations": query_locations,
"locations[]": query_locations_array,
"id": query_id,
"id[]": query_id_array
        }           
    )

    return response

    