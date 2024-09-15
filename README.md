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
```

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
- **Email**: gokulprasanth0127@gmail.com

![{E9ECFCD3-B570-47D1-8655-F34FE9B1E367}](https://github.com/user-attachments/assets/da7c2e0a-81d9-4ade-9017-c8693d59fd22)
![{33A4BA3A-A1C2-47CA-BC2A-B5D466EA290E}](https://github.com/user-attachments/assets/94f7da25-87a4-49b7-9cfd-0f8a7235a683)
![{6CA3CBFC-9C53-4BD5-B165-877AEFBEC5F2}](https://github.com/user-attachments/assets/bfd856a7-6391-4c7e-9df5-2de9faa55a1c)
![{9ABAAF5E-32C0-4244-9DFB-B9684281D5F4}](https://github.com/user-attachments/assets/15241f41-e875-4a40-b801-6db5c14f3b19)
![{510FE216-25C9-4A54-A821-B0223F1A4E6F}](https://github.com/user-attachments/assets/7fe35fd2-129c-4ac4-8b4e-951e921cbe67)
![{84FE665B-AE8A-457A-8F9E-6BDB92A9CA69}](https://github.com/user-attachments/assets/4f31de63-f2bf-4c4b-98aa-da99993f5261)

