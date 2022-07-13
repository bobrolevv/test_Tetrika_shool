tests = [
    {'data':
        { 'lesson': [1, 30],
            'pupil': [2, 6, 8, 10, 15, 20],
            'tutor': [1, 7, 8, 18]},
            'answer': 9
    },
    {'data':
        { 'lesson': [1594663200, 1594666800],
            'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
            'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
            'answer': 3117
    },
    {'data':
         {'lesson': [1594702800, 1594706400],
           'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
           'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
        'answer': 3577
    },
    {'data':
         {'lesson': [1594692000, 1594695600],
           'pupil': [1594692033, 1594696347],
           'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

def appearance(intervals):
    result = []
    answer = 0

    len_pupil = len(intervals['pupil'])
    len_tutor = len(intervals['tutor'])

    start_c = intervals['tutor'][0]
    end_c = intervals['tutor'][1]

    # обход списка учеников
    for a in range(1, len_pupil, 2):
        start_a = intervals['pupil'][a - 1]
        end_a = intervals['pupil'][a]

        # обход списка преподов
        for b in range(1, len_tutor, 2):
            start_b = intervals['tutor'][b - 1]
            end_b = intervals['tutor'][b]

            # проверка на персечение
            if (
                        start_a < end_b and end_a > start_b
                    # and start_a < end_c and end_a > start_c
                    # and start_c < end_b and end_c > start_b
            ):

                # ищем начало пересечения
                if start_a > start_b: result.append(start_a)
                else: result.append(start_b)

                # ищем конец пересечения
                if end_a > end_b: result.append(end_b)
                else: result.append(end_a)

    # подсчет суммарного времени
    for r in range(1, len(result), 2):
        answer = answer + (result[r] - result[r-1])

    return answer


if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
