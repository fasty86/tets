from unitTest.Survey import Survey_simple

survey = Survey_simple("What is your favourite language? : ")
survey.get_question()
while True:
    response = input("If you don't want to answer, press 'q'")
    if response != 'q':
        survey.set_response(response)
    else:
        break
survey.show_results()
