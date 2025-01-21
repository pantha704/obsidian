

Certainly! Here's a roadmap to help you navigate the Oppia repository effectively:

### 1. Main Directory Structure

- **`core/`**: Contains the main application logic, including backend controllers, domain services, platform-specific services, storage models, and frontend templates.
  - **`controllers/`**: Backend controllers and their tests.
  - **`domain/`**: Services and classes for various data models.
  - **`platform/`**: Google App Engine services.
  - **`storage/`**: Definitions for storage models.
  - **`templates/`**: Frontend directives, controllers, filters, and services.
  - **`tests/`**: End-to-end tests for various pages.
  - **`README.md`**: Overview of the `core` folder contents.
    
```1:9:core/README.md
This folder contains the scripts for Oppia backend & frontend.

- controllers: Backend controllers & tests for them.
- domain: Services & classes for various data models used in Oppia codebase.
- platform: Google app engine services.
- storage: Definitions for storage models on Google App engine.
- templates: All the frontend directive, controllers, filters & services.
- tests: E2E tests for various Oppia pages.

```


- **`extensions/`**: Frontend and backend code for various extensions and plugins.
  - **`README.md`**: Overview of the `extensions` folder contents.
    
```1:12:extensions/README.md
This folder contains the frontend & backend code for various extensions & plugins used in Oppia codebase.

- actions: Definitions of domain classes for various user actions on Oppia website.
- answer_summarizers: Model definitions for answer summarizers.
- ckeditor_plugins: Plugins used in CKEditor RTE.
- classifiers: Various common services used for tokenization and prediction.
- interactions: The frontend & backend code for interactions supported on Oppia website.
- objects: The frontend & backend code for various typed editors like boolean editor, filepath editor etc.
- rich_text_components: The frontend & backend code for rich text components supported on Oppia RTE.
- value_generators: The frontend & backend code for value generators used in Oppia.
- visualizations: The frontend & backend code for visualizations used in Oppia.

```


- **`assets/`**: Contains various assets like images, scripts, and translations.
  - **`README.md`**: Overview of the `assets` folder contents.
    
```1:9:assets/README.md
This folder contains various assets used in Oppia codebase.

- i18n: Contains the translations for supported languages.
- images: Images used in various pages on Oppia website.
- overrides: Overrides for third party.
- pages: Attribution message.
- scripts: Scripts for exploration embeddings & testing.
- videos: Videos used in various pages on Oppia website.

```


- **`.github/`**: Contains GitHub-specific files like issue templates, pull request templates, and workflows.
  - **`CONTRIBUTING.md`**: Guidelines for contributing to the project.
    
```6:17:.github/CONTRIBUTING.md

- [Coders](https://github.com/oppia/oppia/wiki/Contributing-code-to-Oppia)
- [Instructional designers and storytellers](https://github.com/oppia/oppia/wiki/Teaching-with-Oppia)
- [UX researchers](https://github.com/oppia/oppia/wiki/Conducting-research-with-students)
- [Voice artists](https://github.com/oppia/oppia/wiki/Instructions-for-voice-artists)
- [Designers and artists](https://github.com/oppia/oppia/wiki/Contributing-to-Oppia%27s-design)

If you are interested in working on Oppia's Android app, you should also take a look at the [oppia/oppia-android repository](https://github.com/oppia/oppia-android).

If you run into any problems, you can check out the [user documentation](http://oppia.github.io/) or post to our [developer mailing list](https://groups.google.com/forum/?fromgroups#!forum/oppia-dev). Feel free to drop into our [Gitter chat channel](https://gitter.im/oppia/oppia-chat) to say hello, too :)

Finally, if, after reading the above links, you'd like to help, but aren't sure how -- don't worry! The Oppia project is very multi-faceted, and we'd be glad to help you find something to do that matches your interests and skills. Just fill out [this form](https://forms.gle/jEytndtgdsx7BrnV6) to let us know what you'd like to help with, or write to us at [volunteer@oppia.org](mailto:volunteer@oppia.org) and tell us a bit about yourself and what you'd like to do. We'll do our best to help you get started!
```


### 2. Key Files and Their Roles

