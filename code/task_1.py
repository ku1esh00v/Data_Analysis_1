#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

if __name__ == "__main__":
    with open('for_task_1.txt', 'r', encoding='utf-8') as file:
        content = file.read().splitlines()

    sentences_one_letter = []
    other_sentences = []

    for sentence in content:
        words = sentence.split()

        if len(words) > 0:
            if len(words[0]) == 1:
                sentences_one_letter.append(sentence)
            else:
                other_sentences.append(sentence)

    print("Предложения, начинающиеся с одной буквы:")
    for sentence in sentences_one_letter:
        print(sentence)

    print("\nОстальные предложения:")
    for sentence in other_sentences:
        print(sentence)
