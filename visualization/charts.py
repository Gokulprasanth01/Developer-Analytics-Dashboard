import plotly.express as px
import streamlit as st

def plot_commit_frequency(daily_commits):
    fig = px.line(
        daily_commits, 
        title="Commit Frequency Over Time", 
        labels={'value': 'Commits', 'index': 'Date'},
        template="plotly_dark"
    )
    fig.update_traces(mode="lines+markers", hoverinfo="text", marker=dict(size=10, color="blue"))
    fig.update_layout(xaxis_title="Date", yaxis_title="Number of Commits", hovermode="x unified")
    st.plotly_chart(fig)

def plot_pr_merge_rate(merge_rate):
    fig = px.pie(
        values=[merge_rate, 100 - merge_rate],
        names=['Merged PRs', 'Unmerged PRs'],
        title=f"PR Merge Rate: {merge_rate:.2f}%",
        hole=0.5,
        color_discrete_sequence=["#00CC96", "#EF553B"]
    )
    fig.update_traces(textinfo="percent+label", pull=[0.1, 0])
    st.plotly_chart(fig)

def plot_issue_resolution_time(issue_res_times):
    fig = px.bar(
        issue_res_times, 
        x='number', 
        y='resolution_time', 
        title="Issue Resolution Time (Days)",
        template="plotly_dark",
        hover_data=['resolution_time'],
        color="resolution_time",
        color_continuous_scale=px.colors.sequential.Viridis
    )
    fig.update_layout(xaxis_title="Issue Number", yaxis_title="Resolution Time (Days)", hovermode="closest")
    st.plotly_chart(fig)

    # Distribution of resolution times
    fig2 = px.histogram(
        issue_res_times, 
        x="resolution_time", 
        nbins=20, 
        title="Distribution of Issue Resolution Times",
        template="plotly_dark",
        labels={'resolution_time': 'Resolution Time (Days)'}
    )
    fig2.update_layout(bargap=0.2)
    st.plotly_chart(fig2)

def display_repo_info(repo_info):
    st.write(f"Stars: {repo_info['stars']}")
    st.write(f"Forks: {repo_info['forks']}")
    st.write(f"Watchers: {repo_info['watchers']}")
    st.write(f"Open Issues: {repo_info['open_issues']}")
    st.write(f"Repository Age (Days): {repo_info['age_days']}")
