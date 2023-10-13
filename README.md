# Wedding Photographer Website

## Overview

This application is a comprehensive platform designed for a wedding photographer. It allows potential clients to view the photographer's portfolio, check available dates, and book appointments. The application also provides a CRM system where the photographer can manage client details and appointments. It's developed using Django, HTML, CSS, Python, and JavaScript.

## Distinctiveness and Complexity

The Wedding Photographer Website stands out from other projects in CS50's web development course; it's a holistic blend of creativity and functionality. One of the most striking features that sets this project apart is its dual nature. On the one hand, it serves as an portfolio platform, allowing clients to view the photographer's work. On the other, it cleverly integrates a CRM system, a tool typically found in business-oriented software. This CRM system isn't just for the sake of inclusion; it is meticulously tailored to cater to the needs of the photographer, enabling them to manage, record, and annotate intricate client details seamlessly.

Building on the theme of distinctiveness, the dynamic calendar system embedded in the project stands out both in terms of design and utility. The calendar goes beyond date selection. It offers the photographer an intuitive interface to view appointments, block off specific dates, and ensure that their availability is communicated in real-time. Ensuring that blocked dates are not available for further booking on the client's booking form is not a mere aesthetic touch but a demonstration of forward-thinking design and user experience consideration. Additionally, admins have the ability to edit package details directly on the site, another example of UX considerations. 

Furthermore, my pursuit of excellence didn't stop at what was taught in the course. I ventured beyond the curriculum by harnessing the power of additional tools and libraries. One example is the incorporation of django-widget-tweaks – an efficient tool to enhance the rendering of Django form fields. Another notable mention is full calendar, which played a pivotal role in realizing the dynamic calendar feature. By integrating these, I not only enhanced the project's functionality but also its distinctiveness, as it showcases a willingness to explore, learn, and implement external resources to achieve a refined product. Moreover, significant attention was paid to the site's aesthetic appeal. After a study of color theory, a meticulously chosen color palette was added to the CSS, ensuring that the visual experience is not only functional but also emotionally resonant with its audience.

## Files and Their Content

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

## Requirements
- Install the required packages:
   ```bash
   pip3 install markdown
   pip3 install django-widget-tweaks

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
6. The admin page can be accessed using the login and password "CS50staff".

## Additional Information

- **Clients CRM**: Any individual who submits a contact form gets registered as a client. This client-centric model allows for detailed tracking and management of client requests.
  
- **Dynamic Calendar System**: The calendar system, accessible only by the admin, provides an overview of booked and available dates. The system syncs with the contact page, ensuring clients can only select available dates. This integration prevents double bookings and keeps the admin updated with their schedule.
