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
        count = 0

        def wash_single_car(car) -> None:
            # nonlocal count
            if car.clean_mark < self.clean_power:
                car.clean_mark = self.clean_power
                # count += 1
            return None

        def calculate_washing_price() -> float:
            return (car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating) / self.distance_from_city_center

        for car in cars:
            wash_single_car(car)
            calculate_washing_price()
            count += calculate_washing_price()

        return round(count, 1)

    def rate_service(self, one_rate: int) -> float:
        self.average_rating = round((self.average_rating * self.count_of_ratings + one_rate) / (self.count_of_ratings + 1), 1)
        self.count_of_ratings += 1
        return self.average_rating
