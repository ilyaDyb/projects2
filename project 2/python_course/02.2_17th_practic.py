def ask_user():
    ask_answer = {
        "как дела?": 'хорошо!',
        "что делаешь?": "программирую"
    }
    while True:
        a = input()
        if a in ask_answer:
            print(ask_answer[a])
            break


ask_user()