# ✂️ SIC Salon Management

[![Odoo](https://img.shields.io/badge/Odoo-17.0-blueviolet?logo=odoo)](https://www.odoo.com/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)

SIC Salon Management is an Odoo module that extends the functionality of the existing `salon_management` module. It offers enhanced features for managing salon bookings, orders, and customer interactions, including appointment reminders and improved status tracking.

---

## ✨ Features

- **Enhanced Status Tracking:** Visual, color-coded stages for bookings and orders.
- **Appointment Reminders:** Automated reminders for upcoming appointments.
- **Improved Workflow:** Streamlined operations for salon management.
- **Mail Integration:** Automated emails for booking confirmations and reminders.

---

## 📁 Project Structure

```
sic_salon_management/
│
├── __init__.py
├── __manifest__.py
├── controllers/
│   ├── __init__.py
│   └── salon_management.py
├── data/
│   ├── salon_management_mail_template.xml
│   └── salon_stages_data.xml
├── models/
│   ├── __init__.py
│   ├── salon_booking.py
│   └── salon_order.py
├── security/
│   └── ir.model.access.csv
├── views/
│   ├── salon_booking_views.xml
│   ├── salon_order_views.xml
│   └── salon_management_menus.xml
└── static/
    └── src/
        ├── js/
        │   └── salon_dashboard.js
        └── xml/
            └── salon_dashboard.xml
```

---

## 🛠️ Installation

### Prerequisites

- Odoo 17.0 installed and running
- Python 3.9 or higher

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/manziosee/sic_salon_management.git
   ```
2. **Copy to Odoo Addons Directory**
   - Place the `sic_salon_management` folder in your Odoo `addons` or `custom-addons` directory.


3. **Update App List & Install Module**
   - In Odoo, go to *Apps* → *Update Apps List*.
   - Search for **SIC Salon Management** and click *Install*.

---
## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.



