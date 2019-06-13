"""Unit test for api module GraphQL queries."""
import requests
import unittest


class TestApi(unittest.TestCase):
    """Class to execute unit tests for api.py."""

    @classmethod
    def setUpClass(self):
        """Set up function called when class is consructed."""
        self.base_url = 'http://127.0.0.1:5000/graphql'
        self.headers = {'content-type': 'application/json'}

    def test_query_task(self):
        payload = '{"query":"{task(id:1){taskName}}"}'
        response = requests.post(self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['data']['task']['taskName'], 'First task for 1')

    def test_query_task_list(self):
        payload = '{"query": "{taskList{edges{node{id}}}}"}'
        response = requests.post(self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(json['data']['taskList']['edges']), 0)

    def test_query_card(self):
        payload = '{"query":"{card(id:1){cardName}}"}'
        response = requests.post(self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['data']['card']['cardName'], 'First card')

    def test_query_card_list(self):
        payload = '{"query": "{cardList{edges{node{id}}}}"}'
        response = requests.post(self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(json['data']['cardList']['edges']), 0)

    def test_create_task(self):
        # Get batch list
        payload = '{"query": "mutation{createTask(input:{taskName:\\"Test task\\", cardId:\\"Q2FyZDox=\\"}){task{taskName}, task{cardId}}}"}'
        response = requests.post(self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['data']['createTask']['task']['taskName'], 'Test task')

    def test_update_task(self):
        payload = '{"query": "mutation{updateTask(input:{id:\\"VGFzazo4=\\",taskName:\\"Fourth Task for Third Card\\"}){task{taskName}}}"}'
        response = requests.post(self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['data']['updateTask']['task']['taskName'], 'Fourth Task for Third Card')

    def test_create_card(self):
        payload = '{"query": "mutation{createCard(input:{cardName:\\"Test card\\"}){card{cardName}}}"}'
        response = requests.post(self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['data']['createCard']['card']['cardName'], 'Test card')

    def test_update_card(self):
        payload = '{"query": "mutation{updateCard(input:{id:\\"Q2FyZDo3=\\",cardName:\\"Seventh card is for Sport\\"}){card{cardName}}}"}'
        response = requests.post(self.base_url, headers=self.headers, data=payload)
        json = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json['data']['updateCard']['card']['cardName'], 'Seventh card is for Sport')

    @classmethod
    def tearDownClass(self):
        """Tear down function called when class is deconstructed."""
        pass


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestApi)
    unittest.TextTestRunner(verbosity=2).run(suite)
