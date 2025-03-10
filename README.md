# Git, Testing, and CI Learning Repository

This repository is designed for first-year engineering students to learn essential software engineering practices: Git version control, automated testing with pytest, and Continuous Integration (CI) using GitHub Actions. The Python exercises serve as a vehicle for practicing these concepts.

## Repository Structure

- `exercise1/`: Basic calculator functions
- `exercise2/`: String manipulation utilities
- `exercise3/`: Temperature conversion functions
- `tests/`: Test files for all exercises

## Learning Objectives

1. **Git Version Control**: Learn forking, branching, committing changes, and creating pull requests
2. **Test-Driven Development**: Understand how to write and run tests with pytest
3. **Continuous Integration**: Experience how GitHub Actions can automate your testing workflow

## Getting Started

1. **Fork this repository**:
   - Click the "Fork" button at the top right of this repository page
   - This creates a copy of the repository under your GitHub account

2. **Clone your forked repository**:
   ```bash
   git clone https://github.com/your-username/learn-git-pytest.git
   cd learn-git-pytest
   ```

3. **Create a branch with your name**:
   ```bash
   git checkout -b firstname-lastname
   ```

4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Implement the required functions**:
   - Complete the functions in each `.py` file
   - Run the tests locally to check your implementation:
     ```bash
     pytest tests/
     ```

6. **Commit your changes**:
   ```bash
   git add .
   git commit -m "Implement solutions for exercises"
   ```

7. **Push your branch to your fork**:
   ```bash
   git push -u origin firstname-lastname
   ```

## GitHub Actions CI Pipeline

This repository uses GitHub Actions to automatically run tests whenever you push changes to your branch. The workflow:

1. Checks out your code
2. Sets up Python
3. Installs dependencies
4. Runs type checking with mypy
5. Executes all tests with pytest

Check the results in the "Actions" tab of your forked GitHub repository after pushing your changes. Fix any failing tests before submission.

## Submission Process

When you've completed all exercises and all tests pass:

1. Make sure all your changes are committed and pushed to your branch
2. Go to the **original** repository (not your fork)
3. Click on "Pull Requests" and then "New Pull Request"
4. Click on the link "compare across forks"
5. Set the base repository to the original course repository and base branch to `main`
6. Set the head repository to your fork and the compare branch to your `firstname-lastname` branch
7. Add a title like "Exercise Solutions - Firstname Lastname"
8. Click "Create Pull Request"
9. Notify your instructor that you've submitted your pull request

## What to Expect After Submission

Your instructor will:
1. Review your code
2. Verify that all tests pass in the CI pipeline
3. Provide feedback through the pull request comments
4. Either approve and merge your changes or request modifications

Happy coding and testing!

