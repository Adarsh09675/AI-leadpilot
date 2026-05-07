from fastapi import HTTPException, Security, status
from fastapi.security.api_key import APIKeyHeader
from app.config.settings import settings

API_KEY_NAME = "x-api-key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(header_value: str = Security(api_key_header)):
    """
    Validates the x-api-key header against the configured API_KEY.
    """
    if not header_value:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key missing from x-api-key header."
        )
        
    if header_value == settings.API_KEY:
        return header_value
    
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid API Key."
    )
