import time


class TrafficLight:
    __colour = {'red': 4,'yellow' : 2,'green' : 3}

    def running(self):
        for colour, period in self.__colour.items():
            print(f'{colour} {period} сек')
            time.sleep(period)


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
