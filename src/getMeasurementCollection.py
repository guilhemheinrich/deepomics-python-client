
import requests

def getMeasurementCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_location, query_location_array, query_type, query_type_array, query_id, query_id_array
       
    
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
"location": query_location,
"location[]": query_location_array,
"type": query_type,
"type[]": query_type_array,
"id": query_id,
"id[]": query_id_array
        }           
    )

    return response

    