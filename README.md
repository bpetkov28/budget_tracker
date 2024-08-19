# Budget Tracker
## Overview
Budget Tracker is a Python application designed to help users monitor and manage their personal expenses. The app allows users to add expenses with details such as date, category, description, and amount. Users can also generate reports to view their expenses by day and by category for a selected month and year.

Current Version: **Beta**

Features:

- Add expenses with date, category, description, and amount.
- Generate reports to view expenses by day and category for a selected month and year.
Note: The application is in its beta version. Features like input validation and tracking remaining budget for the month are still under development.

## Getting Started
### Prerequisites
Ensure you have Python 3.12 or higher installed on your machine. You can download it from python.org.

### Installation
- Clone the repository to your local machine:

```bash
  git clone https://github.com/bpetkov28/budget_tracker.git
```

- Navigate to the project directory:

```bash
  cd budget_tracker
```
- Install the required dependencies:

```bash
  pip install -r requirements.txt
```
### Usage
1. Run the Application main.py file

- To start the application, run:

```bash
  python main.py
```

Follow the on-screen instructions to add expenses and generate reports.

2. Adding an Expense

 - Date: Specify the date of the expense from the calendar.
 - Category: Choose a category from the dropdown menu.
 - Description: Provide a short description of the expense.
 - Amount: Enter the amount spent.

3. Generating a Report

 - Click the Report button
 - Select the desired month and year to view your expenses.
 - The report will display your expenses broken down by day and by category for the chosen month.

### Development
To contribute to the development of this project, follow these steps:

1. Fork the repository on GitHub.

2. Create a new branch for your feature or bug fix:

```bash
  git checkout -b feature-branch-name
```

3. Make your changes and commit them:

```bash
  git add .
  git commit -m "Describe your changes"
```
4. Push your changes to your forked repository:

```bash
  git push origin feature-branch-name
```

5. Create a pull request on GitHub.

### Known Issues
- Input validation is not yet implemented. Users may need to manually ensure that the date, amount, and other inputs are correct.
- Remaining budget tracking for the month is still under development.

### Future Enhancements
- Implement input validation to ensure correct and meaningful data entries.
- Develop features to track and display remaining budget for the month.
- Add new report functionalities.
- Improve user interface and experience.

### Contact
For any questions or suggestions, please contact bozhidar192@gmail.com
