
import requests

def getGraphCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_monitoredMeasureTypes, query_monitoredMeasureTypes_array, query_id, query_id_array, query_name, query_multisearch, query_order_name_
       
    
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
"monitoredMeasureTypes": query_monitoredMeasureTypes,
"monitoredMeasureTypes[]": query_monitoredMeasureTypes_array,
"id": query_id,
"id[]": query_id_array,
"name": query_name,
"multisearch": query_multisearch,
"order[name]": query_order_name_
        }           
    )

    return response

    