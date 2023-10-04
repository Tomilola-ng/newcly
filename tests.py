from django.test import Testcase

class BigTest(TestCase):
  pass

class CustomTests(TestCase.tests):
  test_1 = "How are you?"
  print(test_1)
  
  return

