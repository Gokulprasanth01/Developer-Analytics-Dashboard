# GitHub Performance Dashboard

This project provides a simple dashboard to analyze GitHub repository performance, including pull request statistics, issue tracking, and more. It is built using Streamlit and Python, with GitHub's REST API for data collection.

## Objective

The objective of this project is to create an interactive dashboard that allows users to input a GitHub repository URL, analyze the repository’s performance, and answer specific questions (like pull request merge rate) based on the collected data.

## Features

- Analyze GitHub repositories by simply entering a URL.
- Get real-time statistics such as:
  - PR merge rate.
  - Open and closed issues.
  - Top contributors.
  - Repository activity metrics.
- Natural language interface to ask questions related to repository performance.

## Techniques Used

- **Streamlit**: For creating an interactive dashboard and user-friendly interface.
- **GitHub REST API**: For fetching repository data such as pull requests, issues, and commits.
- **Python**: Backend logic for data processing and analysis.
- **Natural Language Processing (NLP)**: To answer questions like "What is the PR merge rate?" after analyzing the repository data.

## How to Run the Demo

To run this project locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/github-performance-dashboard.git
cd github-performance-dashboard
### 2. Install Dependencies

Before running the app, ensure you have Python installed on your machine (preferably version 3.7+). Then, install the required packages by running:

```bash
pip install -r requirements.txt
```

### 3. Running the Application

After installing the dependencies, you can start the Streamlit app by running the following command:

```bash
streamlit run app.py
```

This will launch the dashboard in your default web browser at `http://localhost:8501`.

### 4. Using the Application

- **Step 1**: Enter the GitHub repository URL in the input field and click on "Analyze".
- **Step 2**: Once the analysis is complete, use the text input to ask questions like:
  - "What is the PR merge rate?"
  - "How many issues are open?"
  - "Who are the top contributors?"

The dashboard will process your query and display the result below.


## Example Queries

Here are some example queries you can use after analyzing a GitHub repository:

- **What is the PR merge rate?**
  - This question will display the ratio of merged pull requests to total pull requests.
- **How many issues are open?**
  - This will show the number of open issues for the repository.
- **Who are the top contributors?**
  - This will return the list of users who have contributed the most to the repository.

## Contributing

We welcome contributions to improve this project! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes.
4. Submit a pull request with a detailed explanation of your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

If you have any questions or suggestions regarding the project, feel free to reach out to:

- **Author**: Gokulprasanth N
- **Email**: gokulprasanth@example.com
```
