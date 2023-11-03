
import requests

def postLibraryCollection(
    host
    
    
    # Body parameters
       , 
        body_libraryKits, body_libraryProcedure, body_libraryLayout, body_libSize, body_libraryVector, body_libraryScreeningStrategy, body_id
       
    ,
    # Optional body content
    optional_json_content = {},
    # Headers
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "libraryKits": body_libraryKits, "libraryProcedure": body_libraryProcedure, "libraryLayout": body_libraryLayout, "libSize": body_libSize, "libraryVector": body_libraryVector, "libraryScreeningStrategy": body_libraryScreeningStrategy, "id": body_id
    }
    json_content = {
        **optional_json_content,
        **required_body_content           
    }
    
    response = requests.post(
        url = host + final_path,
        headers = headers,
        json = json_content           
    )

    return response

    