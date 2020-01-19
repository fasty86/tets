class Survey_simple:
    """" Simple pool """

    def __init__(self, question):
        self.question = question
        self.response = []

    def get_question(self):
        print(f'{self.question}')

    def set_response(self, response):
        self.response.append(response)

    def show_results(self):
        print("Survey results:")
        for response in self.response:
            print(f'- {response}')




