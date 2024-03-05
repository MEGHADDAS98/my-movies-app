# my-movies-app
This is a Django ORM project that creates a web application for managing movies and collections created by users.
My Movies Management System

Overview

This "MyMoviesApp" Project is to manage movie-related operations, encompassing movie listings, user authentication, and API interactions. It offers a range of functionalities through APIs to handle movie data, user accounts, and movie collections effectively.

Features
User Authentication: Users can register, log in, and authenticate using JWT tokens.
Movie Listing: API for retrieving a paginated list of movies from external sources.
Collection Management: CRUD operations for creating and managing user collections of movies.
Favorite Genres: Logic to determine and display the top 3 favorite genres based on user collections.
Movie Details: API endpoints to access detailed information about individual movies.
Collection Movie Association: Functionality to update and delete movies within a specific collection.
Technologies Used
Django: Powerful Python web framework for developing web applications.
Django REST Framework: Toolkit for building robust Web APIs using Django.
Installation
Clone the repository:
bash
git clone https://github.com/MEGHADDAS98/my-movies-app.git

Install dependencies:

pip install -r requirements.txt

Apply database migrations:

python manage.py migrate

Run the development server:

python manage.py runserver

Usage
Access the API endpoints using tools like Postman or cURL.
Register users, authenticate using tokens, and utilize the endpoints for managing movie data and collections efficiently.
Explore functionalities such as retrieving movie listings, creating collections, updating collection movies, and fetching favorite genres based on user preferences.
This README provides an overview of Your Movie Management System, highlighting its features, technologies utilized, installation steps, and guidance on how to effectively utilize the system for managing movie-related operations.
