from mcp.server.fastmcp import FastMCP
from pydantic import Field
from services.audio_service import audio_service
import asyncio

"""
Servidor MCP para la Generación de Audio (Que Vino Audio MCP).
Expone las capacidades de TTS como herramientas (Tools) para Agentes A2A.
Cumple con la Sección 2.4 de la Constitución.
"""

mcp = FastMCP("QueVinoAudio")

@mcp.tool()
async def list_voices_tool() -> str:
    """
    Obtiene la lista unificada de voces disponibles de todos los proveedores (Google y ElevenLabs).
    Útil para que el agente elija una voz adecuada para el contexto emocional.
    """
    try:
        voices = await audio_service.get_all_voices()
        return f"Voces disponibles: {voices}"
    except Exception as e:
        return f"Error al al listar voces: {str(e)}"

@mcp.tool()
async def list_models_tool() -> str:
    """
    Lista los modelos de síntesis de audio disponibles.
    Permite elegir entre modelos multilingües (ElevenLabs) o técnicos (Google).
    """
    try:
        models = await audio_service.get_all_models()
        return f"Modelos disponibles: {models}"
    except Exception as e:
        return f"Error al listar modelos: {str(e)}"

@mcp.tool()
async def generate_audio_tool(
    text: str, 
    provider: str, 
    voice_id: str, 
    enrich_audio: bool = True
) -> str:
    """
    Genera un archivo de audio a partir de texto utilizando el proveedor seleccionado.
    El audio se guarda automáticamente en el repositorio de auditoría (GCS).
    
    Args:
        text (str): El mensaje a convertir en voz.
        provider (str): 'ELEVENLABS' o 'GOOGLE'.
        voice_id (str): ID de la voz (ej: 'rachel', 'en-US-Standard-A').
        enrich_audio (bool): Si es True, Gemini inyectará tonos emocionales o etiquetas SSML.
        
    Returns:
        str: Un resumen con el Generation ID y el estatus del enriquecimiento.
    """
    try:
        # La lógica de MCP no puede devolver un stream binario fácilmente en el texto de la herramienta.
        # Por lo tanto, orquestamos la generación y devolvemos la referencia de auditoría.
        # El frontend/UI podrá recuperar el audio usando el Generation ID vía REST.
        
        _, metadata = await audio_service.generate_audio(
            text=text,
            provider_key=provider.upper(),
            voice_id=voice_id,
            output_format="mp3",
            enrich_audio=enrich_audio
        )
        
        # Nota: En un entorno productivo real, aquí deberíamos disparar también el BackgroundTask 
        # de subida a GCS si no lo hace ya el AudioService. Actualmente AudioService coordina pero 
        # main.py es quien dispara las tareas de fondo. 
        # Refactorizaremos AudioService para manejar la persistencia básica si se desea independencia total de MCP.
        
        res = (
            f"Audio generado exitosamente.\n"
            f"- Generation ID: {metadata['generation_id']}\n"
            f"- Estatus Enriquecimiento: {metadata['enrichment_status']}\n"
            f"- Path GCS (Audit): generations/{metadata['generation_id']}.mp3"
        )
        return res
    except Exception as e:
        return f"Error al generar audio: {str(e)}"

if __name__ == "__main__":
    mcp.run()
