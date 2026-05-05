import os
from google.cloud import speech_v1p1beta1 as speech
from typing import BinaryIO

class STTService:
    def __init__(self):
        # Google Cloud credentials should be set in environment
        # GOOGLE_APPLICATION_CREDENTIALS points to the service account JSON
        self.client = speech.SpeechClient()

    async def transcribe(self, audio_content: bytes, language_code: str = "en-IN") -> tuple[str, float]:
        """
        Transcribes audio bytes to text using Google Cloud STT.
        Returns a tuple of (transcript, confidence_score).
        """
        audio = speech.RecognitionAudio(content=audio_content)
        
        # Configure for Hinglish support by adding alternative language codes
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.WEBM_OPUS, # Common for browser MediaRecorder
            sample_rate_hertz=48000,
            language_code=language_code,
            alternative_language_codes=["hi-IN"],
            enable_automatic_punctuation=True,
            model="latest_long", # Or "command_and_search" for short clips
        )

        # Note: In a production environment, this should be an async call.
        # speech.SpeechClient doesn't have a built-in async version in the same way,
        # usually run in a thread pool if needed, or use the gapic async client if available.
        # For now, we'll keep it simple as it's foundational.
        
        response = self.client.recognize(config=config, audio=audio)

        if not response.results:
            return "", 0.0

        # Get the best alternative from the first result
        best_alternative = response.results[0].alternatives[0]
        return best_alternative.transcript, best_alternative.confidence

stt_service = STTService()
