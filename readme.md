# Departmental Announcement System

## Table of Contents
- [Project Overview](#project-overview)
- [System Requirements](#system-requirements)
- [Design](#design)
  - [Database Design](#database-design)
  - [Frontend](#frontend)
  - [Backend](#backend)
- [Implementation](#implementation)
- [Additional Features](#additional-features)
- [Technologies](#technologies)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)

## Project Overview
The Departmental Announcement System is designed to streamline communication within a department by allowing authorised users to post announcements in various categories. The system supports notification alerts for users when new announcements are posted and provides functionality for setting expiration dates on announcements. Additional features include the potential for mobile app integration, email notifications, and user engagement tools such as commenting and liking announcements.

## System Requirements
1. **User Authentication**: Only authorised users can post announcements.
2. **Announcement Categories**: Announcements are categorised (e.g., Events, News, Reminders).
3. **Posting Announcements**: Announcements may contain text, images, and attachments.
4. **Notification System**: Users receive notifications when new announcements are posted.
5. **Announcement Expiration**: Announcements expire after a specified date.

## Design

### Database Design
- **User Table**
  - `username`: User's login name
  - `password`: Hashed password
  - `role`: User role (e.g., Admin, Member)

- **Announcement Table**
  - `title`: Title of the announcement
  - `content`: Main content or message
  - `category`: Category of the announcement (e.g., Event, Reminder)
  - `expiration_date`: Date when the announcement expires
  - `posted_by`: The user who posted the announcement

- **Notification Table**
  - `announcement_id`: Reference to the announcement
  - `user_id`: The user to be notified
  - `read_status`: Indicator of whether the user has read the announcement

### Frontend
- **Login Page**: User login interface for authentication.
- **Announcement Posting Form**: Form for creating and submitting announcements (with text, images, attachments).
- **Announcement List Page**: Displays categorised announcements with search functionality.
- **Announcement Detail Page**: Displays detailed view of announcement.
- **Notification List Page**: List of unread notifications and read status.

### Backend
- **User Authentication API**: Handles login and user authorisation.
- **Announcement Posting API**: Manages announcement creation, editing, and deletion.
- **Notification API**: Notifies users of new announcements and tracks read status.


## Additional Features
1. **Email Notifications**: Send email alerts for new announcements.
2. **Mobile App Integration**: Expand the system to support mobile platforms.
3. **Commenting and Liking**: Allow users to comment on and like announcements.
4. **User Roles and Permissions**: Define different permissions for Admins, Managers, and Regular Users.
5. **Analytics and Reporting**: Implement tools to track user engagement and announcement reach.

## Technologies
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask/Django)
- **Database**: MySQL/PostgreSQL
- **Notification System**: RabbitMQ, Celery (or similar)
- **Authentication**: OAuth/Django Auth
- **Deployment**: Docker, Nginx, Gunicorn, AWS/Azure

## Setup and Installation

1. **Unzip the folder**

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. Create a superuser
    ```bash
    python manage.py createsuperuser
    ```

4. **Run the Server**
   ```bash
   python manage.py runserver
   ```

## Usage
1. **Login**: Authenticate as an authorised user.
2. **Post Announcements**: Fill out the form and upload any necessary files.
3. **View Notifications**: Check the notifications page for unread announcements.
4. **Search Announcements**: Use the category filters or search bar to find specific announcements.
5. **Admin Control**: Control the system from an admin level by going to `127.0.0.1:8000/admin/` while server is running.
--- 
