
import requests

def api_reactors_replicates_get_subresourceReactorSubresource(
    host
    # Path parameters
       , 
        path_id
       
    # Query parameters
       , 
        query_page, query_pageSize, query_reactor_experimentalSeries_id, query_reactor_experimentalSeries_id_array, query_reactor_id, query_reactor_id_array, query_id, query_id_array, query_slug, query_slug_array, query_multisearch, query_order_slug_
       
    
    ,
    # Headers
    headers = None
):
    final_path = "/reactors/{id}/replicates".format(
        id = path_id
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers,
        params = {
            "page": query_page,
"pageSize": query_pageSize,
"reactor.experimentalSeries.id": query_reactor_experimentalSeries_id,
"reactor.experimentalSeries.id[]": query_reactor_experimentalSeries_id_array,
"reactor.id": query_reactor_id,
"reactor.id[]": query_reactor_id_array,
"id": query_id,
"id[]": query_id_array,
"slug": query_slug,
"slug[]": query_slug_array,
"multisearch": query_multisearch,
"order[slug]": query_order_slug_
        }           
    )

    return response

    