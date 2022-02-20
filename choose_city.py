import requests


class ChooseCity:
    def __init__(self):
        self.apikey = '40d1649f-0493-4b70-98ba-98533de7710b'
        self.server_address = 'http://geocode-maps.yandex.ru/1.x/'

        self.cities = 'Москва, Нью-Йорк, Лондон, Венеция, Ванкувер, Барселона, Кейптаун, \
Сан-Франциско, Сидней, Рим, Сингапур, Лиссабон, Амстердам, Прага, \
Рио-де-Жанейро, Будапешт, Стамбул, Токио, Вена, Буэнос-Айрес, Торонто, \
Сан-Диего, Квебек, Гонконг, Чикаго, Брюгге, Мадрид, Гавана, Дубай, \
Иерусалим, Эдинбург, Кито, Цюрих, Куско, Санкт-Петербург, Берлин, Ханой, \
Куинстаун, Сан-Мигель-де-Альенде, Сеул, Дубровник, \
Сан-Себастьян, Бангкок'.split(", ")

        self.cities_coordinates = {}
        self.identification_city()
        print(self.cities_coordinates)

    def identification_city(self):
        for city in self.cities:
            geocoder_request = f"{self.server_address}?apikey={self.apikey}&geocode={city}1&format=json"
            response = requests.get(geocoder_request)
            if response:
                json_response = response.json()
                toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
                toponym_coodrinates = toponym["Point"]["pos"].split(' ')
                self.cities_coordinates[city] = toponym_coodrinates
            else:
                print("Ошибка выполнения запроса:")
                print(geocoder_request)
                print("Http статус:", response.status_code,
                      "(", response.reason, ")")


ChooseCity()
