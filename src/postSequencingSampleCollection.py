
import requests

def postSequencingSampleCollection(
    host
    
    
    # Body parameters
       , 
        body_sequencingRun, body_project, body_sample, body_displaySample, body_pcrPrimers, body_displayPcrPrimers, body_matrixType, body_displayMatrixType, body_nucleicAcid, body_targetedGeneOrGenomicRegion, body_displayTargetedGeneOrGenomicRegion, body_taxonomicOrFunctionalGroups, body_displayTaxonomicOrFunctionalGroups, body_targetSubfragments, body_displaySubfragments, body_sequencingSampleComplement, body_sequencingSampleResult, body_sampleResults, body_theBestSampleResult, body_canDelete, body_correctTargetSubfragmentsMandatory, body_libraryLayoutSlug, body_resultFilename, body_resultReverseFilename, body_comments, body_id, body_measures, body_slug
       
    ,
    # Optional body content
    optional_json_content = {},
    headers = None
):
    final_path = "${data.path}"
    
    # Body parameters (required)
    required_body_content = {
        "sequencingRun": body_sequencingRun}, "project": body_project}, "sample": body_sample}, "displaySample": body_displaySample}, "pcrPrimers": body_pcrPrimers}, "displayPcrPrimers": body_displayPcrPrimers}, "matrixType": body_matrixType}, "displayMatrixType": body_displayMatrixType}, "nucleicAcid": body_nucleicAcid}, "targetedGeneOrGenomicRegion": body_targetedGeneOrGenomicRegion}, "displayTargetedGeneOrGenomicRegion": body_displayTargetedGeneOrGenomicRegion}, "taxonomicOrFunctionalGroups": body_taxonomicOrFunctionalGroups}, "displayTaxonomicOrFunctionalGroups": body_displayTaxonomicOrFunctionalGroups}, "targetSubfragments": body_targetSubfragments}, "displaySubfragments": body_displaySubfragments}, "sequencingSampleComplement": body_sequencingSampleComplement}, "sequencingSampleResult": body_sequencingSampleResult}, "sampleResults": body_sampleResults}, "theBestSampleResult": body_theBestSampleResult}, "canDelete": body_canDelete}, "correctTargetSubfragmentsMandatory": body_correctTargetSubfragmentsMandatory}, "libraryLayoutSlug": body_libraryLayoutSlug}, "resultFilename": body_resultFilename}, "resultReverseFilename": body_resultReverseFilename}, "comments": body_comments}, "id": body_id}, "measures": body_measures}, "slug": body_slug}
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

    