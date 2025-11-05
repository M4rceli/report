#!/usr/bin/env python3
"""
File Manager - Reporting System
Helper script for managing JSON files (auto-move from Downloads, list sections, etc.)
"""

import os
import sys
import time
import shutil
from pathlib import Path
from datetime import datetime

# Colors for terminal output (ANSI)
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'


class FileManager:
    def __init__(self, project_folder="c:/repos/report"):
        self.project_folder = Path(project_folder)
        self.saved_sections = self.project_folder / "saved_sections"
        self.downloads_folder = Path.home() / "Downloads"
        
        # Create folders if they don't exist
        self.saved_sections.mkdir(exist_ok=True)
    
    def find_json_files_in_downloads(self):
        """Find report JSON files in Downloads folder"""
        # Section patterns (individual sections)
        patterns = [
            'overall-assessment_*.json',
            'completeness-analysis_*.json',
            'accuracy-consistency_*.json',
            'action-plan_*.json',
            'report_complete_*.json',
            'data_quality_report_full_*.json'  # Full reports
        ]
        
        found_files = []
        for pattern in patterns:
            files = list(self.downloads_folder.glob(pattern))
            found_files.extend(files)
        
        return found_files
    
    def move_files_from_downloads(self):
        """Move JSON files from Downloads to saved_sections"""
        print(f"\n{Colors.BLUE}🔍 Searching for files in Downloads...{Colors.END}")
        
        files = self.find_json_files_in_downloads()
        
        if not files:
            print(f"{Colors.YELLOW}⚠️  No report files found in Downloads{Colors.END}")
            return 0
        
        print(f"\n{Colors.GREEN}✅ Found {len(files)} files:{Colors.END}")
        for file in files:
            print(f"  📄 {file.name}")
        
        # Confirmation
        confirm = input(f"\n{Colors.BOLD}Move these files? (y/n): {Colors.END}").strip().lower()
        
        if confirm != 'y':
            print(f"{Colors.YELLOW}❌ Operation cancelled{Colors.END}")
            return 0
        
        # Move files
        moved_count = 0
        for file in files:
            try:
                dest = self.saved_sections / file.name
                
                # If file exists, add timestamp
                if dest.exists():
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                    base_name = dest.stem
                    dest = self.saved_sections / f"{base_name}_{timestamp}.json"
                
                shutil.move(str(file), str(dest))
                print(f"  {Colors.GREEN}✅ Moved:{Colors.END} {file.name} → {dest.name}")
                moved_count += 1
            except Exception as e:
                print(f"  {Colors.RED}❌ Error:{Colors.END} {file.name} - {e}")
        
        print(f"\n{Colors.GREEN}✅ Successfully moved {moved_count} files!{Colors.END}")
        return moved_count
    
    def list_saved_sections(self):
        """Display list of saved sections"""
        print(f"\n{Colors.BLUE}📋 Saved Sections:{Colors.END}")
        print("=" * 60)
        
        json_files = list(self.saved_sections.glob("*.json"))
        
        if not json_files:
            print(f"{Colors.YELLOW}⚠️  No saved sections found{Colors.END}")
            return
        
        # Sort by modification date
        json_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
        
        print(f"\n{Colors.GREEN}Found {len(json_files)} files:{Colors.END}\n")
        
        for file in json_files:
            modified = datetime.fromtimestamp(file.stat().st_mtime)
            size_kb = file.stat().st_size / 1024
            
            print(f"  📄 {Colors.BOLD}{file.name}{Colors.END}")
            print(f"     Modified: {modified.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"     Size: {size_kb:.1f} KB")
            print()
    
    def watch_downloads(self, interval=5):
        """Watch Downloads folder for new files and auto-move"""
        print(f"\n{Colors.BLUE}👀 Watching Downloads folder...{Colors.END}")
        print(f"   Interval: {interval} seconds")
        print(f"   Press Ctrl+C to stop\n")
        
        seen_files = set(self.find_json_files_in_downloads())
        
        try:
            while True:
                time.sleep(interval)
                current_files = set(self.find_json_files_in_downloads())
                new_files = current_files - seen_files
                
                if new_files:
                    print(f"\n{Colors.GREEN}✅ New file detected!{Colors.END}")
                    for file in new_files:
                        try:
                            dest = self.saved_sections / file.name
                            if dest.exists():
                                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                                base_name = dest.stem
                                dest = self.saved_sections / f"{base_name}_{timestamp}.json"
                            
                            shutil.move(str(file), str(dest))
                            print(f"  {Colors.GREEN}✅ Auto-moved:{Colors.END} {file.name}")
                        except Exception as e:
                            print(f"  {Colors.RED}❌ Error:{Colors.END} {e}")
                    
                    seen_files = current_files
                else:
                    print(f"{Colors.BLUE}.{Colors.END}", end='', flush=True)
        
        except KeyboardInterrupt:
            print(f"\n\n{Colors.YELLOW}👋 Stopped watching{Colors.END}")


def main():
    """Main program function"""
    print("=" * 60)
    print(f"{Colors.BOLD}   File Manager - Reporting System{Colors.END}")
    print("=" * 60)
    
    manager = FileManager()
    
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "move":
            manager.move_files_from_downloads()
        elif command == "list":
            manager.list_saved_sections()
        elif command == "watch":
            interval = int(sys.argv[2]) if len(sys.argv) > 2 else 5
            manager.watch_downloads(interval)
        else:
            print(f"{Colors.RED}❌ Unknown command: {command}{Colors.END}")
            print("\nAvailable commands:")
            print("  python file_manager.py move         - Move files from Downloads")
            print("  python file_manager.py list         - List saved sections")
            print("  python file_manager.py watch [sec]  - Watch Downloads (auto-move)")
    else:
        # Interactive mode
        print(f"\n{Colors.BOLD}1.{Colors.END} Move files from Downloads")
        print(f"{Colors.BOLD}2.{Colors.END} List saved sections")
        print(f"{Colors.BOLD}3.{Colors.END} Watch Downloads folder")
        print(f"{Colors.BOLD}0.{Colors.END} Exit")
        
        choice = input(f"\n{Colors.BOLD}Select option: {Colors.END}").strip()
        
        if choice == "1":
            manager.move_files_from_downloads()
        elif choice == "2":
            manager.list_saved_sections()
        elif choice == "3":
            manager.watch_downloads()
        elif choice == "0":
            print("Closing...")
        else:
            print(f"{Colors.RED}❌ Invalid option{Colors.END}")


if __name__ == "__main__":
    main()
