from github import Github
import pandas as pd

class GitHubDataCollector:
    def __init__(self, token):
        self.g = Github(token)

    def get_repo_data(self, repo_url):
        try:
            # Split the URL and get the owner/repo name
            repo_name = repo_url.split("/")[-1]
            owner_name = repo_url.split("/")[-2]
            
            # Fetch the repository data from the GitHub API
            repo = self.g.get_repo(f"{owner_name}/{repo_name}")
            
            # Get general repo information
            repo_info = {
                "owner_name": owner_name,  
                "repository_name": repo_name,
                "stars": repo.stargazers_count,
                "forks": repo.forks_count,
                "watchers": repo.watchers_count,
                "open_issues": repo.open_issues_count,
                "created_at": repo.created_at,
                "updated_at": repo.updated_at
            }
            
            # Get commits
            commits = repo.get_commits()
            commit_data = [
                {
                    "sha": c.sha,
                    "author": c.commit.author.name,
                    "date": c.commit.author.date,
                    "message": c.commit.message
                }
                for c in commits
            ]
            
            # Get pull requests
            pull_requests = repo.get_pulls(state='all')
            pr_data = [
                {
                    "number": pr.number,
                    "state": pr.state,
                    "created_at": pr.created_at,
                    "closed_at": pr.closed_at,
                    "merged_at": pr.merged_at,
                    "title": pr.title
                }
                for pr in pull_requests
            ]
            
            # Get issues
            issues = repo.get_issues(state='all')
            issue_data = [
                {
                    "number": i.number,
                    "state": i.state,
                    "created_at": i.created_at,
                    "closed_at": i.closed_at,
                    "title": i.title
                }
                for i in issues
            ]
            
            return {
                "repo_info": repo_info,
                "commit_data": pd.DataFrame(commit_data),
                "pr_data": pd.DataFrame(pr_data),
                "issue_data": pd.DataFrame(issue_data)
            }
        
        except Exception as e:
            print(f"Error fetching repository data: {e}")
            return None
