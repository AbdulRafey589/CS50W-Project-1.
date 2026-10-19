# Wiki — CS50 Web Programming

A Wikipedia-inspired online encyclopedia built with Django as part of [Harvard's CS50 Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/).

The application allows users to browse encyclopedia entries, search for topics, create new pages, edit existing content, and navigate to a random entry.

## Features

- **Browse Entries:** View encyclopedia pages containing information on different topics.
- **Search:** Search for encyclopedia entries by title.
- **Create New Pages:** Add new encyclopedia entries through a form.
- **Edit Pages:** Update the content of existing entries.
- **Markdown Support:** Write entry content in Markdown and render it as HTML.
- **Random Page:** Navigate to a randomly selected encyclopedia entry.

## Technologies Used

- **Python** — Application logic
- **Django** — Web framework and request handling
- **HTML** — Page structure
- **CSS** — Styling
- **Markdown2** — Convert Markdown content into HTML

## Getting Started

### Prerequisites

- Python 3
- pip

### Installation

1. Clone the repository:

   ```bash
   git clone <YOUR-REPOSITORY-URL>
   ```

2. Navigate to the project directory:

   ```bash
   cd <YOUR-REPOSITORY-DIRECTORY>
   ```

3. Install the required dependencies:

   ```bash
   pip install django markdown2
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

5. Open the local development URL shown in your terminal, usually `http://127.0.0.1:8000/`.

## Project Structure

- `encyclopedia/` — Main Django application containing views, URL routing, and supporting logic.
- `entries/` — Directory containing the encyclopedia's Markdown entry files, if present in your project structure.
- `templates/` — HTML templates used to render the application.
- `manage.py` — Django command-line utility.

*Note: Adjust the project structure section to match your actual repository.*

## What I Learned

Through this project, I practised building a web application with Django, working with URL routing and views, rendering templates, handling GET and POST requests, processing forms, and converting Markdown content into HTML.

The project also helped me develop my debugging skills and understand how different parts of a web application work together.

## Acknowledgements

This project was developed as part of [CS50's Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/) by Harvard University.

The project specifications and course materials are available through the official course website.
