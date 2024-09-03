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
11. [Deployment](#deployment)
    - [Docker and Docker-Compose](#docker-and-docker-compose)
    - [Nginx Configuration](#nginx-configuration)
12. [Frontend Overview](#frontend-overview)
13. [Decision Making](#decision-making)
14. [Contributing](#contributing)
15. [License](#license)
16. [Acknowledgements](#acknowledgements)


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
        DATABASE_URL=postgres://username:password@localhost:5432/healthy_menu_db
        JWT_SECRET_KEY=your_jwt_secret_key

3. **Install Backend Dependencies**

    Navigate to the backend directory and install the Python dependencies
   
        pip install -r requirements.txt
   
4. **Install Frontend Dependencies**

    Navigate to the frontend directory and install the Node.js dependencies:

        cd frontend
        npm install
        Running the Project

5. **Run the Project Using Docker Compose**

    From the root directory, use Docker Compose to build and run the entire project:

        docker-compose up --build

    This will start up the PostgreSQL database, Django backend, and React frontend in separate containers.

6. **Access the Application**

    Once all containers are running, you can access the application at http://localhost in your browser.

### Running Tests

  To run the tests for backend:
  
        docker-compose exec backend python manage.py test accounts.tests

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
    
