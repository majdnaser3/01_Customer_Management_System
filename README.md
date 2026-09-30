# Customer Management System

A desktop customer management application built with **Python, Flet, and SQLite**.

The application provides a simple interface for managing customer records, including creating, viewing, searching, editing, and deleting customers.

## Features

* Add new customers
* View customer records
* Search customers by:

  * Name
  * Email
  * Phone
  * Company
* Edit existing customers
* Delete customers with confirmation
* Input validation
* SQLite database persistence
* Responsive layout suitable for smaller screens
* Git/GitHub version control

## Technologies

* **Python**
* **Flet**
* **SQLite**
* **Git**
* **GitHub**

## Project Structure

```text
01-Customer-Management-System/
│
├── assets/
│   └── icon.png
│
├── data/
│   └── .gitkeep
│
├── src/
│   ├── main.py
│   └── Customers_database.py
│
├── .gitignore
├── pyproject.toml
└── README.md
```

## Database

The application uses SQLite for local data storage.

The database contains a `Customers` table with:

* `id`
* `name`
* `email`
* `phone`
* `company`
* `created_at`

The database file is intentionally excluded from Git because it contains runtime application data.

## Architecture

```text
Flet UI
   ↓
main.py
   ↓
Customers_database.py
   ↓
SQLite
```

The user interface is separated from the database operations so that the application can be extended more easily in the future.

## Validation

The application validates customer input before saving:

* Name is required
* Email is required and checked for a basic valid format
* Phone number is required and accepts digits and `+`
* Company is required

## Running the Project

Install the project dependencies and run the application with:

```bash
flet run
```

## Windows Build

The application can be packaged as a Windows application using:

```bash
flet build windows -v
```
## Android Build

The application can be packaged as an APK application using:

```bash
flet build apk -v
```

The generated build files are excluded from Git.

## Future Improvements

Possible future improvements include:

* Improved mobile-specific UI
* Additional customer fields
* More advanced filtering and sorting
* Data export/import
* Authentication
* Cloud database support
* AI-powered customer management features

## Author

**Majd Naser**

This project is part of my long-term journey toward becoming an **AI Solutions Developer**, with a focus on building practical software and AI-powered business solutions.
