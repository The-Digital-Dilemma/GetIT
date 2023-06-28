# LMS System for Learning Programming Languages

## Intro:
Welcome to the Learning Management System (LMS) project for learning programming languages. This repository contains the source code and project files for the LMS system. Follow the instructions below to get started with setting up the project on your local environment and collaborating with the team.

Please visit [Markdown](#https://code.visualstudio.com/Docs/languages/markdown) for more information on Markdown

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

**1. Commit the Changes:** Add the modified files to the staging area and commit the changes with a descriptive commit message. This captures the snapshot of your changes.
**2. Push the Changes:** Push the committed changes to the repository on GitHub. This updates the remote repository with your latest changes.

Once all the necessary commits have been made to solve the issue or achieve the goal, the team can create a pull request. This step ensures that the changes are ready for review as a cohesive unit.
* Before creating the pull request, ensure that all relevant commits addressing the specific issue or goal have been pushed to the branch associated with the pull request.
* Make sure to provide a descriptive title and additional comments in the pull request, summarizing the work done and providing context if necessary.
* Include any relevant information, such as references to related issues, project boards, or specific instructions for reviewing the changes.
* It can be beneficial to discuss the pull request with team members or collaborators before creating it, to ensure that the changes are complete and ready for review.
* Once the pull request is created, it will be reviewed by the repository maintainers or project collaborators, who will provide feedback and suggestions for improvement.
* Iterate and update the pull request as needed, addressing the feedback received and making any necessary changes until the changes are approved for merging.

[About pull requests - Github](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

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




## Usage:

## Contributing:

## License:

## Acknowledgments:

This section will be accomplished at the end of the project.

## Troubleshooting:

## FAQ:

## Changelog:

