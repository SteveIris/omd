import math
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


def tf_transform(count_matrix: list) -> list:
    """Принимает терм-документную матрицу и возвращает матрицу повторений"""
    sums = [sum(document) for document in count_matrix]
    tf_matrix = [[round(i/total, 3) for i in document] for document, total in zip(count_matrix, sums)]
    return tf_matrix


def idf_transform(count_matrix: list) -> list:
    """Принимает терм-документную матрицу и возвращает матрицу обратных частот"""
    total_docs = len(count_matrix)
    transposed_matrix = list(map(list, zip(*count_matrix)))
    docs_with_word = [sum(map(bool, word)) for word in transposed_matrix]
    return [round(1+math.log((total_docs+1)/(amount+1)), 1) for amount in docs_with_word]


class TfidfTransformer:

    def __init__(self):
        """Инициализирует пустые матрицы"""
        self.tf_matrix = []
        self.idf_matrix = []

    def fit_transform(self, count_matrix: list) -> list:
        """Принимает терм-документную матрицу и возвращает матрицу tf-idf"""
        self.tf_matrix = tf_transform(count_matrix)
        self.idf_matrix = idf_transform(count_matrix)
        return [[round(a*b, 3) for a, b in zip(tf_doc, self.idf_matrix)] for tf_doc in self.tf_matrix]


class TfidfVectorizer(CountVectorizer):

    def __init__(self):
        """Инициализирует родительский класс и экземпляр Transsformer"""
        super().__init__()
        self.transformer = TfidfTransformer()

    def fit_transform(self, corpus: list) -> list:
        """Принимает список строк и возвращает соответствующую tf-idf матрицу"""
        return self.transformer.fit_transform(super().fit_transform(corpus))


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
    transformer = TfidfTransformer()
    tf_idf_vectorizer = TfidfVectorizer()
    count_matrix = [
        [1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    ]
    assert vectorizer.fit_transform(corpus1) == count_matrix
    assert vectorizer.get_feature_names() == ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
                                              'fresh', 'ingredients', 'parmesan', 'to', 'taste']
    assert tf_transform(count_matrix) == [[0.143, 0.143, 0.286, 0.143, 0.143, 0.143, 0, 0, 0, 0, 0, 0],
                                                          [0, 0, 0.143, 0, 0, 0, 0.143, 0.143, 0.143, 0.143, 0.143, 0.143]]
    assert idf_transform(count_matrix) == [1.4, 1.4, 1.0, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4]
    assert transformer.fit_transform(count_matrix) == [[0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0, 0, 0, 0, 0, 0],
                                                       [0, 0, 0.143, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]
    assert vectorizer.fit_transform(corpus2) == [[1, 1, 1, 1, 1, 1, 1, 0],
                                                 [1, 1, 1, 1, 1, 1, 1, 0],
                                                 [0, 0, 0, 0, 1, 0, 0, 0],
                                                 [1, 1, 0, 0, 0, 0, 1, 1]]
    assert vectorizer.get_feature_names() == ['каждый', 'охотник', 'желает', 'знать', 'где', 'сидит', 'фазан', 'не']
    assert tf_idf_vectorizer.fit_transform(corpus1) == [[0.2, 0.2, 0.286, 0.2, 0.2, 0.2, 0, 0, 0, 0, 0, 0],
                                                        [0, 0, 0.143, 0, 0, 0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]
    assert tf_idf_vectorizer.get_feature_names() == ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
                                                     'fresh', 'ingredients', 'parmesan', 'to', 'taste']
    print('Всё работает')


if __name__ == '__main__':
    main()
