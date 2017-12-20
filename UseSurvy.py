import Survey  

question='你的首选开发语言'
my_survey=Survey.AnonymousSurvey(question)

my_survey.show_question()
print('Ente q to quit')

while True:
  respose=input("语言:")
  if respose=='q':
     break
  my_survey.store_question(respose)

print("感谢参与")
my_survey.showResult()


