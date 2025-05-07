# Tour distance class using Google Maps Distance Matrix API

import urllib.request

class Tour:
    def __init__(self, *cities):
        self.cities = list(cities)

    def __str__(self):
        return "; ".join(self.cities)

    def __repr__(self):
        return self.__str__()

    def distance(self, mode='driving'):
        total = 0
        base_url = "http://maps.googleapis.com/maps/api/distancematrix/json?"
        for i in range(len(self.cities) - 1):
            origin = self.cities[i].replace(" ", "+")
            dest = self.cities[i + 1].replace(" ", "+")
            url = f"{base_url}origins={origin}&destinations={dest}&mode={mode}&sensor=false"

            try:
                web_obj = urllib.request.urlopen(url)
                result_str = str(web_obj.read())
                web_obj.close()

                start = result_str.find('"distance"')
                if start == -1:
                    raise ValueError("No distance returned from API")

                value_index = result_str.find('"value"', start)
                colon_index = result_str.find(":", value_index)
                comma_index = result_str.find(",", colon_index)
                meters = int(result_str[colon_index + 1:comma_index].strip())
                total += meters
            except Exception:
                raise ValueError("Failed to retrieve distance between cities.")
        return total

    def __add__(self, other):
        return Tour(*(self.cities + other.cities))

    def __mul__(self, times):
        if not isinstance(times, int):
            raise TypeError("Multiplier must be an integer.")
        if times < 0:
            raise ValueError("Multiplier must be non-negative.")
        return Tour(*(self.cities * times))

    def __rmul__(self, times):
        return self.__mul__(times)

    def __eq__(self, other):
        return self.cities == other.cities

    def __gt__(self, other):
        return self.distance() > other.distance()

    def __lt__(self, other):
        return self.distance() < other.distance()

def main():
    t1 = Tour("New York, NY", "Lansing, MI", "Sacramento, CA")
    t2 = Tour("Oakland, CA")
    t3 = Tour("Sacramento, CA", "Oakland, CA")

    print("t1: {}t2:{}t3:{}".format(t1, t2, t3))
    print("t1 distances: driving-{} km; biking-{} km; walking-{} km".format(
        round(t1.distance() / 1000), 
        round(t1.distance('bicycling') / 1000), 
        round(t1.distance('walking') / 1000)
    ))

    print("\nUsing driving distances from here on.")
    t4 = t1 + t2
    print("t4:", t4)
    print("t4 driving distance:", round(t4.distance() / 1000), "km")
    print("t4 == t1 + t2:", t4 == (t1 + t2))
    print("t1 * 2:", t1 * 2)
    print("2 * t2:", 2 * t2)
    print("t1 > t3:", t1 > t3)
    print("t1 < t3:", t1 < t3)

if __name__ == "__main__":
    main()
