import requests

response = requests.get('https://api.github.com')
print(f"Статус відповіді GitHub API: {response.status_code}")