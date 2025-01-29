import requests

def check_license_notice(owner, repo):
    url = f'https://api.github.com/repos/{owner}/{repo}/contents/'

    response = requests.get(url)

    if response.status_code == 200:
        files = response.json()
        for file in files:
            if 'license' in file['name'].lower():
                print(f"Found LICENSE file: {file['name']}")
            if 'notice' in file['name'].lower():
                print(f"Found NOTICE file: {file['name']}")
    else:
        print("Error fetching repository contents")

# Replace with the desired GitHub owner and repo
check_license_notice('Prabhakanthgc1995', 'kanth')

