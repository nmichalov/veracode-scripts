#!/usr/bin/env python3
# A simple script for iterating through and scanning all repos with sourceclear
# run python3 github_sca_scan.py `github_username`
# machine must have an active srcclr agent since it just invokes a command line call

import requests, os, sys

def main():
    # use the below request to scan by username
    r = requests.get(f'https://api.github.com/users/{sys.argv[1]}/repos')   # request a list of user's repos from the github API
    # use the below request to scan by organization
    # r = requests.get(f'https://api.github.com/orgs/{sys.argv[1]}/repos')
    raw_data = r.json()             # extract JSON containing repo data from the request reciev
    for repo in raw_data:           # loop through the JSON
        url = repo['html_url']      # get the html url for each of the repos
        print(f'scanning {url}')    # print repo url to the command line so we know what we're scanning
        try:                        # try to scan
            os.system(f'srcclr scan --url {url}') # runs the srcclr agent from the command line
            print(f'successfully scanned {url}')  # print a notification that we successfully scanned the repo to the command line
        except:                             # if the scan fails for some reason
            print(f'failed to scan {url}')  # print which repo failed
    
if __name__ == '__main__':   # this is needed so that the code can be run from the CLI
    main()