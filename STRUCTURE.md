<!-- File Organization Guide -->

DIRECTORY STRUCTURE:
===================

floor-hosting/
│
├── 📄 index.html                      # Landing/Home Page
├── 📄 README.md                       # Project Documentation
├── 📄 .htaccess                       # Server Configuration
│
├── 📁 pages/                          # All Application Pages
│   │
│   ├── 📁 auth/
│   │   └── auth.html                  # Login & Registration
│   │
│   ├── 📁 dashboard/
│   │   ├── dashboard.html             # Main User Dashboard
│   │   ├── profile.html               # User Profile Settings
│   │   └── domains.html               # Domain Management
│   │
│   ├── 📁 services/
│   │   ├── services.html              # Service Plans Display
│   │   └── services-list.html         # All Services Listing
│   │
│   ├── 📁 billing/
│   │   ├── billing.html               # Billing Overview
│   │   ├── add-payment-method.html    # Add Payment Method
│   │   ├── invoice.html               # View Invoice Details
│   │   └── payment-checkout.html      # Payment Processing
│   │
│   ├── 📁 account/
│   │   ├── manage.html                # Service Management
│   │   └── renew.html                 # Service Renewal Wizard
│   │
│   └── 📁 info/
│       ├── about.html                 # About Company
│       ├── faq.html                   # FAQ Section
│       └── support.html               # Support & Help
│
├── 📁 assets/                         # Static Assets
│   │
│   ├── 📁 css/
│   │   └── style.css                  # Global Stylesheet (shared)
│   │
│   ├── 📁 js/
│   │   └── main.js                    # JavaScript Utilities (shared)
│   │
│   └── 📁 img/
│       └── (images, logos, icons)
│
└── 📁 .git/                           # Git Version Control


NAVIGATION MAP:
===============

HOME (index.html)
├── Authentication (pages/auth/auth.html)
│   └── Dashboard (pages/dashboard/dashboard.html)
│       ├── Profile (pages/dashboard/profile.html)
│       ├── Domains (pages/dashboard/domains.html)
│       ├── Manage Services (pages/account/manage.html)
│       │   └── Renew Service (pages/account/renew.html)
│       │       └── Payment Checkout (pages/billing/payment-checkout.html)
│       ├── Billing (pages/billing/billing.html)
│       │   ├── Add Payment (pages/billing/add-payment-method.html)
│       │   └── View Invoice (pages/billing/invoice.html)
│       │       └── Checkout (pages/billing/payment-checkout.html)
│       └── Services (pages/services/services.html)
│
├── Services (pages/services/services.html)
├── About (pages/info/about.html)
├── FAQ (pages/info/faq.html)
└── Support (pages/info/support.html)


PAGE PURPOSES:
==============

AUTHENTICATION
- auth.html: Handles user registration and login

DASHBOARD (Protected - Requires Login)
- dashboard.html: Main hub after login, shows overview
- profile.html: User personal information and settings
- domains.html: Domain management interface

SERVICES
- services.html: Showcase of available hosting plans
- services-list.html: Detailed listing of all services

BILLING & PAYMENTS
- billing.html: Invoice history and payment methods overview
- add-payment-method.html: Credit card, PayPal, Bank Transfer forms
- invoice.html: Detailed invoice viewer with PDF option
- payment-checkout.html: Final payment processing

ACCOUNT MANAGEMENT
- manage.html: Service management and settings
- renew.html: 3-step subscription renewal wizard

INFORMATION
- about.html: Company information and team
- faq.html: Frequently asked questions
- support.html: Help and support resources


SHARED RESOURCES:
================

CSS (assets/css/style.css):
- Global color variables
- Typography styles
- Button styles
- Form controls
- Cards and alerts
- Responsive utilities
- Layout helpers

JavaScript (assets/js/main.js):
- Mobile menu toggle
- Form validation
- Currency/Date formatting
- localStorage helpers
- User authentication state
- Alert notifications
- Navigation active states


LINK PATTERNS:
==============

From index.html (root):
- To dashboard: <a href="pages/dashboard/dashboard.html">
- To auth: <a href="pages/auth/auth.html">
- To services: <a href="pages/services/services.html">

From dashboard pages (pages/dashboard/):
- To auth: <a href="../auth/auth.html">
- To billing: <a href="../billing/billing.html">
- To styles: <link href="../../assets/css/style.css">
- To js: <script src="../../assets/js/main.js">

From nested pages (pages/billing/):
- To dashboard: <a href="../dashboard/dashboard.html">
- To styles: <link href="../../assets/css/style.css">
- To js: <script src="../../assets/js/main.js">


DEPLOYMENT:
===========

Development:
1. All files in local folder
2. Use Python/Node/PHP server
3. Test all links

Production:
1. Upload all files (maintaining structure)
2. Ensure .htaccess is present
3. Enable Apache mod_rewrite
4. Set proper file permissions
5. Enable HTTPS


NOTES:
======

✓ All pages share style.css and main.js
✓ Each page is self-contained (no dependencies)
✓ localStorage used for data persistence
✓ Responsive design works on all devices
✓ No database needed for demo
✓ Easy to add new pages in appropriate folders
✓ Clear file organization for scaling
