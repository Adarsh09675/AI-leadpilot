from fastapi import APIRouter, Depends, Request
from app.schemas.lead_schema import LeadCreate, LeadEnrichmentResponse, LeadClassificationResponse
from app.services.enrichment_service import enrichment_service
from app.services.ai_service import ai_service
from app.utils.logger import logger

router = APIRouter(prefix="/leads", tags=["Leads"])

@router.post("/enrich", response_model=LeadEnrichmentResponse)
async def enrich_lead_endpoint(lead: LeadCreate, request: Request):
    logger.info(f"Processing enrichment request for {lead.email}")
    return await enrichment_service.enrich_lead(lead.name, lead.company, lead.email)

@router.post("/classify", response_model=LeadClassificationResponse)
async def classify_lead_endpoint(lead: LeadCreate, request: Request):
    logger.info(f"Processing classification request for {lead.email}")
    return await ai_service.classify_intent(lead.message or "")
