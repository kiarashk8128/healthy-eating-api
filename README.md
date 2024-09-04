# Healthy Menu

## Table of Contents
1. [Overview](#overview)
2. [Project Architecture](#project-architecture)
3. [Technologies Used](#technologies-used)
4. [Features](#features)
5. [Installation](#installation)
   - [Prerequisites](#prerequisites)
   - [Setup](#setup)
   - [Running the Project](#running-the-project)
6. [Project Structure](#project-structure)
7. [Models and Database](#models-and-database)
8. [Logic and Algorithms](#logic-and-algorithms)
   - [Loading Food Data](#loading-food-data)
   - [Generating Menus](#generating-menus)
9. [Security Measures](#security-measures)
10. [Testing](#testing)
    - [Automated Tests](#automated-tests)
    - [Manual Tests](#manual-tests)
11. [Docker-Compose and Nginx Configuration](#docker-compose-and-nginx-configuration)
    - [Docker and Docker-Compose](#docker-and-docker-compose)
    - [Nginx Configuration](#nginx-configuration)
12. [Frontend Overview](#frontend-overview)
13. [Decision Making](#decision-making)

## Overview
Healthy Menu is a comprehensive application designed to help users create weekly meal plans based on their nutritional needs. The application allows users to input their personal data or family members' data, and automatically generates a healthy, balanced menu tailored to their dietary requirements. The menus are generated using a combination of food group data, serving size recommendations, and dietary guidelines.

The application is built with a robust backend for handling data processing and a user-friendly frontend for easy interaction. It supports multiple users and provides personalized menus based on individual profiles, including age, gender, and specific dietary needs.

## Project Architecture
The Healthy Menu project follows a modular architecture, dividing the application into distinct layers that handle specific responsibilities. The main layers are:

1. **Backend (Django)**: Handles all business logic, data processing, and interaction with the database. It’s responsible for generating menus, managing user profiles, and enforcing dietary guidelines.

2. **Frontend (React.js)**: Provides an interactive user interface for users to manage their profiles, generate menus, and view their weekly plans. It communicates with the backend via API calls.

3. **Database (PostgreSQL)**: Stores all persistent data, including user profiles, food items, dietary guidelines, and generated menus.

4. **API Layer**: Facilitates communication between the frontend and backend. This layer handles authentication, data validation, and serves as the gateway to backend services.

5. **Deployment (Docker & Nginx)**: The project is containerized using Docker for easy deployment and scaling. Nginx is used as a reverse proxy to handle incoming requests and serve the application.

## Technologies Used
The Healthy Menu project utilizes the following technologies:

- **Python & Django**: Core backend framework for handling data processing, business logic, and ORM for database interactions.
- **React.js**: Frontend library for building the user interface and managing user interactions.
- **PostgreSQL**: Relational database management system for storing and querying user data, food groups, and menus.
- **Docker**: Containerization tool used for packaging the application and its dependencies for easy deployment.
- **Nginx**: Web server and reverse proxy for handling HTTP requests and serving the frontend application.
- **Axios**: Promise-based HTTP client used in the frontend for making API requests.
- **JWT (JSON Web Tokens)**: Used for securing API endpoints and managing user authentication.

## Features
Healthy Menu provides a range of features designed to promote healthy eating habits:

1. **User and Family Member Profiles**: Users can create profiles for themselves and their family members, each with individual dietary needs.
   
2. **Automated Menu Generation**: Based on user profiles, the system generates a weekly meal plan that meets daily nutritional requirements.

3. **Customizable Food Groups**: The backend supports a comprehensive list of food items categorized into food groups, which can be adjusted or expanded.

4. **Dietary Guidelines Enforcement**: The system includes dietary guidelines such as consuming a variety of vegetables, whole grains, and lean proteins. These are enforced in the generated menus.

5. **Interactive Frontend**: Users can easily navigate the application, generate new menus, and view or adjust their profiles through a clean and responsive interface.

6. **Security and Authentication**: User data is protected through secure authentication mechanisms using JWT, ensuring that only authorized users can access and modify their profiles.

7. **Scalability and Deployment**: The application is containerized with Docker, making it easy to deploy, scale, and manage in various environments.

## Installation

To get started with the Healthy Menu project, follow the steps below to set up the environment and run the application locally.

### Prerequisites

Before setting up the project, ensure you have the following installed on your system:

- **Python 3.8+**: The project is built using Python, so you need an appropriate version installed.
- **Node.js 14+**: Required for running the frontend application.
- **Docker**: Used for containerization of the application components.
- **Docker Compose**: Manages multi-container Docker applications.
- **PostgreSQL**: The application uses PostgreSQL as its database.

### Setup

1. **Clone the Repository**


       git clone https://github.com/yourusername/healthy-menu.git
       cd healthy-menu
2. **Set Up Environment Variables**

    Create a .env file in the root directory and populate it with the necessary environment variables. An example .env file:
  
        DEBUG=True
        SECRET_KEY=your_secret_key
        ALLOWED_HOSTS=hosts
        POSTGRES_NAME=name
        POSTGRES_DB=database
        POSTGRES_USER=user
        POSTGRES_PASSWORD=password
        POSTGRES_HOST=host

3. **Install Backend Dependencies**

    Navigate to the backend directory and install the Python dependencies
   
        pip install -r requirements.txt
   
4. **Install Frontend Dependencies**

    Navigate to the frontend directory and install the Node.js dependencies:

        cd frontend
        npm install
### Running the Project

5. **Run the Project Using Docker Compose**

    From the root directory, use Docker Compose to build and run the entire project:

        docker-compose up --build

    This will start up the PostgreSQL database, Django backend, and React frontend in separate containers.

6. **Access the Application**

    Once all containers are running, you can access the application at http://localhost in your browser.

## Project Structure

   The Healthy Menu project is organized into the following structure:

    healthy-menu/
    │
    ├── backend/                    # Django backend
    │   ├── accounts/               # User accounts app
    │   │   ├── migrations/         # Django migrations for accounts app
    │   │   ├── tests/              # Tests for accounts app
    │   │   │   ├── test_login.py   # Tests related to login functionality
    │   │   │   └── test_signup.py  # Tests related to signup functionality
    │   │   ├── __init__.py         # App initialization
    │   │   ├── admin.py            # Admin configuration
    │   │   ├── apps.py             # App configuration
    │   │   ├── forms.py            # Forms for account management
    │   │   ├── models.py           # Database models
    │   │   ├── serializers.py      # Serializers for converting complex data types
    │   │   ├── tests.py            # General tests
    │   │   ├── urls.py             # URL routing
    │   │   └── views.py            # View logic
    │   │
    │   ├── data/                   # Initial data and CSV files
    │   │   ├── fg_directional_statements-en_ONPP.csv  # Directional statements data
    │   │   ├── foodgroups-en_ONPP.csv                 # Food groups data
    │   │   ├── foods-en_ONPP_rev.csv                  # Foods data
    │   │   ├── servings_per_day-en_ONPP.csv           # Servings per day data
    │   │
    │   ├── health/                 # Project health configurations
    │   │   ├── __init__.py         # Health app initialization
    │   │   ├── asgi.py             # ASGI configuration
    │   │   ├── settings.py         # Project settings
    │   │   ├── urls.py             # URL routing for health checks
    │   │   └── wsgi.py             # WSGI configuration
    │   │
    │   ├── nginx/                  # NGINX configurations
    │   │   └── nginx.conf          # NGINX configuration file
    │   │
    │   ├── nutrition/              # Nutrition and menu-related app
    │   │   ├── management/         # Custom management commands
    │   │   │   └── commands/       # Specific commands to manage nutrition data
    │   │   │       └── load_food_data.py     # Command to load food data
    │   │   ├── migrations/         # Django migrations for nutrition app
    │   │   ├── __init__.py         # App initialization
    │   │   ├── admin.py            # Admin configuration
    │   │   ├── apps.py             # App configuration
    │   │   ├── menu_generation.py  # Menu generation logic
    │   │   ├── models.py           # Database models
    │   │   ├── tests.py            # General tests
    │   │   ├── urls.py             # URL routing
    │   │   └── views.py            # View logic
    │   │
    │   ├── staticfiles/            # Static assets for the project
    │   ├── venv/                   # Virtual environment directory
    │   ├── .env                    # Environment variables file
    │   ├── .gitignore              # Git ignore file
    │   ├── docker-compose.yml      # Docker Compose configuration
    │   ├── Dockerfile              # Dockerfile for backend
    │   ├── manage.py               # Django management script
    │   └── requirements.txt        # Python dependencies
    │
    ├── frontend/                   # React frontend
    │   ├── public/                 # Public assets and index.html
    │   │   └── vite.svg            # Vite logo
    │   ├── src/                    # React components and logic
    │   │   ├── api/                # API calls using axios
    │   │   │   └── axios.js        # Axios setup for API requests
    │   │   ├── assets/             # Static assets like images
    │   │   │   ├── Healthy-eating.jpg # Healthy eating image
    │   │   │   └── react.svg       # React logo
    │   │   ├── pages/              # React pages
    │   │   │   ├── LandingPage.jsx  # Landing page component
    │   │   │   ├── Login.jsx        # Login page component
    │   │   │   ├── MainPage.jsx     # Main page component
    │   │   │   ├── MenuPage.jsx     # Menu page component
    │   │   │   ├── PersonalInfo.jsx # Personal info page component
    │   │   │   └── Signup.jsx       # Signup page component
    │   │   ├── App.css             # Main CSS file for App
    │   │   ├── App.jsx             # Main App component
    │   │   ├── index.css           # Global CSS
    │   │   ├── index.js            # ReactDOM render call
    │   │   ├── main.jsx            # Main entry point for React
    │   │   ├── MainPage.css        # CSS for main page
    │   │   ├── MenuPage.css        # CSS for menu page
    │   │   ├── PersonalInfo.css    # CSS for personal info page
    │   │   └── Signup.css          # CSS for signup page
    │   ├── .gitignore              # Git ignore file
    │   ├── eslint.config.js        # ESLint configuration
    │   ├── index.html              # Main HTML file
    │   ├── package.json            # Node.js dependencies
    │   ├── package-lock.json       # Lock file for Node.js dependencies
    │   ├── README.md               # README for frontend
    │   └── vite.config.js          # Vite configuration
    │
    └── .github/                    # GitHub-specific files
        └── workflows/              # GitHub actions workflows
            └── ci.yml              # Continuous integration configuration
    
## Models and Database

The backend of the Healthy Menu project uses Django's ORM to define the core models that represent the data structure of the application. Below are the primary models and their purposes:

- **CustomUser**:
  - Stores user-specific data, including authentication credentials and profile information.
  - Acts as the main user entity in the application.

- **FamilyMember**:
  - Represents additional family members associated with a user.
  - Stores relevant data like name, age, gender, height, weight, and dietary requirements.

- **FoodGroup**:
  - Defines categories of food items, such as Vegetables, Fruits, Grains, etc.
  - Contains fields like `fgid`, `fgcat_id`, `fgcat`, and `foodgroup`.

- **Food**:
  - Stores individual food items, including their group category, serving sizes, and nutritional information.
  - Linked to `FoodGroup` via a foreign key.

- **ServingPerDay**:
  - Specifies the recommended daily servings for different age groups and genders.
  - Linked to the corresponding food groups.

- **Menu**:
  - Represents a generated menu for a user or family member.
  - Stores the meals for each day of the week, including the food items and serving sizes.

### Database Initialization

The database is initialized with a set of predefined food groups, foods, and serving recommendations. These are loaded into the database during setup using Django’s migration and fixture system.

   **Apply Migrations**: Run migrations to create the necessary tables in the database.
   
         docker-compose exec backend python manage.py makemigrations
         docker-compose exec backend python manage.py migrate


## Logic and Algorithms

### Menu Generation Logic
   The logic for generating a healthy menu is based on a combination of user data, food serving requirements, and directional statements (guidelines). The process follows these steps:

   **User Data**: The user's age, gender, and dietary preferences are taken into account.
   
   **Serving Requirements**: The daily servings required for different food groups are determined based on the user's age and gender.
   
   **Directional Statements**: Guidelines such as "Make half your grains whole grains" or "Choose lower-fat milk products" are applied to ensure a balanced and healthy menu.
   
   **Food Selection**: Food items are randomly selected from the available options within each food group to fulfill the serving requirements.
   
   **Menu Composition**: The menu is composed for each day of the week, ensuring that all guidelines are met.
   
### Loading Food Data
   The food data, including food groups and serving recommendations, is loaded into the database from CSV files. These CSV files contain the initial dataset required for the application.

Steps to Load Food Data:

**Prepare the CSV Files**:

Ensure that the CSV files are formatted correctly and placed in the data directory.

**Run the Data Load Command**:

Use Django's custom management command to load the food data into the database.

      docker-compose exec backend python manage.py load_food_data
      
**Verify the Data**:

After loading the data, verify that the food items, food groups, and serving recommendations have been correctly populated in the database.

### Generating Menus
   The menu generation algorithm creates a weekly meal plan based on the user's dietary needs and preferences. The process includes:

**Determine Serving Requirements**: Based on the user's age, gender, and dietary restrictions, calculate the daily servings required for each food group.

**Apply Directional Statements**: Ensure that the menu adheres to nutritional guidelines, such as including a specific number of servings of whole grains or vegetables.

 **Random Food Selection**:Randomly select food items from the available options to meet the serving requirements.
 
**Generate Daily Menus**: Compose the menu for each day of the week, ensuring a variety of meals and compliance with nutritional guidelines.

**Final Adjustments**: After the initial menu is generated, apply any necessary adjustments, such as ensuring that vegetables are served more frequently than juice or that lean meats are included.

**Store the Menu**: Once the menu is generated, it is stored in the database associated with the user or family member.


By following these steps, the Healthy Menu project generates a balanced, nutritious weekly menu tailored to the specific needs of each user.


## Security Measures

Security is a critical aspect of the Healthy Menu project. The following measures have been implemented to ensure the protection of user data and the integrity of the application:

### Authentication and Authorization
- **JWT (JSON Web Token)**: The application uses JWT for secure user authentication. Tokens are issued upon successful login and must be included in the header of subsequent requests to access protected resources.
- **Role-Based Access Control**: Different levels of access are enforced based on user roles (e.g., regular users vs. admins). Sensitive operations are restricted to authorized users only.

### Data Encryption
- **Password Hashing**: User passwords are securely hashed using Django's built-in `make_password` function before being stored in the database. This ensures that passwords are not stored in plain text.
- **SSL/TLS**: The application is configured to use SSL/TLS for encrypting data in transit, protecting it from interception during transmission over the network.

### Input Validation and Sanitization
- **Form Validation**: All user inputs are validated on the server-side to prevent common attacks such as SQL injection and XSS (Cross-Site Scripting). 
- **CSRF Protection**: Django's CSRF protection is enabled to guard against Cross-Site Request Forgery attacks. This ensures that requests made to the server originate from trusted sources.

### Error Handling and Logging
- **Error Handling**: The application is configured to handle errors gracefully. Sensitive information is not exposed to end-users; instead, generic error messages are displayed.
- **Logging**: Important events, such as failed login attempts and unauthorized access, are logged for monitoring and auditing purposes.

### Secure Data Storage
- **Database Security**: Access to the database is restricted to authorized users only. The database credentials are stored securely using environment variables.
- **Data Retention Policies**: Personal data is retained only for as long as necessary, and users have the option to delete their accounts, which triggers the removal of their data.

---

## Testing

Comprehensive testing is crucial for ensuring the reliability and stability of the Healthy Menu project. Both automated and manual tests are employed to cover various aspects of the application.

### Automated Tests

Automated tests are executed as part of the CI/CD pipeline to catch regressions and ensure that the application behaves as expected after code changes. The following types of automated tests are included:

- **Unit Tests**: These tests focus on individual components and functions within the application, ensuring they produce the correct output given specific inputs.
- **Integration Tests**: These tests verify that different parts of the application work together as intended. For example, integration tests ensure that the backend APIs interact correctly with the database.
- **End-to-End Tests**: These tests simulate user interactions with the application to validate the entire user flow, from logging in to generating a menu.

### Manual Tests

In addition to automated tests, manual testing is performed to catch issues that may not be easily detected by automated tests. Manual testing focuses on:

- **User Interface (UI) Testing**: Ensuring that the frontend is responsive, user-friendly, and free of visual bugs.
- **Usability Testing**: Observing how real users interact with the application to identify any usability issues or areas for improvement.
- **Exploratory Testing**: Manually testing various parts of the application without predefined test cases to discover unexpected behaviors or edge cases.

---

### Automated Tests

Automated tests are implemented using Django's testing framework for the backend and Jest for the frontend. These tests are designed to run automatically as part of the continuous integration (CI) process.

- **Testing Framework**: Django's built-in test framework is used to write and run backend tests.
- **Test Cases**: Tests are organized by modules and cover different aspects of the application, such as user authentication, menu generation, and data validation.
- **Running Tests**: To run the automated tests for the backend, use the following command:

  ```bash
   docker-compose exec backend python manage.py test accounts.tests


## Docker-Compose and Nginx Configuration

### Docker and Docker-Compose

   The Healthy Menu project uses Docker to containerize the application, making it easier to deploy and manage. Docker Compose is used to orchestrate the various containers required by the application.

   The Django application runs in its own container. The Dockerfile in the backend/ directory defines the image, which includes the Python environment and all necessary dependencies.

   A PostgreSQL database container is used to store application data.

### Nginx Configuration
   Nginx is used as a reverse proxy to route traffic between the frontend and backend services and to serve static files efficiently.
   
   **Static Files**: Nginx serves static files directly from the /static/ directory, improving the performance of the application.
   
   **Reverse Proxy**: Requests to the root URL (/) are forwarded to the frontend, while API requests (/api/) are routed to the Django backend.

   **Security:** Nginx is configured to handle SSL/TLS certificates, providing encrypted communication between the client and server.


## Frontend Overview
The frontend of the Healthy Menu project is built using React, a popular JavaScript library for building user interfaces. The frontend interacts with the backend API to fetch data and display it to users in a responsive and user-friendly manner.

### Key Components

**Landing Page**: The main entry point of the application, providing an overview of the features and a call to action for users to log in or sign up.

**Login/Signup Pages**: These pages allow users to authenticate themselves and create new accounts.

**Main Page**: After logging in, users are taken to the main page, where they can view and manage their profile, family members, and dietary preferences.

**Menu Page**: The core feature of the application, where users can generate and view their weekly menu based on the dietary guidelines.

**Personal Info** Page: Allows users to update their personal information, such as height, weight, and age, which influence the generated menu.

## Decision Making

The Healthy Menu project involved several critical decisions to ensure that the application is both functional and maintainable. Below are some of the key decisions made during the development process:

### Technology Stack
- **Django and React**: Django was chosen for its robust and scalable backend capabilities, particularly its ORM for managing complex database interactions. React was selected for the frontend due to its component-based architecture, making it easier to manage the dynamic user interface.

### Database
- **PostgreSQL**: Chosen for its reliability and performance, particularly with complex queries and large datasets. Its support for JSONB fields was also considered for potential future enhancements involving more complex data structures.

### Containerization
- **Docker**: The decision to containerize the application using Docker was made to ensure consistency across development, staging, and production environments. Docker Compose was used to simplify the management of multiple containers.

### Security
- **JWT Authentication**: JSON Web Tokens were chosen for user authentication due to their stateless nature, which is well-suited for distributed systems and microservices. This decision was made to improve scalability and security.
- **Environment Variables**: Sensitive information such as secret keys and database credentials are managed through environment variables to enhance security and simplify configuration.

### Frontend Design
- **Responsive Design**: The decision to implement a fully responsive design ensures that the application is accessible and functional across all device types, including desktops, tablets, and smartphones.

