
import requests

def getCompartmentReplicateCollection(
    host
    
    # Query parameters
       , 
        query_page, query_pageSize, query_compartment_reactor_experimentalSeries, query_compartment_reactor_experimentalSeries_array, query_compartment, query_compartment_array, query_reactorReplicate, query_reactorReplicate_array, query_id, query_id_array, query_project_id, query_project_id_array, query_multisearch
       
    
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
"compartment.reactor.experimentalSeries": query_compartment_reactor_experimentalSeries,
"compartment.reactor.experimentalSeries[]": query_compartment_reactor_experimentalSeries_array,
"compartment": query_compartment,
"compartment[]": query_compartment_array,
"reactorReplicate": query_reactorReplicate,
"reactorReplicate[]": query_reactorReplicate_array,
"id": query_id,
"id[]": query_id_array,
"project.id": query_project_id,
"project.id[]": query_project_id_array,
"multisearch": query_multisearch
        }           
    )

    return response

    