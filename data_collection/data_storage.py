import pandas as pd
import os
import xlsxwriter

class DataStorage:
    def __init__(self, filename="github_data.xlsx"):
        self.filename = filename

    def save_to_csv(self, repo_info: dict, commit_data: pd.DataFrame, pr_data: pd.DataFrame, issue_data: pd.DataFrame):
        # Convert repo_info dictionary to a DataFrame
        repo_info_df = pd.DataFrame([repo_info])
        
        # Remove timezone from all datetime columns in the dataframes
        def remove_timezone(df):
            for col in df.columns:
                if pd.api.types.is_datetime64_any_dtype(df[col]):
                    df[col] = df[col].dt.tz_localize(None)  # Remove timezone
            return df
        
        # Apply the timezone removal function to the DataFrames
        commit_data = remove_timezone(commit_data)
        pr_data = remove_timezone(pr_data)
        issue_data = remove_timezone(issue_data)
        repo_info_df = remove_timezone(repo_info_df)
        
        # Create an Excel writer object to save data into different sheets
        with pd.ExcelWriter(self.filename, engine='xlsxwriter') as writer:
            # Save repo_info, commit_data, pr_data, and issue_data to respective sheets
            repo_info_df.to_excel(writer, sheet_name='Repo Info', index=False)
            commit_data.to_excel(writer, sheet_name='Commits', index=False)
            pr_data.to_excel(writer, sheet_name='Pull Requests', index=False)
            issue_data.to_excel(writer, sheet_name='Issues', index=False)

        print(f"Data saved to {self.filename} successfully.")
        return self.filename  # Return the filename for download

    def get_csv_data(self):
        # Read the Excel content into a byte-like object for downloading
        with open(self.filename, "rb") as file:
            return file.read()
