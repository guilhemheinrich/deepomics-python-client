
import requests

def getProjectCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_order_startDate_, query_order_coordinator_lastname_, query_order_name_, query_order_slug_, query_startDate, query_startDate_array, query_coordinator_lastname, query_id, query_id_array, query_name, query_slug, query_slug_array, query_multisearch
       
    
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
"order[startDate]": query_order_startDate_,
"order[coordinator.lastname]": query_order_coordinator_lastname_,
"order[name]": query_order_name_,
"order[slug]": query_order_slug_,
"startDate": query_startDate,
"startDate[]": query_startDate_array,
"coordinator.lastname": query_coordinator_lastname,
"id": query_id,
"id[]": query_id_array,
"name": query_name,
"slug": query_slug,
"slug[]": query_slug_array,
"multisearch": query_multisearch
        }           
    )

    return response

    