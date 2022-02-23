# -*- coding: utf-8 -*-
import unittest

from main import getRepos, getCommits


class TestAPI(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testGetRepos(self):
        repos = getRepos()
        self.assertGreater(len(repos), 0, "Trouble getting repos, length is 0")

    def testGetCommits(self):
        repos = getRepos()
        reposInAccount = repos
        repoCommitDict = getCommits(reposInAccount)
        self.assertGreater(len(repoCommitDict), 0, "Trouble commits")


if __name__ == "__main__":
    print("Running unit tests")
    unittest.main()
