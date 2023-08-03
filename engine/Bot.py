from engine.responses import answers

class Bot:
    def __init__(self):
        pass

    def ask(self, question_asked):
        question_asked = question_asked.lower()
        
        is_answer_found = False
        for answer in answers:
            #print(answer)
            for key,values in answer.items():
                if question_asked in values:
                    is_answer_found = True
                    print(key)
                    break
            
        if not is_answer_found:
           print("I dont understand your question")

        
            
        

 