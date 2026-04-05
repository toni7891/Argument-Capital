# Argument Capital Project 🚀

[![Project Status](https://img.shields.io/badge/status-active-success)](https://github.com/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A modern desktop ATM simulation application built with Python, featuring user authentication, transaction management, and administrative controls for banking operations.

---

## 🌟 Project Overview

Argument Capital ATM Machine is a comprehensive desktop application that simulates a full-featured ATM system. It provides users with secure access to banking operations including deposits, withdrawals, balance inquiries, and transaction history, while offering administrators powerful tools to manage users and monitor system activity.

This project addresses the need for a reliable, user-friendly ATM interface that can be easily deployed on desktop environments, combining intuitive GUI design with robust data persistence and modular architecture for maintainable banking software.

---

## ✨ Key Features

- **Secure User Authentication**: PIN-based login with account blocking after failed attempts.
- **ATM Operations**: Deposit, withdrawal, and balance checking with real-time updates.
- **Transaction History**: Detailed logs of all financial transactions with timestamps.
- **Admin Panel**: Comprehensive user management, account oversight, and system controls.
- **Modern GUI**: Sleek interface using `customtkinter` with dark mode support.
- **Data Persistence**: JSON-based storage for accounts, transactions, and system state.
- **Modular Architecture**: Separated UI, business logic, and storage layers for easy extension.
- **Cross-Platform Compatibility**: Designed for Windows with macOS support in development.

---

## 📁 File Structure

```text
ArgumentCapitalProject/
├── `main.py`                  # Main application entry point for Windows
├── `main_mac.py`              # Alternate application entry point for macOS compatibility
├── `models.py`                # Domain models and business logic definitions
├── `storage.py`               # Local storage layer and persistence utilities
├── `data.json`                # Sample or live data store for application state
├── `README.md`                # Project documentation
├── `requirements.txt`         # Python dependencies for the project
├── `ui_windows/`              # Windows-specific UI modules and tests
│   ├── `ui_admin_login.py`     # Admin login screen implementation
│   ├── `ui_admin_panel.py`     # Admin dashboard panel implementation
│   ├── `ui_admin_user_table.py`# User management interface
│   ├── `ui_dashboard.py`       # Main dashboard UI
│   ├── `test_final_ui.py`      # End-to-end UI validation tests
│   └── `test_ui_mac.py`        # macOS UI compatibility tests
└── `__init__.py`              # Package initialization marker
```

---

## ⚙️ Installation & Usage

### Prerequisites

- Python 3.10 or newer
- `pip` package manager

### Install dependencies

```bash
python -m pip install -r requirements.txt
```

This repository depends on several UI and utility libraries, including:
- `customtkinter` for the modern desktop interface,
- `CTkTable` for table and data-grid widgets,
- `darkdetect` for automatic dark/light mode detection,
- `pillow` for image handling,
- `requests` for any HTTP integration,
- and supporting packaging/runtime modules.

### Run the application

For Windows:

```bash
python main.py
```

For macOS or alternate launch flow:

```bash
python main_mac.py
```

### Run tests

```bash
python -m pytest
```

> Tip: Use a virtual environment to keep dependencies isolated:
> `python -m venv .venv && .venv\Scripts\activate && python -m pip install -r requirements.txt`

---

## 👥 The Team

- **Guy Peres**
- **Tony Verin**
- **Harel Valfish**

---

## 🏗️ Architecture

The application follows a clean, layered architecture:

- **UI Layer** (`ui_windows/`): Handles all user interface components using `customtkinter` and `CTkTable` for tables.
- **Business Logic Layer** (`models.py`): Contains the `Client` and `Admin` classes with methods for transactions and account management.
- **Data Layer** (`storage.py`): Manages JSON file operations for persistent data storage.
- **Entry Points** (`main.py`, `main_mac.py`): Platform-specific application launchers.

This separation ensures maintainability and allows for easy testing and future enhancements.

---

## ⚙️ Configuration

The application uses a JSON file (`data.json`) for data storage. No additional configuration files are required, but you can modify the data file directly for initial setup or testing.

For development, ensure Python 3.10+ is used, as the code leverages modern Python features.

---

## 🚀 Development Workflow

1. **Clone the repository**: `git clone <repo-url>`
2. **Set up virtual environment**: `python -m venv .venv && .venv\Scripts\activate`
3. **Install dependencies**: `pip install -r requirements.txt`
4. **Run tests**: `python -m pytest` (ensure pytest is installed)
5. **Make changes**: Edit code in your preferred IDE
6. **Test locally**: Run `python main.py` or `python main_mac.py`
7. **Commit and push**: Follow standard Git workflow

---

## 📸 Screenshots

*Coming soon: Screenshots of the login screen, dashboard, and admin panel will be added here.*

---


## 📄 License

This project is licensed under the MIT License.
