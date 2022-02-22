import requests
import json

urlRoot = "https://api.github.com"
userId = "frankied003"

reposInAccount = []


def getRepos():
    endpoint = "/users/" + userId + "/repos"
    url = urlRoot + endpoint
    headers = {"User-Agent": "Frankie-is-cool", "content-type": "application/json"}
    response = requests.get(url, headers=headers)
    data = response.json()
    for repo in data:
        name = repo.get("name")
        reposInAccount.append(name)


def getCommits(repos):
    for repo in repos:
        endpoint = "/repos/" + userId + "/" + repo + "/commits"
        url = urlRoot + endpoint
        headers = {"User-Agent": "Frankie-is-cool", "content-type": "application/json"}
        response = requests.get(url, headers=headers)
        data = response.json()
        commitCount = 0
        for commit in data:
            commitCount += 1
        print("Repo: " + repo + " Number of commits: " + str(commitCount))


if __name__ == "__main__":
    getRepos()
    getCommits(reposInAccount)
