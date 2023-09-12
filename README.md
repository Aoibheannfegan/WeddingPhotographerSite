# Wedding Photographer Website

## Overview

This application is a comprehensive platform designed for a wedding photographer. It allows potential clients to view the photographer's portfolio, check available dates, and book appointments. The application also provides a CRM system where the photographer can manage client details and appointments. It's developed using Django, HTML, CSS, Python, and JavaScript.

## Distinctiveness and Complexity

The Wedding Photographer Website stands out with its multi-faceted approach, combining both a portfolio showcase for clients and a CRM system tailored specifically for the photographer. The inclusion of a dynamic calendar system, the ability to handle client bookings while cross-referencing available dates, as well as the CRM-style interface to manage and annotate client details, are evidences of the project's complexity and distinctiveness.

## Files and Their Content

### Project Structure

- `main_directory/`: Contains the main Django project settings and configuration.
  - `app_name/`: Contains the application logic.
    - `models.py`: Define database models, including User, Client, Calendar, Note, and Package.
    - `views.py`: 
        - Handles rendering of homepage, gallery, packages, appointment, clients, client-specific pages, and calendar.
        - Provides functionality to add/edit packages.
        - Manages appointment requests.
        - Provides logic for approving client requests and adding notes.
        - Retrieves unavailable dates and event details for the dynamic calendar system.
    - `urls.py`: 
        - Defines routes for the application.
        - Maps URLs to corresponding view functions.
        - Provides API endpoints for retrieving unavailable dates, event details, and package details.
    - `admin.py`: 
        - Registers models (User, Client, Calendar, Note, Package) with the Django admin interface.
    - `static/`: Contains static files for the app.
      - `styles.css`: Contains styling for the web app.
      - `images/`: Folder containing all the images used in the site.
      - `javascript/`: Contains the JS logic for various functionalities.
        - `calendar.js`: Handles displaying unavailable dates, and provides add/view event functionality.
        - `crm.js`: Handles the toggling between the event and notes views, and the client approval functionality.
        - `packages.js`: Allows for editing of package details directly from the front end using text areas.
  - `templates/`: Contains the HTML templates.
    - `appointment.html`: 
        - Contains form fields for booking requests.
        - Provides JavaScript functionality to handle unavailable dates in the date picker.
    - `calendar.html`:
        - Provides a visual calendar and forms to add/view events.
    - `client.html`:
        - Displays individual client profiles, contact information, and event details.
        - Provides an interface to add notes and approve client requests.
    - `clients.html`:
        - Lists all clients in a table format, sortable by various fields like name, email, and requested date.
    - `index.html`:
        - Displays a welcome banner with the brand logo.
        - Introduces the photographer with a bio and image.
        - Showcases a gallery section with curated images.
        - Highlights the various photography packages offered.
        - Features client reviews.
        - Provides a final call-to-action for booking.
    - `layout.html`:
        - Contains the main structure for the website.
        - Defines the site's navbar with links to the homepage, gallery, packages, and booking.
        - Loads the primary CSS and JS resources.
        - Uses block tags to allow other templates to insert content.
    - `packages.html`:
        - Lists out the available packages, each with its title, description, price, and details.
        - For authenticated users, offers an edit button for each package.


### Navigating the Application
1. **Homepage** ([View](/)): An introductory page that showcases the photographer's work and ethos.
2. **Gallery Page** ([View](/gallery)): A visual collection of the photographer's work.
3. **Packages Page** ([View](/packages)): A breakdown of available packages offered by the wedding photographer.
4. **Booking Page** ([View](/appointment)): A form where clients can request bookings. It dynamically checks available dates from the calendar.
5. **Clients Page (Admin only)** ([View](/clients)): Acts as a CRM, listing all clients. Details of each client, including their requests, can be accessed and managed here.
6. **Calendar Page (Admin only)** ([View](/calendar)): Displays all appointments and requests. Allows for the addition of new events, and any dates with events can't be booked by clients.


## Running the Application
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required packages:
   ```bash
   pip3 install markdown
   pip3 install django-widget-tweaks
4. Run the Django development server:
   ```bash
   python manage.py runserver
5. Visit localhost:8000 in your browser to access the application.

## Additional Information

- **Clients CRM**: Any individual who submits a contact form gets registered as a client. This client-centric model allows for detailed tracking and management of client requests.
  
- **Dynamic Calendar System**: The calendar system, accessible only by the admin, provides an overview of booked and available dates. The system syncs with the contact page, ensuring clients can only select available dates. This integration prevents double bookings and keeps the admin updated with their schedule.
