tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена','Станислав','Алексей','Антон','Алла','Марсель']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

def check_gen(tutors: list, klasses: list):
    for i in range (len(tutors)):
        if i<len(klasses):
            pair=(tutors[i],klasses[i])
            yield pair
        else:
            yield (tutors[i],None)


generator = check_gen(tutors, klasses)
# добавьте здесь доказательство, что создали именно генератор
print("Тип функции:",type(generator))
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
