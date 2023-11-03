
import requests

def getEventCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_location_id, query_location_id_array, query_id, query_id_array
       
    
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
"location.id": query_location_id,
"location.id[]": query_location_id_array,
"id": query_id,
"id[]": query_id_array
        }           
    )

    return response

    