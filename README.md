
# RESTAURANT MANAGEMENT SYSTEM DOCUMENTATION

This guide provides comprehensive information about the API, its endpoints, and instructions to set up and test the project locally.

Here are the names of the students in the group assignment, who contributed:
1. WAYNE LUMADEDE- 151295
2. ALVIN NDUATI- 166244
3. JOE NJIOKA-150170
4. NYAKIO NDAMBIRI- 152136
5. FINNRAYAT OCHIENG-165915
6. NTUMWA
 

---

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Environment Setup](#environment-setup)
4. [API Endpoints](#api-endpoints)
   1. Menus
   2. Orders
   3. Reservations
   4. Payment
5. [Contributing](#contributing)

---

## Overview

The **Restaurant Management System** is built using Django and Django REST Framework (DRF). It enables managing of restaurant, the orders that come. 

---

## Installation

Follow these steps to clone and run the project locally:

### Prerequisites
Ensure the following are installed on your system:
- Python 3.8+
- pip (Python package manager)
- Git

### Clone the Repository

```bash
$ git clone https://github.com/NYAKIOMURIUKI-TECH/restaurantmanagementsys.git
$ cd restaurant_system
```

---

## Environment Setup

### 1. Create a Virtual Environment

```bash
$ python -m venv venv
$ source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

### 2. Install Dependencies

```bash
$ pip install -r requirements.txt
```

### 3. Apply Migrations

```bash
$ python manage.py migrate
```


### 4. Run the Server

```bash
$ python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`.

---

## API Endpoints

### Orders
- **Create order**
  - `POST /api/orders/`

- **List Orders**
  - `GET /api/orders/{id}/`
  - `GET /api/orders/{id}/`-order status [from placed to in preparation]

### Menus
- **List Menus**
  - `GET /api/menu/`
    

- **/Update the menu**
  - `GET /api/menu/{id}/`
  - `PUT /api/menu/{id}/`



## Contributing

We welcome contributions to enhance the functionality of the API. Please follow these steps:
1. Fork the repository.
2. Create a feature branch.
3. Commit your changes and open a pull request.

---

