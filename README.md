# Book Exchange Platform

## Overview

The Book Exchange Platform is a web-based application designed to facilitate the exchange of books among users. It provides a user-friendly interface for book enthusiasts to register, manage their profiles, request books, create wishlists, share ratings and reviews, and search for books based on their preferences. The platform is built using HTML, CSS, Bootstrap for the frontend, and Python with Django for the backend. MySQL is used for database management.

## Features

1. **User Registration and Login:**
   - Users can create accounts by registering with the platform.
   - Existing users can log in securely.

2. **User Profile:**
   - Users can manage their profiles, including updating personal information and changing passwords.

3. **Book Requests:**
   - Users can request books from other users.
   - The platform facilitates communication between users for coordinating book exchanges.

4. **Wishlist:**
   - Users can create and manage their wishlists by adding books they are interested in.

5. **Rating and Reviews:**
   - Users can share their opinions by providing ratings and reviews for the books they have read.

6. **Search and Filter:**
   - Users can search for books based on titles, authors, genres, or other criteria.
   - Filter options help users narrow down their search results.

7. **Penalty System:**
   - The platform enforces a penalty system for late returning of specific books, ensuring fair and responsible book exchanges.

## Technologies Used

- **Frontend:**
  - HTML
  - CSS
  - Bootstrap

- **Backend:**
  - Python
  - Django

- **Database:**
  - MySQL

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Golam-Tawhid/ReadVenture.git

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Database Setup:**

  Create a MySQL database and update the database configurations in settings.py.

4. **Apply Migrations:**

   ```bash
   python manage.py migrate

5. **Run the Development Server:**
   ```bash
   python manage.py runserver

6. **Access the Platform:**
   Open your web browser and go to http://localhost:8000


# License
This project is licensed under the MIT License.
