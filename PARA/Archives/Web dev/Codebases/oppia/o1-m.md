
# Oppia Repository Roadmap

Welcome to the Oppia repository! This roadmap will help you navigate the codebase efficiently, understand its structure, key components, and best practices, enabling you to contribute effectively.

## 1. Main Directory Structure

The Oppia repository is organized into several key directories, each serving a specific purpose:

```markdown:core/README.md
1|This folder contains the scripts for Oppia backend & frontend.
2|
3|- controllers: Backend controllers & tests for them.
4|- domain: Services & classes for various data models used in Oppia codebase.
5|- platform: Google App Engine services.
6|- storage: Definitions for storage models on Google App engine.
7|- templates: All the frontend directive, controllers, filters & services.
8|- tests: E2E tests for various Oppia pages.
```

**Key Directories:**

- **`.github/`**: Contains GitHub-related configurations like issue templates, pull request templates, code owners, and discussion templates.
  
- **`core/`**: The heart of the application, divided into:
  - **`controllers/`**: Handles backend routes and requests.
  - **`domain/`**: Contains services and data models.
  - **`platform/`**: Integrates with Google App Engine services.
  - **`storage/`**: Defines storage models specific to App Engine.
  - **`templates/`**: Frontend components, directives, controllers, and services.
  - **`tests/`**: End-to-end (E2E) tests for various pages.

- **`assets/`**: Stores various assets used in the codebase.
  - **`i18n/`**: Translations for supported languages.
  - **`images/`**: Website images.
  - **`overrides/`**: Overrides for third-party assets.
  - **`pages/`**: Attribution messages.
  - **`scripts/`**: Scripts for exploration embeddings & testing.
  - **`videos/`**: Website videos.

- **`extensions/`**: Frontend & backend code for extensions & plugins.
  - **`actions/`**, **`answer_summarizers/`**, **`ckeditor_plugins/`**, etc.

- **`scripts/`**: Python scripts for linting, building, and other utilities.

- **`data/`**: YAML data for testing and loading explorations & collections.

## 2. Key Files and Their Roles

Understanding key files is crucial for navigation and contribution:

- **Configuration Files:**
  - **`.github/CODEOWNERS`**: Specifies code ownership for different parts of the repository, ensuring appropriate reviewers are assigned for pull requests.
  - **`.github/PULL_REQUEST_TEMPLATE.md`**: Template for creating pull requests, guiding contributors to provide necessary information.
  - **`main.py`**: Entry point for the backend application, importing various controllers and handling request routing.
  - **`core/tests/lighthouse-pages.json`**: Configuration for Lighthouse performance testing on different pages.

- **Documentation Files:**
  - **`README.md`**: Provides an overview of the repository, installation instructions, contribution guidelines, support channels, and license information.
  - **`core/README.md`**, **`assets/README.md`**, **`extensions/README.md`**: Offer detailed explanations about specific directories and their contents.

- **Test Files:**
  - **`core/tests/`**: Contains E2E tests, configurations, and test dependencies.
  - **`core/tests/webdriverio_desktop/`**: WebdriverIO tests for desktop versions, such as `contributorDashboard.js`.

- **Template and Static Files:**
  - **`core/templates/pages/`**: HTML templates for various pages like the exploration player, contributor dashboard, etc.
  - **`assets/scripts/README.md`**: Instructions for testing embedding scripts.

## 3. Overall Architecture and Data Flow

Oppia follows a modular architecture, separating concerns between frontend and backend:

- **Backend (Python with Google App Engine):**
  - **Controllers**: Handle HTTP requests, interact with services in the `domain/` layer, and manage data storage via the `storage/` models.
  - **Domain Services**: Encapsulate business logic and interact with storage models.

- **Frontend (Angular):**
  - **Templates**: Utilize Angular directives, controllers, and services to build interactive user interfaces.
  - **Assets**: Manage static resources like images, translations, and scripts.

**Data Flow:**

1. **Request Handling**: Incoming HTTP requests are routed to appropriate backend controllers.
2. **Business Logic**: Controllers invoke domain services to process data.
3. **Data Storage**: Services interact with storage models to retrieve or persist data.
4. **Frontend Rendering**: Processed data is sent to the frontend, where Angular templates render the user interface.
5. **User Interaction**: Users interact with the frontend components, which may trigger new requests, continuing the cycle.

## 4. Typical Workflows or Functions

Understanding the workflow helps in identifying where to implement or modify features:

- **Entry Point:**
  - **`main.py`** initializes the application, importing various controllers that define routes and request handlers.

