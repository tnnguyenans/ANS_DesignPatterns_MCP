#!/usr/bin/env python3
"""
ANS Design Patterns MCP Server

A Python implementation of a Model Context Protocol (MCP) server that provides
design pattern documentation. The server responds to requests for specific 
design patterns by returning their markdown content.

Implements the Model Context Protocol (MCP) for integration with Windsurf and other AI tools.
"""

import os
import logging
from typing import Dict, List, Optional
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from dataclasses import dataclass
from pydantic import BaseModel

from mcp.server.fastmcp import FastMCP

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("ans-designpatterns")

# Default pattern directory
DEFAULT_PATTERN_DIR = os.path.join(os.path.dirname(__file__), "design-patterns")


class Config(BaseModel):
    """Configuration model for the MCP server."""
    base_dir: str = os.path.dirname(__file__)
    design_patterns_dir: str = DEFAULT_PATTERN_DIR


@dataclass
class AppContext:
    """Application context for the MCP server."""
    config: Config
    patterns: List[str]


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Manage application lifecycle with type-safe context."""
    # Load configuration
    config = load_config()
    logger.info(f"Using pattern directory: {config.design_patterns_dir}")
    
    # List available patterns
    patterns = []
    try:
        patterns = [f.replace('.md', '') for f in os.listdir(config.design_patterns_dir) 
                   if f.endswith('.md')]
        logger.info(f"Available patterns: {', '.join(patterns)}")
    except Exception as e:
        logger.error(f"Error listing patterns: {e}")
    
    # Create and yield the application context
    yield AppContext(config=config, patterns=patterns)


def load_config() -> Config:
    """Load configuration from config.json if available.
    
    Returns:
        Config: The loaded configuration or defaults.
    """
    try:
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                import json
                config_data = json.load(f)
            logger.info(f"Loaded configuration from {config_path}")
            return Config(**config_data)
    except Exception as e:
        logger.warning(f"Error loading config: {e}")
    
    logger.info("Using default configuration")
    return Config()


# Create an MCP server with lifespan
mcp = FastMCP(
    "ANS Design Patterns", 
    lifespan=app_lifespan,
    dependencies=["pydantic"]
)


@mcp.tool(title="Get Design Pattern")
def get_design_pattern(pattern: str) -> Dict[str, List[Dict[str, str]]]:
    """
    Get documentation for a specific design pattern.
    
    Args:
        pattern: The name of the design pattern to retrieve (e.g., 'singleton', 'factory')
    
    Returns:
        The design pattern documentation in markdown format
    """
    ctx = mcp.get_context()
    app_ctx = ctx.request_context.lifespan_context
    config = app_ctx.config
    
    pattern_dir = config.design_patterns_dir
    filename = os.path.join(pattern_dir, f"{pattern}.md")
    
    logger.info(f"Looking for pattern file: {filename}")
    
    if not os.path.exists(filename):
        logger.warning(f"Pattern file not found: {filename}")
        return {"content": [{"type": "text", "text": f'Pattern "{pattern}" not found.'}]}

    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
        logger.info(f"Successfully read pattern: {pattern}")
        return {"content": [{"type": "markdown", "text": text}]}
    except Exception as e:
        logger.error(f"Error reading pattern file: {e}")
        return {"content": [{"type": "text", "text": f'Error reading pattern "{pattern}": {str(e)}'}]}


@mcp.resource("design-pattern://{pattern_name}", title="Design Pattern")
def design_pattern_resource(pattern_name: str) -> str:
    """
    Get the content of a specific design pattern.
    
    Args:
        pattern_name: The name of the design pattern to retrieve
        
    Returns:
        The design pattern documentation in markdown format
    """
    ctx = mcp.get_context()
    app_ctx = ctx.request_context.lifespan_context
    config = app_ctx.config
    
    pattern_dir = config.design_patterns_dir
    filename = os.path.join(pattern_dir, f"{pattern_name}.md")
    
    if not os.path.exists(filename):
        return f"Pattern '{pattern_name}' not found."
    
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        logger.error(f"Error reading pattern file: {e}")
        return f"Error reading pattern '{pattern_name}': {str(e)}"


@mcp.resource("patterns://list", title="Available Design Patterns")
def list_patterns() -> str:
    """
    List all available design patterns.
    
    Returns:
        A markdown formatted list of all available design patterns
    """
    ctx = mcp.get_context()
    app_ctx = ctx.request_context.lifespan_context
    patterns = app_ctx.patterns
    
    if not patterns:
        return "No design patterns available."
    
    result = "# Available Design Patterns\n\n"
    for pattern in patterns:
        result += f"- [{pattern.capitalize()}](design-pattern://{pattern})\n"
    
    return result


if __name__ == "__main__":
    logger.info("ANS Design Patterns MCP Server starting...")
    # Run the server directly
    # For production, consider mounting to an ASGI server
    mcp.run()
