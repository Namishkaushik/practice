class question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
question_promt = [
    "Q.1) What is 84/2? \n (a) 42 \n (b) 32 \n (c) 52 \n",
    "Q.2) What is the capital of Russia \n (a) Serbia \n (b) Tel Aviv \n (c) Moscow \n"
]
questions=[
    question(question_promt[0],"a"),
    question(question_promt[1],"c")
]
def run(questions):
    score = 0
    for i in questions:
        answer=input(i.prompt)
        if answer == i.answer:
            score+=1
    print("Your score is : ",score, "/", len(questions))
run(questions)