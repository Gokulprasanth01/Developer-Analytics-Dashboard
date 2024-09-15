class NLPQueryProcessor:
    def __init__(self):
        # Define keywords for each metric or visualization
        self.keywords = {
            "commit_frequency": ["commit", "frequency", "commits"],
            "pr_merge_rate": ["pull request", "pr", "merge rate", "merged"],
            "issue_resolution_time": ["issue", "resolution", "time", "closed issues"],
            "repo_info": ["repository", "info", "stars", "forks", "watchers"]
        }

    def process_query(self, query: str):
        # Normalize the query to lower case
        query = query.lower()

        # Check if the query matches any of the known keywords
        if any(word in query for word in self.keywords['commit_frequency']):
            return "commit_frequency"
        elif any(word in query for word in self.keywords['pr_merge_rate']):
            return "pr_merge_rate"
        elif any(word in query for word in self.keywords['issue_resolution_time']):
            return "issue_resolution_time"
        elif any(word in query for word in self.keywords['repo_info']):
            return "repo_info"
        else:
            return "unknown"

