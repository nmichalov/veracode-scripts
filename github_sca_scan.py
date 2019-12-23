#!/usr/bin/env python3
# A simple script for iterating through and scanning all repos with sourceclear
# run python3 github_sca_scan.py `github_username` 'oauth_token'
# machine must have an active srcclr agent since it just invokes a command line call

import requests, os, sys

def main():
    authorization_header = {"Authorization": f'token {sys.argv[2]}'}
    # use the below request to scan by username
    #r = requests.get(f'https://api.github.com/users/{sys.argv[1]}/repos', headers=authorization_header) 
    # use the below request to scan by organization
    r = requests.get(f'https://api.github.com/orgs/{sys.argv[1]}/repos', headers=authorization_header) 
    raw_data = r.json()             
    for repo in raw_data:           
        url = repo['html_url']      
        print(f'scanning {url}')    
        try:                        
            os.system(f'srcclr scan --url {url}') 
            print(f'successfully scanned {url}')  
        except:                             
            print(f'failed to scan {url}')  
    
if __name__ == '__main__':  
    main()