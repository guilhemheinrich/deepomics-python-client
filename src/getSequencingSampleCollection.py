
import requests

def getSequencingSampleCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_sequencingRun_id, query_sequencingRun_id_array, query_sequencingRun_project_id, query_sequencingRun_project_id_array, query_id, query_id_array, query_slug, query_slug_array, query_multisearch, query_order_slug_
       
    
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
"sequencingRun.id": query_sequencingRun_id,
"sequencingRun.id[]": query_sequencingRun_id_array,
"sequencingRun.project.id": query_sequencingRun_project_id,
"sequencingRun.project.id[]": query_sequencingRun_project_id_array,
"id": query_id,
"id[]": query_id_array,
"slug": query_slug,
"slug[]": query_slug_array,
"multisearch": query_multisearch,
"order[slug]": query_order_slug_
        }           
    )

    return response

    