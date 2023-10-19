
import requests

def getTemperatureCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_id, query_id_array
       
    
    ,
    headers = None
):
    final_path = "${data.path}"
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers,
        params = {
            "page": query_page,
"pageSize": query_pageSize,
"id": query_id,
"id[]": query_id_array
        }           
    )

    return response

    