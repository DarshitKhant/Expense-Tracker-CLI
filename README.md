# 💰 Expense Tracker CLI

A robust, modular Command-Line Interface (CLI) application built with **Python**. This project implements **Object-Oriented Programming (OOP)** and **Data Persistence** to help users track daily spending through a menu-driven interface.

## 🚀 Key Features

* **Entry Logging:** Capture amount, category (Food, Travel, Bills, Other), and personalized notes.
* **Data Persistence:** Automatic saving to `expenses.csv` ensures data is never lost between sessions.
* **Intelligent Reporting:** Generate monthly spending summaries with category-wise breakdowns.
* **Validation Engine:** Robust error handling for invalid data types and negative financial inputs.
* **Modular Architecture:** High separation of concerns across logic, storage, and UI layers.

## 🛠️ Technical Architecture

The project is structured into four distinct modules to ensure scalability and maintainability:

1.  **`main.py`**: The **Controller**. Manages the user interaction loop and coordinates between modules.
2.  **`expense.py`**: The **Data Model**. Defines the `Expense` class blueprint and ensures consistent data structure.
3.  **`fileHandler.py`**: The **Storage Layer**. Handles all CRUD operations (Create/Read) with the CSV file.
4.  **`reports.py`**: The **Logic Layer**. Processes raw data to compute totals and filter spending by date.
# 💰 Expense Tracker CLI

A robust, modular Command-Line Interface (CLI) application built with **Python**. This project implements **Object-Oriented Programming (OOP)** and **Data Persistence** to help users track daily spending through a menu-driven interface.

## 💻 Installation & Usage

### Prerequisites
* Python 3.10 or higher installed.

### Setup
1. Clone the repository
2. Run the application