- **Configuration Files**:
  - **`.github/CODEOWNERS`**: Defines code ownership for different parts of the codebase.
    
```1:28:.github/CODEOWNERS
# Per-directory ownership and automatic assignment for pull requests.

# The paths to the directory/files must be relative to the location of this
# file. Wildcards such as '**', '!' are not allowed. Only glob style patterns
# are allowed. For information about supported glob patterns please refer
# https://docs.python.org/2/library/glob.html.

# IMPORTANT NOTES FOR DEVELOPERS:
#
# - When assigning codeowners for new files, please do so by picking an
#   appropriate team lead from this page:
#
#       https://github.com/oppia/oppia/projects
#
#   You do not need to assign yourself as a codeowner (unless you are a project
#   lead listed on the page above).

# IMPORTANT NOTES FOR CODEOWNERS:
#
# - If you will be unavailable for more than 24 hours, please replace your
#   ownership with a delegate, file an issue, and add a todo above the owner
#   line like so:
#
#     TODO(#ISSUE_NUMBER): Revert ownership to @USERNAME after YYYY-MM-DD.
#
#   (See #10252 for an example.) Please make sure to restore ownership after
#   the above date passes.

```


- **Main Application Files**:
  - **`main.py`**: Entry point for the backend application.
    
```34:61:main.py
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


- **Test Files**:
  - **`core/tests/`**: Contains various test files and configurations.
  - **`core/tests/test-dependencies/README.md`**: Describes the purpose of test dependencies.
    
```1:2:core/tests/test-dependencies/README.md
This folder holds the files that are needed mainly when running the scripts.check_ci_test_suites_to_run. The files root-files-mapping-generator.ts and typescript-ast-utilities.ts are used to find which root modules and files are linked together. The test-to-modules-matcher.ts and route-to-module-mapping-generator.ts are used by acceptance tests to find out which modules are affected by a certain test. For more information refer to the wiki page here: https://github.com/oppia/oppia/wiki/Partial-CI-Tests-Structure.

```


### 3. Overall Architecture and Data Flow

The Oppia application is structured around a modular architecture, with clear separation between backend and frontend components. The backend is primarily responsible for handling data processing and business logic, while the frontend manages user interactions and presentation.

- **Backend**: Managed through controllers and domain services, which handle requests and interact with storage models.
- **Frontend**: Built using Angular, with templates and components defined in the `core/templates` directory.

### 4. Typical Workflows or Functions

- **Entry Point**: The application starts with `main.py`, which imports various controllers to handle different routes and functionalities.
- **Core Logic**: Resides in the `core/domain` and `core/controllers` directories, where business logic and request handling are implemented.

### 5. Conventions and Best Practices

- **Naming Conventions**: Use descriptive names with auxiliary verbs for variables (e.g., `isLoading`, `hasError`).
- **Styling**: Follow the guidelines in the `core/templates/css/README.md` for CSS modifications.
  
```1:30:core/templates/css/README.md
# CSS

## Overview

This folder contains all the global style sheets for the oppia frontend.

## Files:

1. oppia.css — Custom css styles written by the oppia-devs for the frontend.
2. oppia-material.css — Material CSS for the oppia-codebase. This css file is generated and shouldn't be modified at all.

## Modification procedure:

1. oppia.css can be modified with proper reasoning in the pr that modifies the file.
2. oppia-material.css shouldn't be changed at any cost. No changes are accepted in this file.
   If, at any time, the oppia-material.css is overriding the styles in oppia.css, create a style tag in the directive and make the selectors more specific.

## Oppia Material

**If at any time the css file is regenerated please update the pr number here**

- Introduced in: #9577
- Updated in: N/A (Comma separated pr numbers).

### Info

More info regarding the oppia-material.css can be found in this doc:
Material CSS doc: https://docs.google.com/document/d/1UoCOC7XNhCZrWIMPAoR5Xex28OYWzteqXrqCU9gRUHQ/edit?usp=sharing

### Steps to generate oppia-material.css file:
```


- **Code Structure**: Favor modularization and iteration over duplication. Use functional programming patterns where possible.

This roadmap should provide a solid foundation for understanding the Oppia codebase and contributing effectively. If you have any specific questions or need further details, feel free to ask!