# Argument Capital Project 🚀

[![Project Status](https://img.shields.io/badge/status-active-success)](https://github.com/)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

A polished desktop application framework for financial decision support, built with modern Python UI tooling and designed to help users interact with capital management workflows.

---

## 🌟 Project Overview

Argument Capital Project is a lightweight application that provides a clean, intuitive interface for financial workflows, user authentication, administrative controls, and dashboard reporting. It brings together a Python GUI, data persistence, and modular components so teams can prototype capital management tools quickly.

This project solves the common problem of building production-ready desktop financial tools from scratch by delivering:
- a consistent UI architecture,
- reusable components for login/admin/dashboard flows,
- and a dependency-managed Python environment for rapid local setup.

---

## ✨ Key Features

- **User Authentication**: Secure login and role-based access via the admin panel.
- **Admin Dashboard**: Manage users, view data summaries, and control application behavior.
- **Responsive GUI**: Built with `customtkinter` for a modern look-and-feel on Windows.
- **Data Persistence**: Local storage and JSON-backed models for easy prototyping.
- **Modular Design**: Separate UI, logic, and storage layers for easier maintenance.
- **Cross-Platform Ready**: Windows-friendly UI code with structure suitable for future macOS/Linux support.

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
├── `test_models.py`           # Unit tests for data model functionality
├── `test_storage.py`          # Unit tests for storage and persistence behavior
├── `ui_windows/`              # Windows-specific UI modules and tests
│   ├── `ui_admin_login.py`     # Admin login screen implementation
│   ├── `ui_admin_panel.py`     # Admin dashboard panel implementation
│   ├── `ui_admin_user_table.py`# User management interface
│   ├── `ui_dashboard.py`       # Main dashboard UI
│   ├── `ui_login.py`           # General login screen implementation
│   ├── `test_adm_dashboard.py` # Tests for admin dashboard views
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

## 📌 Suggested Additional Sections

1. **Architecture** — explain the UI, data, and storage layers.
2. **Configuration** — document environment variables and runtime options.
3. **Development Workflow** — describe how to contribute, branch, and run tests.
4. **Screenshots** — show the application UI and workflow visually.
5. **Roadmap** — list planned features and future improvements.
