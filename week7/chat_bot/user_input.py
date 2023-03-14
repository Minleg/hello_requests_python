def ask_questions(question):
    while True:
        answer = input(question + ' ')
        if not answer:
            print('Please enter your answer.')
        else:
            break
    return answer