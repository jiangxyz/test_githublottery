#!/usr/bin/env python
# coding: utf-8

from github import Github
import random

repository = "jiangxyz/test_githublottery"
github_username = "jiangxyz"
github_password = ""
N = 1

def get_lucky_dogs():
    # First create a Github instance
    # g = Github()
    # Or you can use your GitHub username and password
    g = Github(github_username, github_password)

    # Get a repo by repo-name
    repo = g.get_repo(repository)

    # Now list the users
    stared_users = []
    for user in repo.get_stargazers():
        stared_users.append(user)
    # 返回所有star用户的username的列表
    return stared_users


if __name__ == "__main__":
    print("Running...")
    stared_users = get_lucky_dogs()
    print("Found {} ".format(stared_users))
    print("{} stared users in total.".format(len(stared_users)))

    print("\n\n--- Congratulations!!! --- \n\n")
    alist = random.sample(range(0, len(stared_users)), N) # sample 用于无重复的随机抽样
    [print("{} ({})".format(stared_users[i].login, stared_users[i].email)) for i in alist]





