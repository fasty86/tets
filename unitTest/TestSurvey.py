import unittest
from Survey import Survey_simple


class TestSurvey(unittest.TestCase):
    """"Test unittest for class"""

    def setUp(self):
        """" Create a survey and set of responses for use in it """
        question = 'Who is the president of Russia?'
        self.my_survey = Survey_simple(question)
        self.responses = ['Medvedev', 'Putin', 'Gorbachev']

    def test_single_response(self):
        self.my_survey.set_response(self.responses[1])
        self.assertIn(self.responses[1], self.my_survey.response)

    def test_three_responses(self):

        for line in self.responses:
            self.my_survey.set_response(line)
        for res in self.responses:
            self.assertIn(res, self.my_survey.response)


if __name__ == '__main__':
    unittest.main()
