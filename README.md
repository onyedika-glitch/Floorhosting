# Floor Hosting - Web Hosting Control Panel

A modern, responsive web hosting control panel frontend built with HTML5, Tailwind CSS, and Vanilla JavaScript.

## 📋 Project Overview

Floor Hosting is a professional hosting management platform that allows users to:
- Manage their hosting services and subscriptions
- Track billing and payment history
- Renew and upgrade services
- View and download invoices
- Add and manage payment methods
- Access 24/7 support resources

## 📁 Project Structure

```
floor-hosting/
├── index.html                    # Landing page
├── pages/                        # All page templates
│   ├── auth/
│   │   └── auth.html            # Login & Registration
│   ├── dashboard/
│   │   ├── dashboard.html       # Main dashboard
│   │   ├── profile.html         # User profile
│   │   └── domains.html         # Domain management
│   ├── services/
│   │   ├── services.html        # Services showcase
│   │   └── services-list.html   # Service listings
│   ├── billing/
│   │   ├── billing.html         # Billing overview
│   │   ├── add-payment-method.html
│   │   ├── invoice.html         # Invoice viewer
│   │   └── payment-checkout.html
│   ├── account/
│   │   ├── manage.html          # Service management
│   │   └── renew.html           # Renewal wizard
│   └── info/
│       ├── about.html           # About company
│       ├── faq.html             # FAQ
│       └── support.html         # Support resources
├── assets/
│   ├── css/
│   │   └── style.css            # Global styles
│   ├── js/
│   │   └── main.js              # Shared JavaScript
│   └── img/                      # Images & assets
├── .htaccess                     # URL rewriting & security
└── README.md                     # This file
```

## 🚀 Features

### Authentication
- User registration with email
- Secure login/logout
- Password management
- Profile customization

### Service Management
- View active services
- Manage service settings
- Renew subscriptions
- Track service status

### Billing & Payments
- View billing history
- Multiple payment methods (Credit Card, PayPal, Bank Transfer)
- Add/remove payment methods
- Download invoices
- Payment processing

### User Experience
- Responsive design (mobile, tablet, desktop)
- Smooth navigation
- Form validation
- Real-time updates via localStorage
- Professional UI/UX

## 💻 Tech Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Styling**: Tailwind CSS (CDN)
- **Icons**: Ionicons 5.5.2
- **Fonts**: Inter (Google Fonts)
- **Data Storage**: Browser localStorage
- **Icons**: Heroicons/SVG

## 🔧 Installation & Setup

### Prerequisites
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Web server (Apache with mod_rewrite enabled)
- No database or backend required for demo

### Local Development
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd floor-hosting
   ```

2. Serve files using any HTTP server:
   ```bash
   # Using Python 3
   python -m http.server 8000
   
   # Using Node.js
   npx http-server
   
   # Using PHP
   php -S localhost:8000
   ```

3. Open in browser:
   ```
   http://localhost:8000
   ```

### Production Deployment
1. Upload all files to your web server
2. Ensure `.htaccess` is present in root (enables URL rewriting)
3. Configure your domain DNS
4. Enable HTTPS/SSL certificate
5. Review security settings in `.htaccess`

## 📝 Usage Guide

### For Users
1. **Register**: Click "Get Started" → Fill registration form
2. **Login**: Enter credentials from registration
3. **View Dashboard**: See services and quick stats
4. **Manage Services**: Update settings, renew services
5. **Billing**: Add payment methods, view invoices
6. **Checkout**: Complete payment for renewals

### For Developers

#### Adding a New Page
1. Create HTML file in appropriate `/pages/` subdirectory
2. Link shared CSS and JS:
   ```html
   <link rel="stylesheet" href="../../assets/css/style.css">
   <script src="../../assets/js/main.js"></script>
   ```
3. Update navigation links in `index.html`
4. Test all internal links

#### Using Shared Functions
```javascript
// Get current user
const user = getCurrentUser();

// Save to localStorage
saveToLocalStorage('key', value);

// Validate form
validateForm('formId');

// Show alert
showAlert('Message', 'success'); // type: success, warning, danger, info

// Format currency
const price = formatCurrency(99.99); // "$99.99"

// Format date
const date = formatDate('2025-11-15'); // "Nov 15, 2025"
```

#### Customizing Styles
Global styles are in `assets/css/style.css`. Update CSS variables:
```css
:root {
    --primary-blue: #2563EB;
    --danger: #EF4444;
    --success: #10B981;
}
```

## 🔐 Security Features

- `.htaccess` protects sensitive files
- Input validation on forms
- localStorage XSS protection
- No hardcoded credentials
- HTTPS recommended for production

## 📊 Data Structure

### User Data (localStorage)
```javascript
{
    userFirstName: 'John',
    userLastName: 'Doe',
    userEmail: 'john@example.com',
    userPassword: '****',
    userCompany: 'ACME Corp'
}
```

### Payment Methods
```javascript
{
    paymentMethods: [
        {
            id: 'PM-1234',
            type: 'credit_card',
            cardNumber: '****4242',
            expiryDate: '12/25',
            name: 'John Doe',
            isPrimary: true
        }
    ]
}
```

### Invoices
```javascript
{
    invoices: [
        {
            id: 'INV-001',
            date: '2025-11-15',
            amount: 99.99,
            status: 'paid',
            service: 'Pro Hosting'
        }
    ]
}
```

## 🎨 Customization

### Change Colors
Edit `style.css` CSS variables or use Tailwind classes in HTML

### Change Fonts
Update Google Fonts link in HTML files

### Add Your Logo
Replace brand name with logo image in header

### Modify Layout
Adjust Tailwind classes in HTML (grid, flex, padding, etc.)

## 🐛 Known Limitations

- Uses localStorage (cleared if browser cache is cleared)
- No actual payment processing (demo only)
- No backend database
- Single-user per browser only
- No email notifications

## 🔄 Future Enhancements

- [ ] Backend API integration (Node.js/PHP)
- [ ] Real database (MySQL/PostgreSQL)
- [ ] Payment gateway integration (Stripe, PayPal)
- [ ] Email notifications
- [ ] Admin dashboard
- [ ] Analytics & reports
- [ ] 2FA authentication
- [ ] API documentation
- [ ] Mobile app (React Native)
- [ ] Multi-language support

## 📞 Support

For issues or questions:
- Email: support@floorhosting.com
- Website: https://floorhosting.com
- Documentation: See FAQ page

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

## 👨‍💻 Author

Built by [Your Name/Company]

---

**Last Updated**: November 15, 2025  
**Version**: 1.0.0  
**Status**: Production Ready (Frontend Only)