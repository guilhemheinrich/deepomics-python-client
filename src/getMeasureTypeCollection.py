
import requests

def getMeasureTypeCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_slug, query_slug_array, query_name, query_category, query_category_array, query_tags, query_tags_array, query_tags_slug, query_tags_slug_array, query_id, query_id_array, query_order_slug_, query_order_name_, query_multisearch
       
    
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
"slug": query_slug,
"slug[]": query_slug_array,
"name": query_name,
"category": query_category,
"category[]": query_category_array,
"tags": query_tags,
"tags[]": query_tags_array,
"tags.slug": query_tags_slug,
"tags.slug[]": query_tags_slug_array,
"id": query_id,
"id[]": query_id_array,
"order[slug]": query_order_slug_,
"order[name]": query_order_name_,
"multisearch": query_multisearch
        }           
    )

    return response

    