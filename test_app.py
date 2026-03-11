import sys
import requests
from bs4 import BeautifulSoup

BASE_URL = 'http://127.0.0.1:5000'
session = requests.Session()

def get_csrf(html):
    soup = BeautifulSoup(html, 'html.parser')
    token = soup.find('input', {'name': 'csrf_token'})
    return token['value'] if token else None

def test_app():
    # 1. Create Task
    print("1. Creating a new task without auth...")
    res = session.get(f'{BASE_URL}/task/new')
    csrf_token = get_csrf(res.text)
    data = {
        'csrf_token': csrf_token,
        'title': 'My Automated Task',
        'description': 'This is a test task without login.',
        'due_date': '2026-12-31',
        'status': 'Pending',
        'remarks': 'Test remarks.',
        'user_name': 'Amresh Admin',
        'user_id': '101',
        'submit': 'Save Task'
    }
    res = session.post(f'{BASE_URL}/task/new', data=data)
    
    # 2. Verify Task on Index
    print("2. Verifying task on index page...")
    res = session.get(f'{BASE_URL}/')
    if 'My Automated Task' in res.text and 'Amresh Admin' in res.text:
        print("Success: Task found on the index page! Application flow verified.")
    else:
        print("Failed: Task not found on the index page.")
        print(f"Status Code: {res.status_code}")
        print("Response body snippet: ")
        print(res.text[:1000])
        sys.exit(1)

if __name__ == '__main__':
    try:
        test_app()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
