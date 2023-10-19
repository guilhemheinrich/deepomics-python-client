
import requests

def getLogEntryCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_date_before_, query_date_strictly_before_, query_date_after_, query_date_strictly_after_, query_date, query_date_array, query_actor, query_entityUri, query_entityUri_array, query_entityType, query_entityLabel, query_eventName, query_eventName_array, query_projectUuid, query_projectUuid_array, query_projectPart, query_projectPart_array, query_id, query_id_array, query_order_date_, query_order_actor_, query_multisearch
       
    
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
"date[before]": query_date_before_,
"date[strictly_before]": query_date_strictly_before_,
"date[after]": query_date_after_,
"date[strictly_after]": query_date_strictly_after_,
"date": query_date,
"date[]": query_date_array,
"actor": query_actor,
"entityUri": query_entityUri,
"entityUri[]": query_entityUri_array,
"entityType": query_entityType,
"entityLabel": query_entityLabel,
"eventName": query_eventName,
"eventName[]": query_eventName_array,
"projectUuid": query_projectUuid,
"projectUuid[]": query_projectUuid_array,
"projectPart": query_projectPart,
"projectPart[]": query_projectPart_array,
"id": query_id,
"id[]": query_id_array,
"order[date]": query_order_date_,
"order[actor]": query_order_actor_,
"multisearch": query_multisearch
        }           
    )

    return response

    