class Car:
    def __init__(self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand

class CarWashStation:
    def __init__(self, distance_from_city_center: int, clean_power: int, average_rating: float, count_of_ratings: int) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:

        def wash_single_car() -> int:
            car.clean_mark = self.clean_power
            return car.clean_mark

        for car in cars:
            if car.clean_mark < self.clean_power:
                wash_single_car()

        def calculate_washing_price() -> float:
            return round((car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating) / self.distance_from_city_center, 1)

        return calculate_washing_price()

    def rate_service(self, one_rate: int) -> float:
        return round((self.average_rating * self.count_of_ratings + one_rate) / (self.count_of_ratings + 1), 1)
