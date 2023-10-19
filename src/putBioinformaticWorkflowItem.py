
import requests

def putBioinformaticWorkflowItem(
    host
    # Path parameters
       , 
        path_id
       
    
    # Body parameters
       , 
        body_version, body_bioinformaticFrameworks, body_bioinformaticFrameworksDisplay, body_trimmingAndDenoisingTools, body_trimmingAndDenoisingToolsDisplay, body_assemblySoftware, body_assemblySoftwareDisplay, body_chimeraChecks, body_chimeraChecksDisplay, body_clusteringTools, body_clusteringToolsDisplay, body_taxoAssignTools, body_taxoAssignToolsDisplay, body_taxoAssignDbs, body_taxoAssignDbsDisplay, body_procedure, body_displayProcedure, body_validStatusPublic, body_validPublicStatusSoftware, body_validStatusProcedure, body_slugWithStatus, body_canDelete, body_doi, body_id, body_name, body_project, body_status, body_correctStatusAndProject, body_slug, body_url
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "/bioinformatic_workflows/{id}".format(
        id = path_id
    )
    
    # Body parameters (required)
    required_body_content = {
        "version": body_version}, "bioinformaticFrameworks": body_bioinformaticFrameworks}, "bioinformaticFrameworksDisplay": body_bioinformaticFrameworksDisplay}, "trimmingAndDenoisingTools": body_trimmingAndDenoisingTools}, "trimmingAndDenoisingToolsDisplay": body_trimmingAndDenoisingToolsDisplay}, "assemblySoftware": body_assemblySoftware}, "assemblySoftwareDisplay": body_assemblySoftwareDisplay}, "chimeraChecks": body_chimeraChecks}, "chimeraChecksDisplay": body_chimeraChecksDisplay}, "clusteringTools": body_clusteringTools}, "clusteringToolsDisplay": body_clusteringToolsDisplay}, "taxoAssignTools": body_taxoAssignTools}, "taxoAssignToolsDisplay": body_taxoAssignToolsDisplay}, "taxoAssignDbs": body_taxoAssignDbs}, "taxoAssignDbsDisplay": body_taxoAssignDbsDisplay}, "procedure": body_procedure}, "displayProcedure": body_displayProcedure}, "validStatusPublic": body_validStatusPublic}, "validPublicStatusSoftware": body_validPublicStatusSoftware}, "validStatusProcedure": body_validStatusProcedure}, "slugWithStatus": body_slugWithStatus}, "canDelete": body_canDelete}, "doi": body_doi}, "id": body_id}, "name": body_name}, "project": body_project}, "status": body_status}, "correctStatusAndProject": body_correctStatusAndProject}, "slug": body_slug}, "url": body_url}
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

    