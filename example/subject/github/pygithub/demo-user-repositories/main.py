#!/usr/bin/env python3

# https://pygithub.readthedocs.io/en/latest/introduction.html

from github import Github

#gh = Github("user", "password")
gh = Github()

# https://github.com/github

for repo in gh.get_user('github').get_repos():
	#print(repo.name)
	#print(repo.clone_url)
	print("git clone {url}".format(url=repo.clone_url))
