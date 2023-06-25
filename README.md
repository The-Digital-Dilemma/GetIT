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

Strategy need to be established with the group for Branching, commiting changes and pushing changes.

## Usage:

## Contributing:

## License:

## Acknowledgments:

## Troubleshooting:

## FAQ:

## Changelog:

