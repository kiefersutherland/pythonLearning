import unittest
import Survey

class TestAnonymousSurvey(unittest.TestCase):
    def setup(self):
         question='你的首选目的地'
         self.my_survey=Survey.AnonymousSurvey(question)
         self.responses=['上海','神户','东京']

    def test_stroe_Single(self):
        self.my_survey.store_question(self.responses[0])
        self.assertIn(self.responses[0],self.mysurvy.responses)  


 
unittest.main()