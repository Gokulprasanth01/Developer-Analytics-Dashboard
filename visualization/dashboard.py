import streamlit as st

from visualization.charts import plot_commit_frequency, plot_issue_resolution_time, plot_pr_merge_rate

def display_dashboard(repo_info, commit_freq, pr_merge_rate, pr_data, issue_resolution_times):
    # Display repository info in the sidebar
    st.title("Enhanced GitHub Performance Dashboard")

    # Sidebar for filters and options
    with st.sidebar:
        st.header("Repository Info")
        st.write(f"**Stars:** {repo_info['stars']}")
        st.write(f"**Forks:** {repo_info['forks']}")
        st.write(f"**Watchers:** {repo_info['watchers']}")
        st.write(f"**Open Issues:** {repo_info['open_issues']}")
        st.write(f"**Repository Age (Days):** {repo_info['age_days']}")
    
    # Main dashboard section
    col1, col2, col3 = st.columns([2, 2, 2])

    # Summary of Metrics
    with col1:
        st.metric(label="Total Commits", value=len(commit_freq))
        st.metric(label="Open Issues", value=repo_info['open_issues'])
    with col2:
        # Replace len(pr_merge_rate) with len(pr_data), which represents the number of PRs
        st.metric(label="Pull Requests", value=len(pr_data))  # Use the actual length of PRs
    with col3:
        # Display pr_merge_rate as a percentage value
        st.metric(label="PR Merge Rate", value=f"{pr_merge_rate:.2f}%")  # Display PR merge rate as a percentage

    # Container for charts
    st.subheader("Commit Activity")
    st.write("Track the frequency of commits over time.")
    
    # Plot commit frequency chart here
    plot_commit_frequency(commit_freq)

    # Additional sections for PR and issue performance
    st.subheader("Pull Request (PR) Performance")
    st.write("Visualizing the pull request merge rate.")
    
    # Other visualization functions can be added here similarly
    plot_pr_merge_rate(pr_merge_rate)
    
    # Additional sections for PR and issue performance
    st.subheader("Issue Performance")
    st.write("Visualizing issue resolution times.")
    
    plot_issue_resolution_time(issue_resolution_times)
