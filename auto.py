import subprocess
import datetime
import random

def create_commits():
    try:
        # Change to your repository directory
        repo_path = "c:/Users/Samri/Documents/python/python"
        
        # Define the date range for the last 365 days from the current date
        end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=365)
        
        current_date = start_date
        
        while current_date <= end_date:
            # Skip committing on Sundays (day 6, where Monday is day 0)
            if current_date.weekday() == 6:  # Sunday is day 6 in the weekday() method
                current_date += datetime.timedelta(days=1)
                continue
            
            # Generate a random number of commits for the current day
            commits_count = random.randint(0, 5)  # Adjust the range as needed
            
            for _ in range(commits_count):
                # Format the current date to be used as the commit date
                commit_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
                
                # Create a new commit with the commit message "test commit"
                command = f'git commit --allow-empty --date="{commit_date}" -m "test commit"'
                subprocess.run(command, cwd=repo_path, shell=True, check=True)
            
            # Move to the next day
            current_date += datetime.timedelta(days=1)
        
        print("Random commits created for the last 365 days.")
    
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    create_commits()
