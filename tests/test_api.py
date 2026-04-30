import unittest
from app import create_app, db

class APITestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    # Test 1: Home route
    def test_home(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    # Test 2: Register
    def test_register(self):
        res = self.client.post('/register', json={
            "username": "user1",
            "password": "1234"
        })
        self.assertEqual(res.status_code, 200)

    # Test 3: Login
    def test_login(self):
        self.client.post('/register', json={
            "username": "user1",
            "password": "1234"
        })

        res = self.client.post('/login', json={
            "username": "user1",
            "password": "1234"
        })

        self.assertEqual(res.status_code, 200)

    # Test 4: Add Task (with token)
    def test_add_task(self):
        self.client.post('/register', json={
            "username": "user1",
            "password": "1234"
        })

        login = self.client.post('/login', json={
            "username": "user1",
            "password": "1234"
        })

        token = login.get_json()['token']

        res = self.client.post(
            '/add',
            json={"title": "Test Task"},
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(res.status_code, 201)

    # Test 5: Get Tasks
    def test_get_tasks(self):
        self.client.post('/register', json={
            "username": "user1",
            "password": "1234"
        })

        login = self.client.post('/login', json={
            "username": "user1",
            "password": "1234"
        })

        token = login.get_json()['token']

        self.client.post(
            '/add',
            json={"title": "Test Task"},
            headers={"Authorization": f"Bearer {token}"}
        )

        res = self.client.get(
            '/tasks',
            headers={"Authorization": f"Bearer {token}"}
        )

        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()