# LMS System for Learning Programming Languages

## Intro:
Welcome to the Learning Management System (LMS) project for learning programming languages. This repository contains the source code and project files for the LMS system. Follow the instructions below to get started with setting up the project on your local environment and collaborating with the team.

Please visit [Markdown](#https://code.visualstudio.com/Docs/languages/markdown) for more information on Markdown
## Table of Contents:
- [Intro](#intro)
- [Installation](#installation)
    - [Cloning the Repository](#cloning-the-repository)
    - [Environment Setup](#setting-up-the-development-environment)
- [Collaboration](#collaboration)
    - [Discussions and Projects on GitHub](#discussions-and-projects-on-gitHub)
      - [Discussions](#github-discussions)
      - [Github Project](#github-project)
    - [Project Structure](#project-structure)
    - [Branching Methodology](#branching-methodology)
    - [Pull Request](#pull-request)
    - [Releases](#releases)
    - [Namind and Style convention](#naming-and-style-convention)
    - [CSS Styling](#css-styling)
- [Learning Outcomes](#learning-outcomes)
- [Project Requirements](#project-requirements)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact](#contact)
## Installation:
### Cloning the Repository

To clone the repository to your local environment, follow these steps:

- 1. Open your terminal in VS Code.
- 2. Navigate to the directory where you want to store the project.
- 3. Run the following command to clone the repository:

```
git clone https://github.com/The-Digital-Dilemma/GetIT.git
```

- 4. Press Enter to create your local clone

Please visit [Cloning a Repository](#https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#about-cloning-a-repository) documentation for more information.

### Setting Up the Development Environment

Before running the project, make sure you have the following prerequisites installed:

- asgiref==3.7.2
- Django==4.2.2
- sqlparse==0.4.4
- typing_extensions==4.6.3

Follow these steps to set up the development environment:

- 1. Create and activate a virtual environment:

```
python -m venv myenv
```

Replace myenv with the desired name for your virtual environment.

For MacOS/Linux:

```
source myenv/bin/activate
```

For Windows:

```
.\myenv\Scripts\activate
```

- 2. Install the project dependencies:

```
pip install -r requirements.txt
```

- 3. Apply database migrations:

```
python manage.py migrate
```

- 4. Start the development server:

```
python manage.py runserver
```

The project will be accessible at http://localhost:8000 in your web browser.

## Collaboration:

### Discussions and Projects on GitHub:

GitHub provides features like Discussions and Projects to facilitate collaboration and organization within a project. 

#### Github Discussions:

Discussions allow for asynchronous conversations and are particularly useful for open-ended discussions, Q&A sessions, or brainstorming.
- **1. Create relevant categories:** Organize discussions into specific categories or topics based on their nature. This helps team members find and participate in discussions that are relevant to them.
- **2. Provide clear context:** When starting a new discussion, provide a clear and concise description of the topic to ensure everyone understands its purpose. Include any relevant background information, goals, or questions to guide the conversation.
- **3. Use @mentions:** When referencing specific individuals or teams in a discussion, use the @mention feature to notify them and draw their attention. This ensures that the relevant parties are aware of the discussion and can provide input if needed.
- **4. Follow up and summarize:** As discussions progress, periodically summarize the key points, decisions, or action items. This helps consolidate the information and provides a reference for future discussions or decision-making processes.

#### Github Projects:

Projects is a flexible tool for managing and organizing project tasks, issues, or feature requests. 
- **1. Create project boards:** Set up project boards to represent different stages or workflows within your project. For example, you can have boards for "To Do," "In Progress," and "Completed" tasks. This visual representation provides an overview of the project's progress and helps team members stay organized.
- **2. Add and manage cards:** Create cards within project boards to represent individual tasks, issues, or feature requests. Assign team members to specific cards and add relevant labels or due dates. As work progresses, move cards across the project boards to reflect their current status.
- **3.Use issue integration:** Link project boards with issues in your repository. This allows you to create cards directly from issues, providing seamless integration between the two. Updates made to the cards or issues are reflected in real-time, ensuring transparency and alignment.
- **4. Collaborate and discuss:** Encourage team members to use the card's comment section for discussions, updates, or clarifications related to a specific task. This keeps the conversation contextually linked to the task, making it easier to track progress and decisions.
- **5Track milestones:** Utilize milestones within Projects to group related tasks or issues together. Milestones help establish deadlines or target dates for achieving specific project objectives. They provide a high-level overview of progress towards project milestones or releases.

If ensure, I would recommend to create an issue not too specific and inside that issue, create a tasks list, as each items in the list can be converted to an issue.


### Project Structure:

```
- GetIT (main app)
- courses app
- home app
- users app
- static folder
- db.sqlite3
- manage.py
```
In this structure, the project folder contains the following components:

* GetIT (main app): The main app of the project.
* courses app: An app dedicated to handling courses-related functionalities.
* home app: An app responsible for the home page or landing page of the project.
* users app: An app for managing user-related functionalities.
* static folder: A folder that stores static files such as CSS, JavaScript, and images.
* db.sqlite3: The SQLite database file used by the project.
* manage.py: The entry point for Django's management commands.

### Branching Methodology:

For this small project, we can follow a simple branching methodology to organize our work effectively. Here are some steps to consider:

* **1. Main Branch:** The `main` branch serves as the main development branch, where we merge completed features.
* **2. Feature Branches:** Whenever you start working on a new feature or bug fix, create a new branch from `main`. Use a descriptive name for the branch that reflects the feature you are working on.
* **3. Commits:** Make small, atomic commits while working on your feature. This allows for easier review and helps in isolating issues if they arise.
* **4. Pull Requests:** Once you have completed your feature or bug fix, create a pull request to merge your branch into `main`. Assign the pull request to the lead team member for review.
* **5. Review and Merge:** After the review process, make any necessary changes based on the feedback. Once the branch is approved, it can be merged into `main`.

[About branches- Github](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)

### Pull Request:

Once you make your desired changes on the file from your branch:

* **1. Commit the Changes:** Add the modified files to the staging area and commit the changes with a descriptive commit message. This captures the snapshot of your changes.
* **2. Push the Changes:** Push the committed changes to the repository on GitHub. This updates the remote repository with your latest changes.

Once all the necessary commits have been made to solve the issue or achieve the goal, the team can create a pull request. This step ensures that the changes are ready for review as a cohesive unit.
* Before creating the pull request, ensure that all relevant commits addressing the specific issue or goal have been pushed to the branch associated with the pull request.
* Make sure to provide a descriptive title and additional comments in the pull request, summarizing the work done and providing context if necessary.
* Include any relevant information, such as references to related issues, project boards, or specific instructions for reviewing the changes.
* It can be beneficial to discuss the pull request with team members or collaborators before creating it, to ensure that the changes are complete and ready for review.
* Once the pull request is created, it will be reviewed by the repository maintainers or project collaborators, who will provide feedback and suggestions for improvement.
* Iterate and update the pull request as needed, addressing the feedback received and making any necessary changes until the changes are approved for merging.

[About pull requests - Github](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

### Releases:

### Naming and Style Convention:

Consistent naming and styling conventions enhance code readability and maintainability. Although there are no strict rules, adopting widely accepted conventions promotes collaboration and reduces confusion. Consider the following guidelines:

- **Python:** Follow the [PEP 8 guidelines](https://pep8.org) for Python code, including naming conventions for variables, functions, classes, and modules. Use descriptive names and avoid abbreviations when possible.
- **Django:** Adhere to Django's coding style guidelines, including naming conventions for models, views, templates, URLs, and other components. Use lowercase letters and underscores for most names (e.g., my_model, my_template.html).
- **HTML/CSS:** Use descriptive and meaningful class and ID names in HTML and CSS. Consider using a naming convention like BEM (Block, Element, Modifier) to keep your styles organized and modular.[Block, Element, Modifier](https://css-tricks.com/bem-101/)
- **JavaScript:** Follow established JavaScript coding conventions like [the Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html). Use camelCase for variable and function names.

### CSS Styling:

To maintain consistent styling across our project, it's a good practice to define a root CSS file that contains common styles and colors. This file can be imported in other CSS files for easy access.
```
/* styles.css */

:root {
  --primary-color: #007bff;
  --secondary-color: #6c757d;
  /* Define more variables as needed */
}
```
Then to use defined colors:
```
/* custom_styles.css */

body {
  background-color: var(--primary-color);
  color: var(--secondary-color);
}
```

## Learning Outcomes:

This assessment contributes to the following course learning outcomes:

- **LO 1:** Integrate security and privacy principles throughout Software Development Life Circle (SDLC) to ensure web application security and system level integrity through application of current best IT industry practices
- **LO 3:** Develop secure web applications using web frameworks and server-side scripting. 
- **LO 4:** Apply core software development practices in web application development in organisational context.
  
## Project Requirements:

- **Task 1:** Team setup, software development management and tools selection
- **Task 2:** Requirement analysis, security and privacy policies set up
- **Task 3:** Implementation:
    - Set up the development environment
    - Set up a collaboration repository on GitHub
    - URLs design and implementation 
    - Authentication implementation:
        - Set up “signup” and “login” views
        - Create an admin user
        - Create users and user groups as per the project requirements
    - Authorisation implementation:
        - User and group permissions are set up as per the project requirements
- **Task 4:** Reflective journal (individual task)


## License:

The "License" section specifies the terms and conditions under which the project is released.
This project is currently license-free (2023)


## Acknowledgments:

This section will be accomplished at the end of the project.

## Contact:


