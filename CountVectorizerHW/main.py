from collections import defaultdict


class CountVectorizer:
    """Хранит матрицу соответствия слов частоте их употребления в строках из данного на вход списка"""

    def __init__(self):
        """Конструктор: создаёт матрицу"""
        self.matrix = defaultdict(lambda: defaultdict(lambda: 0))

    def get_feature_names(self) -> list:
        """Возвращает все слова из словаря в порядке их обнаружения в изначальном списке строк"""
        return list(self.matrix.keys())

    def fit_transform(self, corpus: list) -> list:
        """Принимает список строк и возвращает соответствующую терм-документную матрицу"""
        self.matrix.clear()
        for number, document in enumerate(corpus):
            document = document.lower()
            for word in document.split():
                self.matrix[word][number] += 1

        return [[self.matrix[word][number] for word in self.matrix.keys()] for number in range(len(corpus))]


def main():
    """Здесь тестируется созданный класс"""
    corpus1 = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    corpus2 = [
        'Каждый охотник желает знать где сидит фазан',
        'Каждый фазан желает знать где сидит охотник',
        'Где',
        'Не каждый охотник фазан'
    ]
    vectorizer = CountVectorizer()
    assert vectorizer.fit_transform(corpus1) == [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                                                 [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]
    assert vectorizer.get_feature_names() == ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
                                              'fresh', 'ingredients', 'parmesan', 'to', 'taste']
    assert vectorizer.fit_transform(corpus2) == [[1, 1, 1, 1, 1, 1, 1, 0],
                                                 [1, 1, 1, 1, 1, 1, 1, 0],
                                                 [0, 0, 0, 0, 1, 0, 0, 0],
                                                 [1, 1, 0, 0, 0, 0, 1, 1]]
    assert vectorizer.get_feature_names() == ['каждый', 'охотник', 'желает', 'знать', 'где', 'сидит', 'фазан', 'не']
    print('Всё работает')


if __name__ == '__main__':
    main()
