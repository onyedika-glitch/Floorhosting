#!/usr/bin/env python3
"""
Script to add shared CSS and JS links to all HTML pages
"""

import os
from pathlib import Path

base_dir = Path.cwd()

# Define files to update and where to insert the links
files_to_update = [
    'pages/auth/auth.html',
    'pages/dashboard/dashboard.html',
    'pages/dashboard/profile.html',
    'pages/dashboard/domains.html',
    'pages/services/services.html',
    'pages/services/services-list.html',
    'pages/billing/billing.html',
    'pages/billing/add-payment-method.html',
    'pages/billing/invoice.html',
    'pages/billing/payment-checkout.html',
    'pages/account/manage.html',
    'pages/account/renew.html',
    'pages/info/about.html',
    'pages/info/faq.html',
    'pages/info/support.html',
]

def add_shared_assets(file_path):
    """Add shared CSS and JS links to a file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if shared assets are already linked
        if '../../assets/css/style.css' in content and '../../assets/js/main.js' in content:
            print(f"~ Already has shared assets: {file_path.relative_to(base_dir)}")
            return False
        
        # Find the closing </head> tag
        head_close = content.find('</head>')
        if head_close == -1:
            print(f"✗ No closing </head> found in: {file_path.relative_to(base_dir)}")
            return False
        
        # Add CSS link before </head> if not already there
        css_link = '    <link rel="stylesheet" href="../../assets/css/style.css">\n'
        if '../../assets/css/style.css' not in content:
            content = content[:head_close] + css_link + content[head_close:]
            head_close += len(css_link)
        
        # Find the closing </body> tag
        body_close = content.rfind('</body>')
        if body_close == -1:
            print(f"✗ No closing </body> found in: {file_path.relative_to(base_dir)}")
            return False
        
        # Add JS script before </body> if not already there
        js_script = '    <script src="../../assets/js/main.js"></script>\n'
        if '../../assets/js/main.js' not in content:
            content = content[:body_close] + js_script + content[body_close:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Added shared assets to: {file_path.relative_to(base_dir)}")
        return True
    except Exception as e:
        print(f"✗ Error processing {file_path.relative_to(base_dir)}: {e}")
        return False

def main():
    """Main function to add shared assets to all pages"""
    total_updated = 0
    
    for file_path_str in files_to_update:
        file_path = base_dir / file_path_str
        
        if not file_path.exists():
            print(f"✗ File not found: {file_path_str}")
            continue
        
        if add_shared_assets(file_path):
            total_updated += 1
    
    print(f"\nTotal files updated: {total_updated}")

if __name__ == '__main__':
    main()
