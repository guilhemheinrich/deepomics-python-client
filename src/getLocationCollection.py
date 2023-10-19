
import requests

def getLocationCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_project_id, query_project_id_array, query_id, query_id_array, query_multisearch
       
    
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
"project.id": query_project_id,
"project.id[]": query_project_id_array,
"id": query_id,
"id[]": query_id_array,
"multisearch": query_multisearch
        }           
    )

    return response

    