import os
import streamlit as st
from data_collection.github_api import GitHubDataCollector
from data_collection.data_storage import DataStorage
from metrics.calculator import MetricsCalculator
from visualization.dashboard import display_dashboard
from query_interface.nlp_processor import NLPQueryProcessor  # Import the NLP Processor

# Initialize GitHub API token and the DataStorage instance for CSV storage
token = os.getenv("GITHUB_TOKEN")
collector = GitHubDataCollector(token)
storage = DataStorage(filename="github_data.xlsx")
nlp_processor = NLPQueryProcessor()  # Initialize the NLP processor

# Initialize session state for the query and result
if 'user_query' not in st.session_state:
    st.session_state.user_query = ""  # Initialize empty query
if 'query_result' not in st.session_state:
    st.session_state.query_result = ""  # Initialize empty result

st.title("GitHub Performance Dashboard")
repo_url = st.text_input("Enter GitHub Repository URL", "https://github.com/user/repo")

if st.button("Analyze"):
    data = collector.get_repo_data(repo_url)
    
    if data:  # Check if data fetching was successful
        # Save the data to CSV using the DataStorage class
        storage.save_to_csv(data['repo_info'], data['commit_data'], data['pr_data'], data['issue_data'])

        # Calculate metrics for the dashboard
        commit_freq = MetricsCalculator.calculate_commit_frequency(data['commit_data'])
        pr_merge_rate = MetricsCalculator.calculate_pr_merge_rate(data['pr_data'])  # This is a float
        issue_resolution_times = MetricsCalculator.calculate_issue_resolution_time(data['issue_data'])
        repo_info = MetricsCalculator.calculate_repo_info(data['repo_info'])

        # Display the dashboard with the calculated metrics
        display_dashboard(repo_info, commit_freq, pr_merge_rate, data['pr_data'], issue_resolution_times)

        # Load the CSV content for download
        csv_data = storage.get_csv_data()

        # Create a download button for the CSV file
        st.download_button(
            label="Download GitHub Data as CSV",
            data=csv_data,
            file_name="github_data.xlsx",  # The CSV file will be downloaded as an Excel file
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        # **Natural Language Query Section**
        st.subheader("Ask a Question")
        user_query = st.text_input("Ask a question about the repository's performance metrics:", value=st.session_state.user_query, key="user_query")

        # Process the user's query when it's submitted
        if user_query and st.session_state.query_result == "":
            metric = nlp_processor.process_query(user_query)

            # Save the result to session state so it persists after the page reloads
            if metric == "commit_frequency":
                st.session_state.query_result = "Showing commit frequency data."
            elif metric == "pr_merge_rate":
                st.session_state.query_result = f"The Pull Request Merge Rate is {pr_merge_rate:.2f}%."
            elif metric == "issue_resolution_time":
                st.session_state.query_result = "Displaying issue resolution times."
            elif metric == "repo_info":
                st.session_state.query_result = "Displaying repository information."
            else:
                st.session_state.query_result = "Sorry, I don't understand that question."

# Display the stored query result after reload
if st.session_state.query_result:
    st.write(st.session_state.query_result)