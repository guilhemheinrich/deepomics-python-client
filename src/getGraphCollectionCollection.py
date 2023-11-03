
import requests

def getGraphCollectionCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_operation, query_operation_array, query_id, query_id_array, query_name, query_multisearch, query_order_name_
       
    
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
"operation": query_operation,
"operation[]": query_operation_array,
"id": query_id,
"id[]": query_id_array,
"name": query_name,
"multisearch": query_multisearch,
"order[name]": query_order_name_
        }           
    )

    return response

    