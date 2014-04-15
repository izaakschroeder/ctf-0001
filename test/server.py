import unittest, webtest, app

class TestServer(unittest.TestCase):

	def setUp(self):
		self.app = app.app()
		self.server = webtest.TestApplication(self.app)

	def sign(self):
		response = self.server.post('/sign', 'print("Hello")')
		assert response.status_int == 200
		assert 'form' in response

	def executeSigned(self):
		program = self.server.post('/sign', 'print("Hello")').body
		response = self.server.post('/execute', program)
		assert response.status_int == 200
		assert 'Hello' in response

	def executeUnsigned(self):
		response = self.server.post('/execute', 'print("Hello")')
		assert response.status_int == 400

if __name__ == '__main__':
	unittest.main()