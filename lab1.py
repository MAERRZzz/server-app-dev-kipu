class Abiturient:
    def __init__(self, a_id, last_name, first_name, middle_name, address, phone, marks):
        self.a_id = a_id
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.address = address
        self.phone = phone
        self.marks = marks

    def __str__(self):
        return f'Абитуриент №{self.a_id}: {self.last_name} {self.first_name} {self.middle_name}'

    def __hash__(self):
        return hash((self.a_id, self.last_name, self.first_name, self.middle_name))

    @staticmethod
    def create_abiturients():
        abiturients = [
            Abiturient(1, 'Иванов', "Иван", "Иванович", "г. Симферополь", "+79788284321", [4, 4, 5]),
            Abiturient(2, 'Петров', "Петр", "Петрович", "г. Симферополь", "+79788284321", [4, 2, 4]),
            Abiturient(3, 'Кузнецов', "Кузнец", "Кузнецович", "г. Симферополь", "+79788284321", [2, 4, 3])
        ]
        return abiturients

    @staticmethod
    def abiturients_with_bad_marks(a_list: list):
        bad_marks = []
        for a in a_list:
            if 2 in a.marks:
                bad_marks.append(f'  - {a.last_name} {a.first_name}')
        print('1) Абитуриенты с неуд. оценками:')
        print(*bad_marks, sep='\n')

    @staticmethod
    def marks_sum_gt(a_list: list, mark_sum: int):
        marks_sum_gt = []
        for a in a_list:
            if sum(a.marks) > mark_sum:
                marks_sum_gt.append(f'  - {a.last_name} {a.first_name} ({sum(a.marks)})')
        print(f'2) Абитуриенты с суммой оценок больше {mark_sum}:')
        print(*marks_sum_gt, sep='\n')

    @staticmethod
    def abiturients_with_high_marks(a_list: list, a_count: int):
        high_marks = []
        a_list.sort(key=lambda x: sum(x.marks), reverse=True)
        for a in a_list[: a_count]:
            high_marks.append(f'  - {a.last_name} {a.first_name} ({sum(a.marks)})')
        print(f'3) Абитуриенты с максимальной суммой оценок:')
        print(*high_marks, sep='\n')


all_abiturients = Abiturient.create_abiturients()
Abiturient.abiturients_with_bad_marks(all_abiturients)
print()
Abiturient.marks_sum_gt(all_abiturients, 9)
print()
Abiturient.abiturients_with_high_marks(all_abiturients, 3)
