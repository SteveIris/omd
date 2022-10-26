import json
import keyword


class ColorizeMixin:
    """Миксин для раскраски текста"""

    def colorize_text(self, color, text: str):
        color_str = str(color)
        return f'\033[1;{color_str};40m{text} \033[0;0;0m'


class AdvertWithoutConditions:
    """Преобразует словарь в python-объект с доступом к атрибутам через точку. Не накладывает ограничений на данные"""
    def __init__(self, advertisement: dict):

        for attribute in advertisement:
            if keyword.iskeyword(attribute):
                attribute_not_key = attribute+'_'
            else:
                attribute_not_key = attribute
            if isinstance(advertisement[attribute], dict):
                setattr(self, attribute_not_key, AdvertWithoutConditions(advertisement[attribute]))
            else:
                setattr(self, attribute_not_key, advertisement[attribute])
        return


class Advert(ColorizeMixin, AdvertWithoutConditions):
    """Преобразует словарь в python-объект с доступом к атрибутам через точку. Требует price>=0 и наличия title"""
    repr_color_code = 33

    def __init__(self, advertisement: dict):
        self.price = 0
        AdvertWithoutConditions.__init__(self, advertisement)
        self.check_correctness()
        return

    def check_correctness(self):
        """Проверка на то, что введён title и price>=0"""
        if not hasattr(self, 'title'):
            print("Error: must have title")
            exit(0)
        if self.price < 0:
            print("Error: price is negative")
            exit(0)
        return

    def __repr__(self):
        """Выводит название и цену из объявления"""
        return self.colorize_text(Advert.repr_color_code, f' {self.title} | {self.price} ₽')


def test(test_str: str):
    """Переводит строку с объявлением в dict а затем в Advert-объект и выводит его параметры"""
    test_dict = json.loads(test_str)
    test_ad = Advert(test_dict)
    print(test_ad.title)
    print(test_ad.price)
    print(test_ad.location.address)
    print(test_ad)
    return


def main():
    lesson_str = """{
    "title": "python",
    "price": 200,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
    }"""
    test(lesson_str)
    korgi_str = """{
    "title": "Вельш-корги",
    "price": 1000,
    "class": "dogs",
    "location": {
    "address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
    }
    }"""
    test(korgi_str)

    no_price_str = """{
        "title": ":)",
        "price": -2,
        "class": "emoji",
        "location": {
        "address": "Таганрог"
        }
        }"""
    test(no_price_str)


if __name__ == '__main__':
    main()
