#!/usr/bin/env python3
"""
Script to update all HTML file links to reflect new directory structure
"""

import os
import re
from pathlib import Path

# Define the base directory
base_dir = Path.cwd()

# Define replacements for different directory levels
replacements = {
    'pages/dashboard': {
        'href="index.html"': 'href="../../index.html"',
        'href="services.html"': 'href="../services/services.html"',
        'href="about.html"': 'href="../info/about.html"',
        'href="faq.html"': 'href="../info/faq.html"',
        'href="auth.html"': 'href="../auth/auth.html"',
        'href="support.html"': 'href="../info/support.html"',
        'href="services-list.html"': 'href="../services/services-list.html"',
        'href="billing.html"': 'href="../billing/billing.html"',
        'href="dashboard.html"': 'href="./dashboard.html"',
        'href="profile.html"': 'href="./profile.html"',
        'href="domains.html"': 'href="./domains.html"',
        'window.location.href = "dashboard.html"': 'window.location.href = "./dashboard.html"',
    },
    'pages/services': {
        'href="index.html"': 'href="../../index.html"',
        'href="services.html"': 'href="./services.html"',
        'href="about.html"': 'href="../info/about.html"',
        'href="faq.html"': 'href="../info/faq.html"',
        'href="auth.html"': 'href="../auth/auth.html"',
        'href="dashboard.html"': 'href="../dashboard/dashboard.html"',
        'window.location.href = "dashboard.html"': 'window.location.href = "../dashboard/dashboard.html"',
    },
    'pages/billing': {
        'href="index.html"': 'href="../../index.html"',
        'href="billing.html"': 'href="./billing.html"',
        'href="add-payment-method.html"': 'href="./add-payment-method.html"',
        'href="invoice.html"': 'href="./invoice.html"',
        'href="payment-checkout.html"': 'href="./payment-checkout.html"',
        'href="dashboard.html"': 'href="../dashboard/dashboard.html"',
        'href="services.html"': 'href="../services/services.html"',
        'href="about.html"': 'href="../info/about.html"',
        'href="support.html"': 'href="../info/support.html"',
    },
    'pages/account': {
        'href="index.html"': 'href="../../index.html"',
        'href="manage.html"': 'href="./manage.html"',
        'href="renew.html"': 'href="./renew.html"',
        'href="billing.html"': 'href="../billing/billing.html"',
        'href="dashboard.html"': 'href="../dashboard/dashboard.html"',
        'href="payment-checkout.html"': 'href="../billing/payment-checkout.html"',
    },
    'pages/info': {
        'href="index.html"': 'href="../../index.html"',
        'href="about.html"': 'href="./about.html"',
        'href="faq.html"': 'href="./faq.html"',
        'href="support.html"': 'href="./support.html"',
        'href="services.html"': 'href="../services/services.html"',
        'href="auth.html"': 'href="../auth/auth.html"',
        'href="dashboard.html"': 'href="../dashboard/dashboard.html"',
    },
}

def update_file(file_path, rep_dict):
    """Update a single HTML file with replacements"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        for old, new in rep_dict.items():
            content = content.replace(old, new)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Main function to update all HTML files"""
    total_updated = 0
    
    for directory, rep_dict in replacements.items():
        dir_path = base_dir / directory
        
        if not dir_path.exists():
            print(f"Directory not found: {dir_path}")
            continue
        
        # Find all HTML files in this directory
        html_files = list(dir_path.glob('*.html'))
        
        for html_file in html_files:
            if update_file(html_file, rep_dict):
                print(f"✓ Updated: {html_file.relative_to(base_dir)}")
                total_updated += 1
            else:
                print(f"- No changes: {html_file.relative_to(base_dir)}")
    
    print(f"\nTotal files updated: {total_updated}")

if __name__ == '__main__':
    main()
