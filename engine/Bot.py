from engine.responses import answers

class Bot:
    def __init__(self):
        pass

    def ask(self, question_asked):
        question_asked = question_asked.lower()
        for answer in answers:
            #print(answer)
            for key,values in answer.items():
                if question_asked in values:
                    print(key)
                    break
            else:
                print("I dont understand your question")
        
            
        

 