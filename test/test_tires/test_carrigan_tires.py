import unittest

from tires.carrigan_tires import CarriganTires 


class testCarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.4, 0.89, 0.7, 0.9]
        tires = CarriganTires(tire_wear)

        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.3, 0.3, 0.2, 0.89]
        tires = CarriganTires(tire_wear)

        self.assertFalse(tires.needs_service())
