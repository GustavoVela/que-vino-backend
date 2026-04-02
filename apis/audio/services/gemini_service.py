import os
from google import genai
from google.genai import types
from config import settings
from core.logger import logger
from typing import Optional, Tuple

"""
Servicio de enriquecimiento de audio mediante Gemini GenAI (SDK v1.70.0+).
Cumple con la Sección 1.16 de la Constitución, utilizando el SDK 'google-genai' 
y el patrón de Prompts distribuido en archivos Markdown (Sección 10).
"""

class GeminiService:
    def __init__(self, api_key: Optional[str]):
        # Configuración del cliente según disponibilidad de API Key (Native vs Vertex/ADC)
        client_args = {}
        if api_key:
            client_args["api_key"] = api_key
            # Note: For simple text generation v1 is fine. 
            # If using experimental features, api_version='v1alpha' would be needed.
        else:
            # Fallback to ADC in Cloud Run
            client_args["vertexai"] = False 
            
        self.client = genai.Client(**client_args)
        self.model_id = settings.GEMINI_AUDIO_MODEL

    def _load_prompt(self, filename: str) -> str:
        """
        Carga el prompt desde un archivo Markdown específico en /prompts/.
        Cumple con el estándar 'Prompts as Code' definido en la Sección 10 de la Constitución.
        """
        prompt_path = os.path.join(os.path.dirname(__file__), "..", "prompts", filename)
        try:
            with open(prompt_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Documentación Premium: Los prompts deben estar limpios de comentarios de depuración
                return content.strip()
        except FileNotFoundError:
            logger.error(f"Error Crítico: El archivo de prompt '{filename}' no existe en {prompt_path}")
            return ""
        except Exception as e:
            logger.error(f"Fallo al leer el prompt '{filename}': {str(e)}")
            return ""

    async def enrich_text(self, text: str, provider: str) -> Tuple[str, bool]:
        """
        Enriquece el texto con etiquetas específicas de cada proveedor (SSML o Audio Tags).
        
        Sigue el principio de 'Director de Orquesta' definido en research.md:
        - ElevenLabs: Etiquetas entre corchetes [tag].
        - Google TTS: Etiquetas XML SSML.
        
        Args:
            text (str): Texto original solicitado por el usuario.
            provider (str): Identificador del proveedor (ELEVENLABS o GOOGLE).
            
        Returns:
            Tuple[str, bool]: (Texto procesado, Bandera de éxito). 
                              Si falla el LLM, retorna el texto original y False.
        """
        prompt_file = "google_enrichment.md" if provider == "GOOGLE" else "elevenlabs_enrichment.md"
        system_instruction = self._load_prompt(prompt_file)
        
        if not system_instruction:
            # Graceful degradation logic (Section 5.176 / Phase 6.T026)
            return text, False

        try:
            # Invocación al modelo Gemini utilizando el nuevo SDK unificado (Sección 1.16)
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=f"{system_instruction}\n\nTexto a enriquecer: {text}",
                config=types.GenerateContentConfig(
                    temperature=0.7,
                    max_output_tokens=2048
                )
            )
            
            if response and response.text:
                return response.text.strip(), True
            
            logger.warning(f"Gemini retornó una respuesta vacía al enriquecer para {provider}.")
            return text, False
            
        except Exception as e:
            # Manejo de errores detallado según la Constitución
            logger.error(f"Fallo en el servicio Gemini GenAI para {provider}: {str(e)}")
            return text, False


# Instancia única del servicio siguiendo el patrón de inyección de configuración
gemini_service = GeminiService(settings.GEMINI_AUDIO_API_KEY)
