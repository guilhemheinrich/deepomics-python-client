
import requests

def putLibraryItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_libraryKits, body_libraryProcedure, body_libraryLayout, body_libSize, body_libraryVector, body_libraryScreeningStrategy, body_id
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "/libraries/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "libraryKits": body_libraryKits}, "libraryProcedure": body_libraryProcedure}, "libraryLayout": body_libraryLayout}, "libSize": body_libSize}, "libraryVector": body_libraryVector}, "libraryScreeningStrategy": body_libraryScreeningStrategy}, "id": body_id}
    }
    json_content = {
        **optional_json_content,
        **required_body_content           
    }
    
    response = requests.put(
        url = host + final_path,
        headers = headers,
        json = json_content           
    )

    return response

    