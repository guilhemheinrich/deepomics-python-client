
import requests

def getUnitCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_measureTypes_id, query_measureTypes_id_array, query_slug, query_slug_array, query_id, query_id_array, query_name, query_multisearch, query_order_name_, query_order_slug_
       
    
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
"measureTypes.id": query_measureTypes_id,
"measureTypes.id[]": query_measureTypes_id_array,
"slug": query_slug,
"slug[]": query_slug_array,
"id": query_id,
"id[]": query_id_array,
"name": query_name,
"multisearch": query_multisearch,
"order[name]": query_order_name_,
"order[slug]": query_order_slug_
        }           
    )

    return response

    