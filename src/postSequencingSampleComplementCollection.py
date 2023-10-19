
import requests

def postSequencingSampleComplementCollection(
    host
    
    
    # Body parameters
       , 
        body_nuclAcidAmp, body_pcrCond, body_library, body_seqReadLength, body_mids, body_displayMids, body_adapters, body_displayAdapters, body_urls, body_displayUrls, body_sops, body_displaySops, body_id
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "nuclAcidAmp": body_nuclAcidAmp}, "pcrCond": body_pcrCond}, "library": body_library}, "seqReadLength": body_seqReadLength}, "mids": body_mids}, "displayMids": body_displayMids}, "adapters": body_adapters}, "displayAdapters": body_displayAdapters}, "urls": body_urls}, "displayUrls": body_displayUrls}, "sops": body_sops}, "displaySops": body_displaySops}, "id": body_id}
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

    