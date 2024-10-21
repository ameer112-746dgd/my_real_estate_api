
### 2. `API_DOCUMENTATION.md`

```markdown
# API Documentation

## Overview
This document outlines the API endpoints available in the Real Estate API, including user authentication, property management, listing user management, and blog management.

## API Endpoints

### User Authentication
- **Register User**: `POST /api/register/`
- **Login User**: `POST /api/login/`
- **Logout User**: `POST /api/logout/`

### Property Management
- **Add Property**: `POST /api/properties/`
- **Get All Properties**: `GET /api/properties/`
- **Get Property by ID**: `GET /api/properties/<property_id>/`
- **Update Property**: `PUT /api/properties/<property_id>/`
- **Delete Property**: `DELETE /api/properties/<property_id>/`

### Listing User Management
- **Add Listing User**: `POST /api/listingusers/`
- **Get All Listing Users**: `GET /api/listingusers/`
- **Get Listing User by ID**: `GET /api/listingusers/<listing_user_id>/`
- **Update Listing User**: `PUT /api/listingusers/<listing_user_id>/`
- **Delete Listing User**: `DELETE /api/listingusers/<listing_user_id>/`

### Blog Management
- **Add Blog**: `POST /api/blogs/`
- **Get All Blogs**: `GET /api/blogs/`
- **Get Blog by ID**: `GET /api/blogs/<blog_id>/`
- **Update Blog**: `PUT /api/blogs/<blog_id>/`
- **Delete Blog**: `DELETE /api/blogs/<blog_id>/`

## Usage
- Ensure to include authentication tokens for secured endpoints.
- Use appropriate HTTP methods for each endpoint as described.
