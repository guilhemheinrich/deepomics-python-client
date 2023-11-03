
import requests

def getSampleCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_location_id, query_location_id_array, query_project_id, query_project_id_array, query_id, query_id_array, query_slug, query_slug_array, query_multisearch, query_order_slug_
       
    
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
"project.id": query_project_id,
"project.id[]": query_project_id_array,
"id": query_id,
"id[]": query_id_array,
"slug": query_slug,
"slug[]": query_slug_array,
"multisearch": query_multisearch,
"order[slug]": query_order_slug_
        }           
    )

    return response

    