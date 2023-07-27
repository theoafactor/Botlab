from engine.responses import answers

class Bot:
    def __init__(self):
        pass

    def ask(self, question):
        for answer in answers:
            if question in answer:
                print(answer[question])
                break
        
        else:
            print("I dont understand your question")
            
        

 