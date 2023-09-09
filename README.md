# Email Campaign Manager

Email Campaign Manager is a web application built with Django that allows you to manage email subscribers and send email campaigns. It provides the following features:

- Add and manage subscribers with email and first name.
- Create and schedule email campaigns with various content options.
- Send daily campaigns in parallel for optimized sending time.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [URLs](#urls)

## Installation

Follow these steps to run the Email Campaign Manager locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/nandanabhishek/email-campaign-manager.git
   cd email-campaign-manager
   ```

   a. Create a virtual environment and activate it:
   ```bash
   python -m venv myvenv
   myvenv\Scripts\activate
   ```

   b. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   c. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

   d. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

   e. Start the development server:
   ```bash
   python manage.py runserver
   ```

   f. Access the application in your web browser at http://localhost:8000.

## Usage

### Admin Panel

- Access the admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin/) and log in with the superuser credentials.

### Subscriber Management

#### Add Subscribers

To add subscribers, follow these steps:

1. Access the "Add Subscribers" page at [http://localhost:8000/email_campaign/add_subscriber/](http://localhost:8000/email_campaign/add_subscriber/).

2. Fill in the subscriber's information, including their email address and first name.

3. Click the "Save" button to add the subscriber.

#### View Subscriber List

To view the list of subscribers, follow these steps:

1. Access the "Subscriber List" page at [http://localhost:8000/email_campaign/subscriber_list/](http://localhost:8000/email_campaign/subscriber_list/).

2. You'll see a list of all subscribers, including their email addresses and first names.

### Campaign Management

#### Add Campaigns

To create and schedule email campaigns, follow these steps:

1. Access the "Add Campaign" page at [http://localhost:8000/email_campaign/add_campaign/](http://localhost:8000/email_campaign/add_campaign/).

2. Fill in the campaign details, including:
   - Subject: Enter the subject of the email campaign.
   - Preview Text: Add a preview text for your email.
   - Article URL: Provide the URL of the article related to the campaign.
   - HTML Content: Enter the HTML content of your email.
   - Plain Text Content: Optionally, add plain text content for email clients that do not support HTML.
   - Published Date: Set the date when you want the campaign to be sent.

3. Click the "Save" button to create the campaign.

#### View Campaign List

To view the list of campaigns, follow these steps:

1. Access the "Campaign List" page at [http://localhost:8000/email_campaign/campaign_list/](http://localhost:8000/email_campaign/campaign_list/).

2. You'll see a list of all campaigns, including their subjects, preview text, article URLs, and published dates.

## Project Structure

The project is organized with the following structure:

- `email_campaign/` - Django app containing models, views, and templates.
- `templates/` - HTML templates for the app's views.
- `static/` - Static files (CSS, JavaScript, images).
- `manage.py` - Django management script.

## URLs

Here are the main URLs and their descriptions for the Email Campaign Manager:

- **Admin Panel**: Access the admin panel to manage subscribers and campaigns.
   - URL: [http://localhost:8000/admin/](http://localhost:8000/admin/)
   - Use your superuser credentials to log in.

- **Subscriber Management**:
   - **Add Subscribers**: Add new subscribers to your email list.
     - URL: [http://localhost:8000/email_campaign/add_subscriber/](http://localhost:8000/email_campaign/add_subscriber/)
   - **View Subscriber List**: See a list of all subscribers.
     - URL: [http://localhost:8000/email_campaign/subscriber_list/](http://localhost:8000/email_campaign/subscriber_list/)

- **Campaign Management**:
   - **Add Campaigns**: Create and schedule email campaigns.
     - URL: [http://localhost:8000/email_campaign/add_campaign/](http://localhost:8000/email_campaign/add_campaign/)
   - **View Campaign List**: See a list of all created campaigns.
     - URL: [http://localhost:8000/email_campaign/campaign_list/](http://localhost:8000/email_campaign/campaign_list/)
