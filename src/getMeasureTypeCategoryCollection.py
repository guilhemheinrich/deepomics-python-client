
import requests

def getMeasureTypeCategoryCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_children, query_children_array, query_parent, query_parent_array, query_types, query_types_array, query_id, query_id_array, query_name, query_exists_children_, query_exists_parent_, query_exists_types_, query_multisearch, query_order_name_
       
    
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
"children": query_children,
"children[]": query_children_array,
"parent": query_parent,
"parent[]": query_parent_array,
"types": query_types,
"types[]": query_types_array,
"id": query_id,
"id[]": query_id_array,
"name": query_name,
"exists[children]": query_exists_children_,
"exists[parent]": query_exists_parent_,
"exists[types]": query_exists_types_,
"multisearch": query_multisearch,
"order[name]": query_order_name_
        }           
    )

    return response

    