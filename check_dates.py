#!/usr/bin/env python3
"""
Check "Last Updated" dates in markdown files to identify outdated content.

Usage:
    python check_dates.py [--threshold MONTHS]

Example:
    python check_dates.py --threshold 3  # Find files older than 3 months
"""

import os
import re
from datetime import datetime, timedelta
from pathlib import Path
import argparse

# Month name to number mapping
MONTH_MAP = {
    'january': 1, 'february': 2, 'march': 3, 'april': 4,
    'may': 5, 'june': 6, 'july': 7, 'august': 8,
    'september': 9, 'october': 10, 'november': 11, 'december': 12
}

def parse_date(date_string):
    """
    Parse date string like "February 2026" or "Feb 2026"
    Returns datetime object or None if parsing fails
    """
    date_string = date_string.strip().lower()
    
    # Try to match "Month Year" pattern
    match = re.match(r'([a-z]+)\s+(\d{4})', date_string)
    if not match:
        return None
    
    month_str, year_str = match.groups()
    
    # Find month number
    month_num = None
    for full_month, num in MONTH_MAP.items():
        if full_month.startswith(month_str):
            month_num = num
            break
    
    if not month_num:
        return None
    
    try:
        return datetime(int(year_str), month_num, 1)
    except ValueError:
        return None

def extract_last_updated(file_path):
    """
    Extract "Last Updated" date from markdown file.
    Returns (date_string, datetime_obj) or (None, None)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for pattern: > **Last Updated:** Month Year
        pattern = r'>\s*\*\*Last Updated:\*\*\s+([A-Za-z]+\s+\d{4})'
        match = re.search(pattern, content)
        
        if match:
            date_str = match.group(1)
            date_obj = parse_date(date_str)
            return (date_str, date_obj)
        
        return (None, None)
    except Exception as e:
        print(f"⚠️  Error reading {file_path}: {e}")
        return (None, None)

def get_age_description(date_obj, current_date):
    """Return human-readable age description"""
    if not date_obj:
        return "Unknown"
    
    diff = current_date - date_obj
    months = diff.days // 30
    
    if months == 0:
        return "This month"
    elif months == 1:
        return "1 month ago"
    else:
        return f"{months} months ago"

def scan_directory(directory, extensions=['.md'], exclude_dirs=None):
    """
    Recursively scan directory for markdown files with "Last Updated" dates.
    Returns list of (file_path, date_string, datetime_obj)
    """
    if exclude_dirs is None:
        exclude_dirs = {'.git', 'node_modules', '__pycache__', '.vscode', '.cursor'}
    
    results = []
    
    for root, dirs, files in os.walk(directory):
        # Remove excluded directories from traversal
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = Path(root) / file
                date_str, date_obj = extract_last_updated(file_path)
                
                if date_str and date_obj:
                    results.append((file_path, date_str, date_obj))
    
    return results

def main():
    parser = argparse.ArgumentParser(
        description='Check "Last Updated" dates in markdown files'
    )
    parser.add_argument(
        '--threshold',
        type=int,
        default=3,
        help='Months threshold for outdated content (default: 3)'
    )
    parser.add_argument(
        '--directory',
        type=str,
        default='.',
        help='Directory to scan (default: current directory)'
    )
    
    args = parser.parse_args()
    
    print("🔍 Checking 'Last Updated' dates...")
    print("=" * 60)
    
    # Scan for files with dates
    results = scan_directory(args.directory)
    
    if not results:
        print("\n⚠️  No files found with 'Last Updated' dates.")
        print("💡 Make sure files contain: > **Last Updated:** Month Year")
        return
    
    # Calculate threshold date
    current_date = datetime.now()
    threshold_date = current_date - timedelta(days=args.threshold * 30)
    
    # Categorize files
    outdated = []
    fresh = []
    
    for file_path, date_str, date_obj in results:
        rel_path = file_path.relative_to(args.directory)
        age_desc = get_age_description(date_obj, current_date)
        
        if date_obj < threshold_date:
            outdated.append((rel_path, date_str, age_desc))
        else:
            fresh.append((rel_path, date_str, age_desc))
    
    # Display results
    if outdated:
        print(f"\n⚠️  FILES NEEDING REVIEW (>{args.threshold} months old):\n")
        for file_path, date_str, age_desc in sorted(outdated):
            print(f"{file_path}")
            print(f"  Last Updated: {date_str} ({age_desc})")
            print()
    
    if fresh:
        print(f"\n✅ FRESH FILES (≤{args.threshold} months old):\n")
        for file_path, date_str, age_desc in sorted(fresh):
            print(f"{file_path}")
            print(f"  Last Updated: {date_str} ({age_desc})")
            print()
    
    # Summary
    print("=" * 60)
    print(f"✅ FRESH FILES: {len(fresh)}")
    print(f"⚠️  NEEDS REVIEW: {len(outdated)}")
    print(f"📊 TOTAL TRACKED: {len(results)}")
    
    if outdated:
        print(f"\n💡 TIP: Review outdated files and update content/dates")
        print(f"📖 See MAINTENANCE.md for quarterly review process")
        return 1  # Exit code 1 if outdated files found
    else:
        print(f"\n🎉 All files are up to date!")
        return 0

if __name__ == '__main__':
    exit(main())
