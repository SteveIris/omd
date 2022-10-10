from collections import defaultdict


class CountVectorizer:
    """Хранит матрицу соответствия слов частоте их употребления в строках из данного на вход списка"""

    def __init__(self):
        """Конструктор: создаёт матрицу"""
        self.matrix = defaultdict(lambda: defaultdict(lambda: 0))

    def get_feature_names(self) -> list:
        """Возвращает все слова из словаря в порядке их обнаружения в изначальном списке строк"""
        return list(self.matrix.keys())

    def fit_transform(self, iterable) -> list:
        """Принимает список строк и возвращает соответствующую терм-документную матрицу"""
        self.matrix.clear()
        for number, document in enumerate(iterable):
            document = document.lower()
            for word in document.split():
                self.matrix[word][number] += 1

        return [[self.matrix[word][number] for word in self.matrix.keys()] for number in range(len(iterable))]


def main():
    """Здесь тестируется созданный класс"""
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)


if __name__ == '__main__':
    main()
