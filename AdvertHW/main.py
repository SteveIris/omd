import json


class ColorizeMixin:

    def colorize_text(self, color, text):
        color_str = str(color)
        return f'\033[1;{color_str};40m{text} '


class AdvertWithoutConditions:
    def __init__(self, advertisement):

        for attribute in advertisement:
            if isinstance(advertisement[attribute], dict):
                setattr(self, attribute, AdvertWithoutConditions(advertisement[attribute]))
            else:
                setattr(self, attribute, advertisement[attribute])


class Advert(ColorizeMixin, AdvertWithoutConditions):
    repr_color_code = 33

    def __init__(self, advertisement):
        AdvertWithoutConditions.__init__(self, advertisement)
        self.check_correctness()

    def check_correctness(self):
        if not hasattr(self, 'title'):
            print("Error: must have title")
            exit(0)
        if hasattr(self, 'price'):
            if self.price < 0:
                print("Error: price is negative")
                exit(0)
        else:
            self.price = 0

    def __repr__(self):
        return self.colorize_text(self.repr_color_code, f' {self.title} | {self.price} ₽')


def main():
    lesson_str = """{
    "title": "python",
    "price": 200,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
    }"""
    lesson = json.loads(lesson_str)
    lesson_ad = Advert(lesson)
    print(lesson_ad.title)
    print(lesson_ad.price)
    print(lesson_ad.location.address)
    print(lesson_ad)


if __name__ == '__main__':
    main()