```python:main.py
from core.controllers import classroom
from core.controllers import collection_editor
from core.controllers import collection_viewer
from core.controllers import concept_card_viewer
from core.controllers import contributor_dashboard
from core.controllers import contributor_dashboard_admin
from core.controllers import creator_dashboard
from core.controllers import cron
from core.controllers import custom_landing_pages
from core.controllers import diagnostic_test_player
from core.controllers import editor
from core.controllers import email_dashboard
from core.controllers import feature_flag
from core.controllers import features
from core.controllers import feedback
from core.controllers import feedback_updates
from core.controllers import firebase
from core.controllers import improvements
from core.controllers import incoming_app_feedback_report
from core.controllers import learner_dashboard
from core.controllers import learner_goals
from core.controllers import learner_group
from core.controllers import learner_playlist
from core.controllers import library
from core.controllers import moderator
from core.controllers import oppia_root
from core.controllers import pages
from core.controllers import practice_sessions
```

- **Core Logic Location:**
  - **Backend Services**: Reside in `core/domain/`.
  - **Frontend Components**: Located in `core/templates/`.

- **Testing:**
  - **E2E Tests**: Implemented using WebdriverIO in `core/tests/webdriverio_desktop/`.
  - **Unit Tests**: Present alongside services and components.

## 5. Conventions and Best Practices

Maintaining consistency is vital for collaborative development. Oppia follows several conventions:

- **Naming Conventions:**
  - **Directories**: Use lowercase with dashes (e.g., `components/auth-wizard`).
  - **Files**: Descriptive and consistent naming, e.g., `skill-editor-page.module.ts`.

- **Code Style:**
  - **TypeScript**: Functional and declarative patterns are favored over classes.
  - **Python**: Adheres to PEP 8 standards for readability and consistency.

- **File Structure:**
  - **Modularization**: Avoids code duplication by iterating and modularizing functionalities.
  - **Separation of Concerns**: Clear division between frontend templates and backend services.

- **Error Handling:**
  - **Backend**: Implements custom error types and guard clauses for early error detection.
  - **Frontend**: Uses robust error handling in services and components.

- **Documentation:**
  - **README Files**: Each directory contains a `README.md` explaining its purpose.
  - **JSDoc/Python Docstrings**: Functions and components are documented for better IDE support.

- **Testing:**
  - **Comprehensive Tests**: Includes unit and E2E tests to cover various functionalities.
  - **Continuous Integration**: Automated testing pipelines ensure code quality.

- **Security and Performance:**
  - **Input Validation**: Ensures all user inputs are validated to prevent security vulnerabilities.
  - **Optimization**: Implements dynamic imports, responsive design, and image optimizations for performance.

- **Contribution Guidelines:**
  - **Code Owners**: Defined in `.github/CODEOWNERS` to streamline the review process.
  - **Pull Request Templates**: Guides contributors to provide necessary information for reviews.

```markdown:.github/CONTRIBUTING.md
...
6|
7|- [Coders](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia)
8|- [Instructional designers and storytellers](https://github.com/oppia/oppia/wiki/Teaching-with-Oppia)
9|- [UX researchers](https://github.com/oppia/oppia/wiki/Conducting-research-with-students)
10|- [Voice artists](https://github.com/oppia/oppia/wiki/Instructions-for-voice-artists)
11|- [Designers and artists](https://github.com/oppia/oppia/wiki/Contributing-to-Oppia%27s-design)
...
```

## Getting Started

To begin contributing:

1. **Clone the Repository**: Follow the [Installation Instructions](https://github.com/oppia/oppia/wiki/Installing-Oppia) in the `README.md`.

2. **Explore Key Areas**: Familiarize yourself with the `core/`, `extensions/`, and `assets/` directories.

3. **Run Tests**: Ensure your environment is set up correctly by running existing tests.

4. **Choose an Issue**: Browse issues labeled for beginners or specific areas you're interested in.

5. **Follow Contribution Guidelines**: Adhere to the guidelines outlined in `.github/CONTRIBUTING.md` and use the pull request templates provided.

## Additional Resources

- **[Oppia Community Site](https://www.oppia.org)**
- **[User Documentation](https://oppia.github.io/)**
- **[Contributors' Wiki](https://github.com/oppia/oppia/wiki)**
- **[GitHub Discussions](https://github.com/oppia/oppia/discussions)**
- **[Developer Announcements](http://groups.google.com/group/oppia-dev)**
- **[Code Owners Guidelines](https://github.com/oppia/oppia/wiki/Oppia's-code-owners-and-checks-to-be-carried-out-by-developers)**

By following this roadmap, you'll gain a comprehensive understanding of the Oppia codebase, enabling you to contribute effectively and efficiently.