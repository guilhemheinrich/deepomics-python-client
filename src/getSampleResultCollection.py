
import requests

def getSampleResultCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_metabarcodingBioinformaticRun_project_id, query_metabarcodingBioinformaticRun_project_id_array, query_id, query_id_array
       
    
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
"metabarcodingBioinformaticRun.project.id": query_metabarcodingBioinformaticRun_project_id,
"metabarcodingBioinformaticRun.project.id[]": query_metabarcodingBioinformaticRun_project_id_array,
"id": query_id,
"id[]": query_id_array
        }           
    )

    return response

    