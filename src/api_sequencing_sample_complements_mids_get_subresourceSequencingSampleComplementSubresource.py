
import requests

def api_sequencing_sample_complements_mids_get_subresourceSequencingSampleComplementSubresource(
    host
    # Path parameters
       , 
        path_id
       
    # Query parameters
       , 
        query_page, query_pageSize, query_sequence, query_id, query_id_array, query_slug, query_slug_array, query_multisearch, query_order_sequence_, query_order_slug_
       
    
    ,
    # Headers
    headers = None
):
    final_path = "/sequencing_sample_complements/{id}/mids".format(
        id = path_id
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers,
        params = {
            "page": query_page,
"pageSize": query_pageSize,
"sequence": query_sequence,
"id": query_id,
"id[]": query_id_array,
"slug": query_slug,
"slug[]": query_slug_array,
"multisearch": query_multisearch,
"order[sequence]": query_order_sequence_,
"order[slug]": query_order_slug_
        }           
    )

    return response

    