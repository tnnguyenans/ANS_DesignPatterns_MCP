#!/usr/bin/env python3
"""
Direct Test for ANS Design Patterns MCP Server

This script directly reads design pattern files from the design-patterns directory
and prints their contents to verify they can be accessed correctly.
"""

import json
import os
import sys
from typing import Dict, Any, Optional

def read_design_pattern(pattern_name: str) -> Optional[str]:
    """Read a design pattern file directly.
    
    Args:
        pattern_name: The name of the design pattern to read.
        
    Returns:
        str: The content of the design pattern file, or None if not found.
    """
    # Default pattern directory
    pattern_dir = os.path.join(os.path.dirname(__file__), "design-patterns")
    
    # Try to load from config.json if available
    config_path = os.path.join(os.path.dirname(__file__), 'config.json')
    if os.path.exists(config_path):
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config_data = json.load(f)
                if 'design_patterns_dir' in config_data:
                    pattern_dir = config_data['design_patterns_dir']
        except Exception as e:
            print(f"Error loading config: {e}")
    
    # Build the full path to the pattern file
    filename = os.path.join(pattern_dir, f"{pattern_name}.md")
    
    print(f"Looking for pattern file: {filename}")
    
    if not os.path.exists(filename):
        print(f"Pattern file not found: {filename}")
        return None
    
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"Successfully read pattern: {pattern_name}")
        return content
    except Exception as e:
        print(f"Error reading pattern file: {e}")
        return None

def main():
    """Main entry point for the test script."""
    print("Direct Test for ANS Design Patterns MCP Server")
    print("--------------------------------------------")
    
    # Test with singleton pattern
    print("\nTesting with 'singleton' pattern:")
    content = read_design_pattern("singleton")
    if content:
        print("\nPattern content (first 100 chars):")
        print(content[:100] + "...")
        print(f"\nTotal content length: {len(content)} characters")
    
    # Test with factory pattern
    print("\nTesting with 'factory' pattern:")
    content = read_design_pattern("factory")
    if content:
        print("\nPattern content (first 100 chars):")
        print(content[:100] + "...")
        print(f"\nTotal content length: {len(content)} characters")
    
    # Test with non-existent pattern
    print("\nTesting with non-existent pattern:")
    content = read_design_pattern("nonexistent")
    if content is None:
        print("Pattern not found, as expected.")

if __name__ == "__main__":
    main()
