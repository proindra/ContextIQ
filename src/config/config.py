"""Configuration module for Agentic RAG system"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for RAG system"""
    
    # API configuration
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    
    # Model Configuration
    LLM_MODEL = os.getenv("GROQ_MODEL", "qwen/qwen3.8-27b")
    
    # Document Processing
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 50
    
    # Default URLs
    DEFAULT_URLS = [
        "https://lilianweng.github.io/posts/2023-06-23-agent/",
        "https://lilianweng.github.io/posts/2024-04-12-diffusion-video/"
    ]
    
    @classmethod
    def get_llm(cls):
        """Initialize and return the LLM model"""
        if not cls.GROQ_API_KEY:
            raise RuntimeError(
                "GROQ_API_KEY is not set. Add it to your .env file or environment."
            )
        return ChatGroq(model=cls.LLM_MODEL, api_key=cls.GROQ_API_KEY)