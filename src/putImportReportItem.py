
import requests

def putImportReportItem(
    host
    # Path parameters
       , 
        path_subject
       
    
    # Body parameters
       , 
        body_status, body_subject, body_errors, body_warnings, body_creations, body_editions, body_deletions, body_untouched
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "/import_reports/{subject}".format(
        subject = path_subject
    )
    
    # Body parameters (required)
    required_body_content = {
        "status": body_status}, "subject": body_subject}, "errors": body_errors}, "warnings": body_warnings}, "creations": body_creations}, "editions": body_editions}, "deletions": body_deletions}, "untouched": body_untouched}
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

    