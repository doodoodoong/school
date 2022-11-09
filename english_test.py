import random

word_list_10 = {
    "toy car": "장난감자동차",
    "hair band": "머리띠",
    "pencil case": "필통",
    "soccer ball": "축구공",
    "hundred": "백",
    "thousand": "천",
    "much": "많이",
    "want": "원하다",
    "will": "~할 것이다",
}

word_list_11 = {
    "get up": "일어나다",
    "go to bed": "잠자리에 들다",
    "read": "읽다",
    "ride": "타다",
    "drink": "마시다",
    "exercise": "운동하다",
    "every": "모든",
    "day": "날,하루,요일",
    "early": "일찍",
}


def lesson_10():
    word = word_list_10.keys()
    rd_word = random.sample(word, 3)
    meaning = []
    for i in range(3):
        mean = word_list_10[rd_word[i]]
        meaning.append(mean)
    return rd_word, meaning


def lesson_11():
    word = word_list_11.keys()
    rd_word = random.sample(word, 3)
    meaning = []
    for i in range(3):
        mean = word_list_11[rd_word[i]]
        meaning.append(mean)
    return rd_word, meaning


print(lesson_10())
print(lesson_11())
