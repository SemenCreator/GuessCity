import requests

import sys
import random

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
from interface_guess_city import Ui_MainWindow

from cities_coordinates import cities_coordinates

# Картинки только со спутника, потому что в обыбном формате
# на карте появляются опознавательные надписи на определенном языке


class ChooseCity(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
        self.cities_coordinates = cities_coordinates
        self.buttons = [self.choice_1, self.choice_2,
                        self.choice_3, self.choice_4]
        for button in self.buttons:
            button.setStyleSheet('background-color: rgb(220,220,220);')
        self.next_town.clicked.connect(self.switching_town)
        self.right_city = ''
        self.counter_city = 0
        self.guessed = False
        self.four_cities = []
        self.random_city()

    def switching_town(self):
        if self.guessed:
            for button in self.buttons:
                button.setStyleSheet('background-color: rgb(220,220,220);')
            self.guessed = False
            self.random_city()

    def random_city(self):
        self.right_city = random.sample(
            list(self.cities_coordinates.keys()), 1)[0]
        self.request_for_city()
        self.variants_cities()
        self.change_buttons_name()

    def request_for_city(self):
        geocoder_params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": self.right_city,
            "format": "json"}
        response = requests.get(
            self.geocoder_api_server, params=geocoder_params)

        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        toponym_coodrinates = toponym["Point"]["pos"]
        toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

        delta = "0.02"

        map_params = {
            "ll": ",".join([toponym_longitude, toponym_lattitude]),
            "spn": ",".join([delta, delta]),
            "l": "sat"
        }

        map_api_server = "http://static-maps.yandex.ru/1.x/"
        self.response = requests.get(map_api_server, params=map_params)
        self.map_file = "map.png"
        if self.counter_city > 0:
            with open(self.map_file, "wb") as f:
                f.write(self.response.content)
            self.pixmap = QPixmap(self.map_file)
            self.image.setPixmap(self.pixmap)
        else:
            self.new_image()

    def new_image(self):
        with open(self.map_file, "wb") as f:
            f.write(self.response.content)

        self.pixmap = QPixmap(self.map_file)
        self.image = QLabel(self)
        self.image.move(100, 10)
        self.image.resize(600, 300)
        self.image.setPixmap(self.pixmap)
        self.counter_city += 1

    def variants_cities(self):
        self.variants_of_cities = list(self.cities_coordinates.keys())
        self.variants_of_cities.remove(self.right_city)
        self.four_cities = [self.right_city] + random.sample(
            list(self.variants_of_cities), 3)

    def change_buttons_name(self):
        index = 0
        random.shuffle(self.four_cities)
        for button in self.buttons:
            button.clicked.connect(self.choose_right_players)
            button.setText(self.four_cities[index])
            index += 1

    def choose_right_players(self):
        sender = self.sender()
        for button in self.buttons:
            if button == sender:
                if button.text() == self.right_city:
                    button.setStyleSheet('background-color: rgb(0, 255, 0);')
                    self.guessed = True
                    for button in self.buttons:
                        if button.text() != self.right_city:
                            button.setStyleSheet(
                                'background-color: rgb(255, 0, 0);')
                    break
                else:
                    button.setStyleSheet('background-color: rgb(255, 0, 0);')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ChooseCity()
    ex.show()
    sys.exit(app.exec_())
