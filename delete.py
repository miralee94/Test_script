from github import Github
import argparse

def parse_args():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description='Create a new private repository on GitHub')
    parser.add_argument('repo', type=str, help='Name of the repository')
    return parser.parse_args()

#Reads GitHub access token from a config file
def get_github_token():
    with open('config.txt', 'r') as f:
        token = f.read().strip()
    return token

def delete(repo, token):
    g = Github(token)
    g.get_user().get_repo(repo).delete()

def main():
    args = parse_args()
    token = get_github_token()
    delete(args.repo, token)

if __name__ == '__main__':
    main()