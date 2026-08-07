#!/usr/bin/env python3
"""
Link Checker for MyDoc Repository
Scans markdown files for broken internal links
"""

import os
import re
from pathlib import Path

def find_broken_links(root_dir='.'):
    """Find all broken internal markdown links"""
    broken_links = []
    total_links = 0
    
    # Key files to check thoroughly
    priority_files = [
        'README.md',
        'QUICK-START.md', 
        'GLOSSARY.md',
        'guides/README.md',
        'domains/backend-dev/README.md',
        'domains/game-dev/README.md',
        'domains/ai-ml/README.md',
    ]
    
    for file_path in priority_files:
        if not os.path.exists(file_path):
            print(f"⚠️  File not found: {file_path}")
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all relative markdown links
        pattern = r'\[([^\]]+)\]\((\./[^)]+\.md|\.\./[^)]+\.md)\)'
        matches = re.findall(pattern, content)
        
        for link_text, link_path in matches:
            total_links += 1
            
            # Remove any anchors (#section)
            clean_path = link_path.split('#')[0]
            
            # Calculate absolute path
            file_dir = os.path.dirname(file_path)
            target_path = os.path.normpath(os.path.join(file_dir, clean_path))
            
            if not os.path.exists(target_path):
                broken_links.append({
                    'file': file_path,
                    'link_text': link_text,
                    'link_path': link_path,
                    'target': target_path
                })
    
    return broken_links, total_links

def main():
    print("🔍 MyDoc Link Audit")
    print("=" * 60)
    
    broken, total = find_broken_links()
    
    if not broken:
        print(f"✅ SUCCESS! All {total} links are valid!")
        print("\n📊 Files checked:")
        print("   - README.md")
        print("   - QUICK-START.md")
        print("   - GLOSSARY.md")
        print("   - Key domain READMEs")
        return
    
    print(f"❌ Found {len(broken)} broken links out of {total} total links\n")
    
    # Group by source file
    by_file = {}
    for item in broken:
        file = item['file']
        if file not in by_file:
            by_file[file] = []
        by_file[file].append(item)
    
    # Print report
    for file, items in by_file.items():
        print(f"\n📄 {file} ({len(items)} broken):")
        for item in items:
            print(f"   ❌ [{item['link_text']}]({item['link_path']})")
            print(f"      → Target not found: {item['target']}")
    
    print("\n" + "=" * 60)
    print(f"📊 Summary: {len(broken)}/{total} links broken ({len(broken)/total*100:.1f}%)")
    
    # Save report
    with open('meta/ops/LINK_AUDIT_REPORT.md', 'w', encoding='utf-8') as f:
        f.write("# Link Audit Report\n\n")
        f.write(f"**Date:** {os.popen('date /t').read().strip()}\n\n")
        f.write(f"**Summary:** {len(broken)} broken links found out of {total} total links\n\n")
        
        if broken:
            f.write("## Broken Links\n\n")
            for file, items in by_file.items():
                f.write(f"### {file}\n\n")
                for item in items:
                    f.write(f"- ❌ `[{item['link_text']}]({item['link_path']})`\n")
                    f.write(f"  - Target: `{item['target']}`\n\n")
        else:
            f.write("✅ All links are valid!\n")
    
    print("\n💾 Report saved to: meta/ops/LINK_AUDIT_REPORT.md")

if __name__ == '__main__':
    main()
