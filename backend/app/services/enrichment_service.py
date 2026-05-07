from app.utils.logger import logger
from app.schemas.lead_schema import LeadEnrichmentResponse

class EnrichmentService:
    @staticmethod
    async def enrich_lead(name: str, company: str, email: str) -> LeadEnrichmentResponse:
        logger.info(f"Enriching lead: {name} from {company}")
        
        # 1. Generate a realistic LinkedIn URL
        formatted_name = name.lower().replace(" ", "")
        linkedin_url = f"https://www.linkedin.com/in/{formatted_name}-{company.lower().replace(' ', '')}"
        
        # 2. Derive Industry based on keywords
        company_lower = company.lower()
        if any(kw in company_lower for kw in ["tech", "software", "ai", "data", "cloud"]):
            industry = "Technology / SaaS"
        elif any(kw in company_lower for kw in ["bank", "finance", "invest", "crypto"]):
            industry = "FinTech / Finance"
        elif any(kw in company_lower for kw in ["health", "med", "bio", "clinic"]):
            industry = "Healthcare"
        else:
            industry = "Professional Services"
            
        # 3. Derive Company Size based on length (mock strategy)
        name_len = len(company)
        if name_len < 6:
            company_size = "11-50 employees"
        elif name_len < 12:
            company_size = "51-200 employees"
        elif name_len < 20:
            company_size = "201-1000 employees"
        else:
            company_size = "1000+ employees"
            
        return LeadEnrichmentResponse(
            linkedin_url=linkedin_url,
            company_size=company_size,
            industry=industry
        )

enrichment_service = EnrichmentService()
