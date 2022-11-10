import random

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


def lesson_11():
    word = word_list_11.keys()
    rd_word = random.sample(word, 3)
    meaning = []
    for i in range(3):
        mean = word_list_11[rd_word[i]]
        meaning.append(mean)
    return rd_word, meaning


print(lesson_11())
