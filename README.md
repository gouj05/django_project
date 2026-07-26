# Updates24 — Real-Time News Delivery Platform

[![Django](https://img.shields.io/badge/Django-5.0+-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.4-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)](https://tailwindcss.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

**Updates24** is a modern, high-performance web application powered by Django designed to deliver real-time, daily news coverage across diverse domains. Featuring automated content categorization, dynamic trending algorithms, search functionality, and personalized reader feeds, Updates24 ensures users stay informed with minimal noise.

---

## Table of Contents

- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [System Architecture](#system-architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Database Setup & Migrations](#database-setup--migrations)
  - [Running the Server](#running-the-server)
- [Project Directory Structure](#project-directory-structure)
- [Core Models & Schemas](#core-models--schemas)
- [Configuration & Environment Variables](#configuration--environment-variables)
- [Admin Portal Guide](#admin-portal-guide)
- [Future Enhancements](#future-enhancements)
- [License](#license)

---

## Key Features

- 📰 **Fresh Daily Content**: Instant publishing workflow with breaking news alerts and real-time updates.
- 📂 **Categorized News Segregation**: Granular categorization covering Politics, Technology, Business, Sports, Entertainment, World, and Science.
- 🔍 **Full-Text Search & Filtering**: Instant search across headlines, content, tags, and authors with custom date filtering.
- 🔥 **Trending & Top Stories Engine**: Automated view counter and engagement tracking to surface high-priority stories.
- 📱 **Fully Responsive Interface**: Tailored reading experience designed for mobile devices, tablets, and desktops.
- 🔖 **User Bookmarks & Reading History**: Personal dashboard for registered users to save articles for later reading.
- 👤 **Editorial Workflow**: Multi-tier user roles (Authors, Editors, Superusers) for draft review and publishing control.

---

## Tech Stack

| Domain | Technology |
| :--- | :--- |
| **Backend Framework** | Django 5.0+ |
| **Language** | Python 3.10+ |
| **Database** | PostgreSQL (Production) / SQLite (Development) |
| **Frontend UI** | HTML5, Tailwind CSS, JavaScript |
| **Template Engine** | Django Templates |
| **Caching & Queue** | Redis & Celery (optional background worker for automated news fetching) |
| **Media Management** | Pillow / Cloudinary |

---

## System Architecture

```text
                               +-------------------+
                               |     End User      |
                               +---------+---------+
                                         |
                                         v
                               +-------------------+
                               |   URL Dispatcher  |
                               +---------+---------+
                                         |
                                         v
   +-----------------------+   +-------------------+   +-----------------------+
   |  News Feed View       |---|   View Handlers   |---|   Category Filter     |
   +-----------------------+   +---------+---------+   +-----------------------+
                                         |
                                         v
                               +-------------------+
                               |   ORM (Models)    |
                               +---------+---------+
                                         |
            +----------------------------+----------------------------+
            |                                                         |
            v                                                         v
  +-------------------+                                     +-------------------+
  |  News Database    |                                     |    Media Assets   |
  |  (Articles/Tags)  |                                     |  (Images/Banners) |
  +-------------------+                                     +-------------------+
