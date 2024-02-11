# Library Management System

This is a comprehensive library management system built using Django, designed to streamline the management of library resources and activities.


## Features

- **Student CRUD**:  Administrators can manage student records, including adding new students, updating their information, and deleting obsolete records.
- **Category CRUD**:  Create, update, and delete categories to classify books based on their genres or subjects.
- **Subcategory CRUD**: Further classify books within categories by creating, updating, and deleting subcategories.
- **Books CRUD**: Add new books to the library database, update existing book details, and remove books that are no longer available.
- **Book Transaction CRUD**:  Record borrowing and returning activities, manage due dates, and track overdue books.
- **Authentication System**: Secure access to the system with user authentication, allowing administrators, librarians to log in with their credentials.
- **Dashboard of All Activities**: Monitor library activities and key metrics through a customizable dashboard, providing insights into library operations.

## Installation

1. Clone the repository:
  git clone https://github.com/Prasad-Bojja/library_management.git
   
2. Navigate to the project directory:
   cd library_management
   
4. Install the required dependencies:
   pip install -r requirements.txt
   
5. Apply database migrations:
   python manage.py migrate

6. Create a superuser account (optional):
   python manage.py createsuperuser

7. Run the development server:
   python manage.py runserver

## Usage

- Log in with your administrator credentials to access the admin dashboard.

- Manage students, categories, subcategories, books, and book transactions through the respective CRUD interfaces.

- Use the dashboard to monitor system activities and track book transactions.

## Contributing

- Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please feel free to open an issue or submit a pull request.


 

