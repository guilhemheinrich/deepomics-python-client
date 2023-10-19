
import requests

def getImportReportCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize
       
    
    ,
    headers = None
):
    final_path = "${data.path}"
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers,
        params = {
            "page": query_page,
"pageSize": query_pageSize
        }           
    )

    return response

    