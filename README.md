# Real Estate API

## Project Overview
This API is designed for managing real estate properties, including buying, selling, and renting properties. It includes user authentication, property management, listing user management, and blog management.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
  - [User Authentication](#user-authentication)
  - [Property Management](#property-management)
  - [Listing User Management](#listing-user-management)
  - [Blog Management](#blog-management)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites
- Python 3.x
- Django
- Django REST Framework
- db.sqlite (or other database)

### Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo

2. Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:

pip install -r requirements.txt

4. Set up the database:

Update settings.py with your database configuration.
Run migrations: python manage.py migrate

5. Create a superuser: python manage.py createsuperuser

6. Run the server: python manage.py runserver

# Usage
Use Postman or any API client to test the endpoints.
Ensure to include the appropriate authentication tokens for secured endpoints.

# API Endpoints
# User Authentication
Register User: POST /api/register/
Login User: POST /api/login/
Logout User: POST /api/logout/

# Property Management
Add Property: POST /api/properties/
Get All Properties: GET /api/properties/
Get Property by ID: GET /api/properties/<property_id>/
Update Property: PUT /api/properties/<property_id>/
Delete Property: DELETE /api/properties/<property_id>/

# Listing User Management
Add Listing User: POST /api/listingusers/
Get All Listing Users: GET /api/listingusers/
Get Listing User by ID: GET /api/listingusers/<listing_user_id>/
Update Listing User: PUT /api/listingusers/<listing_user_id>/
Delete Listing User: DELETE /api/listingusers/<listing_user_id>/

# Blog Management
Add Blog: POST /api/blogs/
Get All Blogs: GET /api/blogs/
Get Blog by ID: GET /api/blogs/<blog_id>/
Update Blog: PUT /api/blogs/<blog_id>/
Delete Blog: DELETE /api/blogs/<blog_id>/

