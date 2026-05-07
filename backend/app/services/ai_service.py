import google.generativeai as genai
import json
from app.config.settings import settings
from app.utils.logger import logger
from app.schemas.lead_schema import LeadClassificationResponse

class AIService:
    def __init__(self):
        if settings.GEMINI_API_KEY:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            self.model = genai.GenerativeModel('gemini-pro')
        else:
            self.model = None
            logger.warning("GEMINI_API_KEY not found. AI features will use mock logic.")

    async def classify_intent(self, message: str) -> LeadClassificationResponse:
        if not message:
            return LeadClassificationResponse(intent="unknown", confidence=0.0, is_hot_lead=False)

        prompt = f"""
        Analyze the following lead message and classify it into one of these categories:
        - sales_enquiry
        - partnership
        - support
        - spam
        - unknown

        Return the result strictly as a JSON object with two fields:
        "intent": (the category name)
        "confidence": (a float between 0 and 1)

        Message: "{message}"
        """

        try:
            if self.model:
                response = self.model.generate_content(prompt)
                # Clean the response text in case of markdown blocks
                clean_text = response.text.replace('```json', '').replace('```', '').strip()
                data = json.loads(clean_text)
            else:
                raise Exception("Model not initialized")

        except Exception as e:
            logger.error(f"AI Classification failed: {str(e)}. Falling back to keywords.")
            data = self._mock_classification(message)

        # Apply Confidence Threshold Logic
        final_intent = data.get("intent", "unknown")
        final_confidence = data.get("confidence", 0.0)

        if final_confidence < 0.6:
            logger.info(f"Low confidence ({final_confidence}). Defaulting intent to unknown.")
            final_intent = "unknown"

        is_hot = final_intent == "sales_enquiry" and final_confidence > 0.8

        return LeadClassificationResponse(
            intent=final_intent,
            confidence=final_confidence,
            is_hot_lead=is_hot
        )

    def _mock_classification(self, message: str) -> dict:
        msg = message.lower()
        if any(kw in msg for kw in ["buy", "price", "interested", "demo", "services"]):
            return {"intent": "sales_enquiry", "confidence": 0.85}
        elif any(kw in msg for kw in ["partner", "collab", "integration"]):
            return {"intent": "partnership", "confidence": 0.80}
        elif any(kw in msg for kw in ["help", "issue", "error", "bug"]):
            return {"intent": "support", "confidence": 0.90}
        return {"intent": "unknown", "confidence": 0.50}

ai_service = AIService()
