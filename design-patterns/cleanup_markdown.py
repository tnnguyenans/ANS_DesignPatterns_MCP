#!/usr/bin/env python3
"""
Cleanup script to remove Russian language content and EN: prefixes from generated markdown files
"""

import os
import re
from pathlib import Path

class MarkdownCleaner:
    def __init__(self):
        self.base_dir = Path(r"C:\Programs\PythonTraining\ANS_DesignPatterns_MCP\design-patterns")
        self.processed_files = []
        
    def clean_content(self, content):
        """Clean content by removing Russian text and EN: prefixes"""
        lines = content.split('\n')
        cleaned_lines = []
        skip_until_next_section = False
        
        for i, line in enumerate(lines):
            original_line = line
            
            # Skip lines that are primarily Russian content
            if any(keyword in line for keyword in ['RU:', 'Назначение:', 'Паттерн', 'Конкретные', 'Абстрактная Фабрика', 'объектов']):
                skip_until_next_section = True
                continue
                
            # Stop skipping when we hit an EN: line or structural element
            if skip_until_next_section:
                if (line.strip().startswith('EN:') or 
                    line.strip().startswith('class ') or 
                    line.strip().startswith('def ') or
                    line.strip().startswith('from ') or
                    line.strip().startswith('import ') or
                    line.strip().startswith('#include') or
                    line.strip().startswith('*/') or
                    line.strip() == '' or
                    '```' in line):
                    skip_until_next_section = False
                else:
                    continue
            
            # Remove EN: prefixes
            line = re.sub(r'\s*EN:\s*', '', line)
            
            # Remove RU: prefixes and content
            line = re.sub(r'\s*RU:\s*.*', '', line)
            
            # Remove Russian text patterns (Cyrillic characters)
            line = re.sub(r'[А-Яа-я]+.*', '', line)
            
            # Remove specific Russian words and phrases
            russian_patterns = [
                r'Назначение:.*',
                r'Паттерн.*',
                r'собственный класс.*',
                r'исполнения программы.*',
                r'Конкретные.*',
                r'Абстрактная.*',
                r'объектов.*',
                r'интерфейс.*',
                r'алгоритмов.*'
            ]
            
            for pattern in russian_patterns:
                line = re.sub(pattern, '', line, flags=re.IGNORECASE)
            
            # Clean up extra whitespace and empty comment lines
            line = re.sub(r'^\s*\*\s*$', '', line)  # Remove empty comment lines
            line = re.sub(r'^\s*//\s*$', '', line)  # Remove empty C++ comment lines
            line = re.sub(r'^\s*#\s*$', '', line)   # Remove empty Python comment lines
            
            # Don't add completely empty lines that result from cleaning
            if line.strip() or original_line.strip() == '':
                cleaned_lines.append(line)
        
        # Join lines and clean up multiple consecutive empty lines
        content = '\n'.join(cleaned_lines)
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)  # Replace multiple empty lines with double
        
        return content
    
    def clean_file(self, file_path):
        """Clean a single markdown file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            cleaned_content = self.clean_content(content)
            
            # Only write if content changed
            if cleaned_content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(cleaned_content)
                print(f"[OK] Cleaned {file_path.name}")
                self.processed_files.append(file_path.name)
                return True
            else:
                print(f"[-] No changes needed for {file_path.name}")
                return False
                
        except Exception as e:
            print(f"[ERROR] Error processing {file_path.name}: {e}")
            return False
    
    def clean_all_markdown_files(self):
        """Clean all markdown files in the directory"""
        print("Starting cleanup of markdown files...")
        print(f"Directory: {self.base_dir}")
        print()
        
        # Find all markdown files except the original templates and readme
        markdown_files = []
        for file_path in self.base_dir.glob("*.md"):
            # Skip the original template files and readme
            if file_path.name not in ['singleton.md', 'singleton_threadsafe.md', 'README_Generation_Summary.md']:
                markdown_files.append(file_path)
        
        if not markdown_files:
            print("No markdown files found to clean.")
            return
        
        print(f"Found {len(markdown_files)} markdown files to process:")
        for f in sorted(markdown_files):
            print(f"  - {f.name}")
        print()
        
        cleaned_count = 0
        for file_path in sorted(markdown_files):
            if self.clean_file(file_path):
                cleaned_count += 1
        
        print(f"\nCleanup completed!")
        print(f"Files processed: {len(markdown_files)}")
        print(f"Files modified: {cleaned_count}")
        
        if self.processed_files:
            print(f"\nModified files:")
            for filename in sorted(self.processed_files):
                print(f"  [OK] {filename}")

if __name__ == "__main__":
    cleaner = MarkdownCleaner()
    cleaner.clean_all_markdown_files()
