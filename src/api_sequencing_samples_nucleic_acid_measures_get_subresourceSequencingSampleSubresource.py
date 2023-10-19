
import requests

def api_sequencing_samples_nucleic_acid_measures_get_subresourceSequencingSampleSubresource(
    host
    # Path parameters
       , 
        path_id, path_nucleicAcid
       
    # Query parameters
       , 
        query_page, query_pageSize, query_id, query_id_array
       
    
    ,
    headers = None
):
    final_path = "/sequencing_samples/{id}/nucleic_acid/measures".format(
        id = path_id, nucleicAcid = path_nucleicAcid
    )
    
    
    
    response = requests.get(
        url = host + final_path,
        headers = headers,
        params = {
            "page": query_page,
"pageSize": query_pageSize,
"id": query_id,
"id[]": query_id_array
        }           
    )

    return response

    