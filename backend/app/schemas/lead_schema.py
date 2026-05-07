from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime

class LeadBase(BaseModel):
    name: str = Field(..., min_length=1, example="John Doe")
    email: EmailStr = Field(..., example="john@company.com")
    company: str = Field(..., min_length=1, example="Acme Inc")
    message: Optional[str] = Field(None, example="I am interested in your SaaS services")

class LeadCreate(LeadBase):
    pass

class LeadEnrichmentResponse(BaseModel):
    linkedin_url: str
    company_size: str
    industry: str

class LeadClassificationResponse(BaseModel):
    intent: str
    confidence: float
    is_hot_lead: bool

class LeadResponse(LeadBase):
    id: Optional[int] = None
    linkedin_url: Optional[str] = None
    company_size: Optional[str] = None
    industry: Optional[str] = None
    intent: Optional[str] = None
    confidence: Optional[float] = None
    created_at: Optional[datetime] = None

    class Config:
        from_attributes = True
