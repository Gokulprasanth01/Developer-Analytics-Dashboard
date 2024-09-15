import pandas as pd
from datetime import timezone

class MetricsCalculator:
    @staticmethod
    def calculate_commit_frequency(commit_data):
        commit_data['date'] = pd.to_datetime(commit_data['date'])
        daily_commits = commit_data.groupby(commit_data['date'].dt.date).count()['sha']
        return daily_commits

    @staticmethod
    def calculate_pr_merge_rate(pr_data):
        if 'state' not in pr_data.columns or 'merged_at' not in pr_data.columns:
            return None
        merged_prs = pr_data[pr_data['state'] == 'closed']
        merge_rate = len(merged_prs[merged_prs['merged_at'].notna()]) / len(pr_data) * 100
        return merge_rate

    @staticmethod
    def calculate_issue_resolution_time(issue_data):
        if 'created_at' not in issue_data.columns or 'closed_at' not in issue_data.columns:
            return None
        issue_data['created_at'] = pd.to_datetime(issue_data['created_at'])
        issue_data['closed_at'] = pd.to_datetime(issue_data['closed_at'])
        issue_data['resolution_time'] = (issue_data['closed_at'] - issue_data['created_at']).dt.days
        return issue_data[['number', 'resolution_time']]

    @staticmethod
    def calculate_repo_info(repo_info):
        # Get the current time in UTC
        current_time = pd.Timestamp.now(tz='UTC')
        
        # Check if 'created_at' is timezone-aware
        created_at = repo_info["created_at"]
        
        if created_at.tzinfo is None:
            # If 'created_at' is naive (no timezone), localize it to UTC
            created_at_utc = created_at.replace(tzinfo=timezone.utc)
        else:
            # If 'created_at' is already timezone-aware, just convert it to UTC
            created_at_utc = created_at.astimezone(timezone.utc)

        # Calculate repository age in days
        return {
            "stars": repo_info["stars"],
            "forks": repo_info["forks"],
            "watchers": repo_info["watchers"],
            "open_issues": repo_info["open_issues"],
            "age_days": (current_time - created_at_utc).days
        }
