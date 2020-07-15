import unittest
from chap11.survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Tests the class AnonymousSurvey"""
    def test_store_single_response(self):
        """Test if single response is stored properly"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn("English", my_survey.responses)

    def test_store_three_responses(self):
        """Tests that indivudual responses are stored properly with AnonymousSurvey"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Greek']
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)
if __name__ == "__main__":
        unittest.main()