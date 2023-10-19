
import requests

def getConstituentCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_input_id, query_input_id_array, query_id, query_id_array
       
    
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
"input.id": query_input_id,
"input.id[]": query_input_id_array,
"id": query_id,
"id[]": query_id_array
        }           
    )

    return response

    