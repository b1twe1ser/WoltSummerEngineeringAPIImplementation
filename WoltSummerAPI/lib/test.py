from datetime import datetime
import unittest
import delivery_fee_calculator

friday_rush_hour = datetime.fromisoformat("2022-03-04T15:00:00+00:00")
friday_no_rush = datetime.fromisoformat("2022-03-04T14:00:00+00:00")
not_friday_rush_hour = datetime.fromisoformat("2022-03-05T15:00:00+00:00")


class TestCalculation(unittest.TestCase):

	def test_small_order_surcharge_fee(self):
		self.assertEqual(delivery_fee_calculator.small_order_surcharge_fee(8_90), 1_10)
		self.assertEqual(delivery_fee_calculator.small_order_surcharge_fee(11_00), 0)

	def test_delivery_fee_distance(self):
		self.assertEqual(2_00, delivery_fee_calculator.delivery_fee_distance(500))
		self.assertEqual(3_00, delivery_fee_calculator.delivery_fee_distance(1499))
		self.assertEqual(3_00, delivery_fee_calculator.delivery_fee_distance(1500))
		self.assertEqual(4_00, delivery_fee_calculator.delivery_fee_distance(1501))

	def test_delivery_number_of_items(self):
		self.assertEqual(0, delivery_fee_calculator.delivery_number_of_items(4))
		self.assertEqual(50, delivery_fee_calculator.delivery_number_of_items(5))
		self.assertEqual(3_00, delivery_fee_calculator.delivery_number_of_items(10))

	def test_delivery_time_surcharge(self):
		self.assertEqual(110, delivery_fee_calculator.delivery_fee_with_time_surcharge(friday_rush_hour, 100))
		self.assertEqual(100, delivery_fee_calculator.delivery_fee_with_time_surcharge(friday_no_rush, 100))
		self.assertEqual(100, delivery_fee_calculator.delivery_fee_with_time_surcharge(not_friday_rush_hour, 100))

	def test_calculate_delivery_fee(self):
		self.assertEqual(7_10, delivery_fee_calculator.calc_delivery_fee(7_90, 2235, 4, datetime.fromisoformat("2021-10-12T13:00:00+00:00")))
		self.assertEqual(0, delivery_fee_calculator.calc_delivery_fee(100_00, 2235, 4, datetime.fromisoformat("2021-10-12T13:00:00+00:00")))
		self.assertEqual(15_00, delivery_fee_calculator.calc_delivery_fee(7_90, 2235, 34, datetime.fromisoformat("2021-10-12T13:00:00+00:00")))


if __name__ == '__main__':
	unittest.main()
