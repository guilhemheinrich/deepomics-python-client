
import requests

def getImportReportItem(
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
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers           
    )

    return response

    