
import requests

def deleteImportReportItem(
    host
    # Path parameters
       , 
        path_subject
       
    
    
    ,
    # Headers
    headers = None
):
    final_path = "/import_reports/{subject}".format(
        subject = path_subject
    )
    
    
    
    response = requests.delete(
        url = host + final_path,
        headers = headers           
    )

    return response

    