def vote(votes: list[int]) -> int:
    # your code
    max_count = -1
    max_vote = 0
    for cur_vote in votes:
        if votes.count(cur_vote) > max_count:
            max_count = votes.count(cur_vote)
            max_vote = cur_vote
    return max_vote


documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def get_name(doc_number):
    # your code
    for current in documents:
        if current['number'] == doc_number:
            return current['name']
    return "Документ не найден"


def get_directory(doc_number):
    # your code
    for i_, current in enumerate(directories.values(), 1):
        if doc_number in current:
            return i_
    return "Полки с таким документом не найдено"


def add(document_type, number, name, shelf_number):
    # your code
    documents.append({"type": document_type, "number": number, "name": name})
    directories[str(shelf_number)] = number  # setdefault(shelf_number, number)


def discriminant(a, b, c):
    """
    функция для нахождения дискриминанта
    """
    output = b ** 2 - 4 * a * c
    # Ваш алгоритм
    # print(output)
    return output


def solution(a, b, c):
    """
    функция для нахождения корней уравнения
    """
    if discriminant(a, b, c) < 0:
        return str("корней нет")
    elif discriminant(a, b, c) == 0:
        return str(- b / (2 * a))
    else:
        roots_lst = [str((- b + (discriminant(a, b, c) ** 0.5)) / (2 * a)),
                     str((- b - (discriminant(a, b, c) ** 0.5)) / (2 * a))]
        return ' '.join(roots_lst)


if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))

    print(vote([1, 1, 1, 2, 3]))
    print(vote([1, 2, 3, 2, 2]))

    print(solution(1, 8, 15))
    print(solution(1, -13, 12))
    print(solution(-4, 28, -49))
    print(solution(1, 1, 1))
    print(solution(1, -7, 12))
