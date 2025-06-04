# ✂️ SIC Salon Management

[![Odoo](https://img.shields.io/badge/Odoo-17.0-blueviolet?logo=odoo)](https://www.odoo.com/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)

SIC Salon Management is an Odoo module that extends the functionality of the existing `salon_management` module. It offers enhanced features for managing salon bookings, orders, and customer interactions, including improved status tracking.

---

## ✨ Features

- **Enhanced Status Tracking:** Visual, color-coded stages for bookings and orders.
- **Improved Workflow:** Streamlined operations for salon management.

---

## 📁 Project Structure

```
sic_salon_management/
├── init.py
├── manifest.py

├── data/
│ └── salon_stages_data.xml

├── models/
│ ├── init.py
│ ├── salon_stage.py
│ ├── salon_booking.py
│ └── salon_order.py

├── views/
│ ├── salon_booking_views.xml
│ ├── salon_order_views.xml
│ └── salon_stage_views.xml
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



