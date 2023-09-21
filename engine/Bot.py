from engine.responses import answers

class Bot:
    def __init__(self):
        pass

    def ask(self, question_asked):
        question_asked = question_asked.lower()

        is_answer_found = False
        for answer in answers:
            for key,values in answer.items():
                if question_asked in values["questions"]:
                    is_answer_found = True
                    secondary_answers = values["secondary_answers"]
                    secondary_answers.append(key)
                    import random
                    index = random.randrange(0, len(secondary_answers))
                    return {
                        "answer": secondary_answers[index],
                        "category": values["category"]
                    }
            
        if not is_answer_found:
           return "I dont understand your question"

        
            
        

 