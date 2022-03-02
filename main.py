import requests
import json

urlRoot = "https://api.github.com"
userId = "frankied003"


def getCommits():
    reposInAccount = []
    endpoint = "/users/" + userId + "/repos"
    url = urlRoot + endpoint
    headers = {"User-Agent": "Frankie-is-cool", "content-type": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    for repo in data:
        name = repo.get("name")
        reposInAccount.append(name)

    repoCommitDict = {}
    for repo in reposInAccount:
        endpoint = "/repos/" + userId + "/" + repo + "/commits"
        url = urlRoot + endpoint
        headers = {"User-Agent": "Frankie-is-cool", "content-type": "application/json"}
        response = requests.get(url, headers=headers)
        data = response.json()
        commitCount = 0
        for commit in data:
            commitCount += 1
        print("Repo: " + repo + " Number of commits: " + str(commitCount))
        repoCommitDict[repo] = commitCount

    return repoCommitDict


if __name__ == "__main__":
    getCommits()
