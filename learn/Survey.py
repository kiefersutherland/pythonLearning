class AnonymousSurvey():
   def __init__(self, question):
       self.question=question
       self.responses=[]

 
   def show_question(self):
        print(self.question)

   def store_question(self, newresponse):
       self.responses.append(newresponse)
   
   def showResult(self):
       print('调查结果')
       for respose in self.responses:
         print('-'+respose)