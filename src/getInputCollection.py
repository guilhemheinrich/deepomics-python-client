
import requests

def getInputCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_inputCategory, query_inputCategory_array, query_inputCategory_id, query_inputCategory_id_array, query_project, query_project_array, query_project_id, query_project_id_array, query_id, query_id_array, query_name, query_multisearch, query_order_name_
       
    
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
"inputCategory": query_inputCategory,
"inputCategory[]": query_inputCategory_array,
"inputCategory.id": query_inputCategory_id,
"inputCategory.id[]": query_inputCategory_id_array,
"project": query_project,
"project[]": query_project_array,
"project.id": query_project_id,
"project.id[]": query_project_id_array,
"id": query_id,
"id[]": query_id_array,
"name": query_name,
"multisearch": query_multisearch,
"order[name]": query_order_name_
        }           
    )

    return response

    