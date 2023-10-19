
import requests

def getTargetedGeneOrGenomicRegionCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_id, query_id_array, query_name, query_slug, query_slug_array, query_multisearch, query_order_name_, query_order_slug_
       
    
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

    