#!/usr/bin/env python3
"""
ANS Design Patterns MCP Test Client

A simple test client for the ANS Design Patterns MCP server.
This client directly reads the design pattern files to verify they exist and are readable.
"""

import os
import json
import logging
from typing import List, Optional

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("test_client")

def load_config() -> dict:
    """Load configuration from config.json if available.
    
    Returns:
        dict: The loaded configuration or defaults.
    """
    try:
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        if os.path.exists(config_path):
            with open(config_path, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
            logger.info(f"Loaded configuration from {config_path}")
            return config_data
    except Exception as e:
        logger.warning(f"Error loading config: {e}")
    
    # Default config
    return {
        "baseDir": os.path.dirname(__file__),
        "designPatternsDir": os.path.join(os.path.dirname(__file__), "design-patterns")
    }

def get_available_patterns(pattern_dir: str) -> List[str]:
    """Get a list of available design patterns.
    
    Args:
        pattern_dir: The directory containing the design pattern files.
        
    Returns:
        List[str]: A list of available pattern names (without .md extension).
    """
    try:
        patterns = [f.replace('.md', '') for f in os.listdir(pattern_dir) 
                   if f.endswith('.md')]
        return patterns
    except Exception as e:
        logger.error(f"Error listing patterns: {e}")
        return []

def read_pattern(pattern_name: str, pattern_dir: str) -> Optional[str]:
    """Read a design pattern file.
    
    Args:
        pattern_name: The name of the pattern to read.
        pattern_dir: The directory containing the design pattern files.
        
    Returns:
        Optional[str]: The content of the pattern file, or None if not found.
    """
    file_path = os.path.join(pattern_dir, f"{pattern_name}.md")
    try:
        if not os.path.exists(file_path):
            logger.warning(f"Pattern file not found: {file_path}")
            return None
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        logger.info(f"Successfully read pattern: {pattern_name}")
        return content
    except Exception as e:
        logger.error(f"Error reading pattern file: {e}")
        return None

def main():
    """Main entry point for the test client."""
    logger.info("Starting test client...")
    
    # Load configuration
    config = load_config()
    pattern_dir = config.get("designPatternsDir")
    logger.info(f"Pattern directory: {pattern_dir}")
    
    # Get available patterns
    patterns = get_available_patterns(pattern_dir)
    if not patterns:
        logger.error("No patterns found!")
        return
    
    # Read the first pattern (usually singleton)
    first_pattern = patterns[0]
    logger.info(f"Reading {first_pattern} pattern...")
    content = read_pattern(first_pattern, pattern_dir)
    
    if content:
        print(f"{first_pattern.title()} pattern content:")
        print("----------------------------")
        print(content)
        print("----------------------------")
    
    # List all available patterns
    print("\nListing all available patterns:")
    for pattern in patterns:
        print(f"- {pattern}.md")

if __name__ == "__main__":
    main()
