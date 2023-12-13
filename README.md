# LABI Agency Website

## Overview

Welcome to the LABI Django project! This project is a website for LABI Agency, an advertising and production company specializing in exhibitions, printing, promotions, and branding. The Django web framework is used to build this project.

## Project Goals

The primary goal is to create a more targeted and sales-oriented website with improved relevance for classic search queries. Additionally, the website must be SEO-friendly. The project encompasses four key areas:

1. **LABI PRINT - Printing Services**
   - Comprehensive printing services with a focus on souvenir products.
   - Potential inclusion of a catalog with main product types and images.

2. **LABI EXPO - Exhibitions**
   - Construction of exclusive and standard exhibition stands.
   - Mobile exhibition stands and exhibition equipment.

3. **LABI DESIGN - Design Services**
   - Logos, corporate identity, websites, and print design.

4. **LABI BRANDING - Outdoor and Interior Branding**
   - Emphasis on branding cargo containers and corporate transport.
   - Design of commercial spaces (offices, showrooms, trade islands, storefronts, pavilions, navigation, space decoration).


## Project Structure

### Files:

#### `labi/urls.py`

This file handles URL routing for the Django project. It includes paths for the admin panel and the home application.

#### `labi/settings.py`

The settings file contains various configurations for the Django project, including database settings, middleware configurations, and internationalization settings.

#### HTML Pages:

- `home/templates/home/index.html`: Home page template.
- `home/templates/home/print.html`: Template for LABI PRINT services.
- `home/templates/home/expo.html`: Template for LABI EXPO services.
- `home/templates/home/design.html`: Template for LABI DESIGN services.
- `home/templates/home/branding.html`: Template for LABI BRANDING services.
- `home/templates/home/services.html`: A page template that lists all the services of the LABI agency and also adds information why the client should choose this company.
- `home/templates/home/contact.html`: Template with LABI agency contacts.
- `home/templates/home/order.html`: Template of a page where the client can place an order and add a file with technical specifications to it.
- `home/templates/home/errors/404.html`: Custom page for error 404.

### Views Functions (views.py)

- `index`: Renders the home page with an overview of LABI Agency's services.
- `print_service`: Renders the LABI PRINT services page.
- `expo_service`: Renders the LABI EXPO services page.
- `design_service`: Renders the LABI DESIGN services page.
- `branding_service`: Renders the LABI BRANDING services page.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/labidjangoproject.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure that you have PostgreSQL installed and update the database settings in `labi/settings.py` accordingly.

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Create a superuser for the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create a superuser account.

5. Run the development server:

   ```bash
   python manage.py runserver
   ```

   The website will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

6. Access the admin panel:

   Visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and log in with the superuser credentials created earlier.

### Custom Database Configuration

This project uses PostgreSQL as the database engine. Make sure to have PostgreSQL installed, and update the database settings in `labi/settings.py` with your PostgreSQL credentials.

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "your_database_name",
        "USER": "your_database_user",
        "PASSWORD": "your_database_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

### Running in Production

Ensure to set `DEBUG = False` in `labi/settings.py` for production. Additionally, handle static files and other production-related settings as needed.

## Django Project Details

### Models

The project includes models for the LABI website, such as the `Print`, `Expo`, `Design`, and `Branding` models. These models represent the different service areas of the LABI Agency.

### URL Structure

- `/admin/`: Django admin panel for site management.
- `/`: Home application with views for different service areas.

### Static Files

Static files (CSS, JavaScript, images) are stored in the `static` directory. Ensure to run `python manage.py collectstatic` to gather static files for deployment.

### Media Files

Media files (uploaded by users) are stored in the `media` directory. Ensure that `MEDIA_ROOT` is correctly configured in `labi/settings.py`.

### SEO Optimization

#### `robots.txt`

The `robots.txt` file is located at the project root and provides directives to web crawlers. It controls which pages should not be crawled by search engines.

#### Meta Tags

Meta tags for SEO are added in the HTML templates, providing information to search engines. Meta tags include `title`, `description`, and `keywords`.
