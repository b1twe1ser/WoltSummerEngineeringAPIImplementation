import datetime
import math


def small_order_surcharge_fee(cart_value: int) -> int:
    if cart_value < 10_00:
        return 10_00 - cart_value

    return 0


def delivery_fee_distance(delivery_distance: int) -> int:
    if delivery_distance <= 1000:
        return 2_00

    return math.ceil(delivery_distance/500) * 100


def delivery_number_of_items(delivery_number_items: int) -> int:
    if delivery_number_items < 5:
        return 0

    number_of_additional_items = delivery_number_items - 4

    return number_of_additional_items * 50


def delivery_fee_with_time_surcharge(delivery_time: datetime, delivery_fee: int) -> int:
    if delivery_time.isoweekday() == 5 and delivery_time.hour in range(15, 20):
        return round(delivery_fee * 1.1)

    return delivery_fee


def calc_delivery_fee(cart_value: int, delivery_distance: int, number_of_items: int, time: datetime) -> float:
    if cart_value >= 100_00:
        return 0

    small_order_surcharge = small_order_surcharge_fee(cart_value)
    number_of_items_fee = delivery_number_of_items(number_of_items)
    delivery_distance_fee = delivery_fee_distance(delivery_distance)

    delivery_fee = small_order_surcharge + number_of_items_fee + delivery_distance_fee

    delivery_fee_time = delivery_fee_with_time_surcharge(time, delivery_fee)

    if delivery_fee_time >= 15_00:
        return 15_00

    return delivery_fee_time

