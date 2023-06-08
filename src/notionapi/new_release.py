from github import Github
import os

# using an access token
work_dir = os.getcwd()
with open("github_token.txt", mode="r") as token_file:
    g = Github(token_file.readline())

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.full_name)


print(g.get_user().get_repo("notion-api").get_latest_release().title)
