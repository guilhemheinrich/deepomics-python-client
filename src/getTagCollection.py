
import requests

def getTagCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_isDeprecated, query_isDeprecated_array, query_id, query_id_array, query_name, query_slug, query_slug_array, query_multisearch, query_order_name_, query_order_slug_
       
    
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
"isDeprecated": query_isDeprecated,
"isDeprecated[]": query_isDeprecated_array,
"id": query_id,
"id[]": query_id_array,
"name": query_name,
"slug": query_slug,
"slug[]": query_slug_array,
"multisearch": query_multisearch,
"order[name]": query_order_name_,
"order[slug]": query_order_slug_
        }           
    )

    return response

    