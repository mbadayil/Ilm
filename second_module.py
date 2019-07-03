from car_rent import perDayRent,revenueYoY,perDayRentwithDiscount,blueTeslaWithNotes
import unittest

class TestCar_Rent(unittest.TestCase):
    def test_perDay(self):
        car={
            "Car": [
                {
                    "make": "Audi",
                    "model": "A7",
                    "vin": "234JKSJDFJKHSDFKJHSDFK",
                    "metadata": {
                        "Color": "Black",
                        "Notes": "Scratches right on the front side of the car"
                    },
                    "perdayrent": {
                        "Price": 340,
                        "Discount": 15
                    },
                    "metrics": {
                        "yoymaintenancecost": 2190.76,
                        "depreciation": 2256.43,
                        "rentalcount": {
                            "lastweek": 4,
                            "yeartodate": 221
                        }
                    }
                },
                {
                    "make": "Tesla",
                    "model": "Hybrid",
                    "vin": "4758693013VIF897234987",
                    "metadata": {
                        "Color": "Blue",
                        "Notes": "Scratches left on the front side of the car"
                    },
                    "perdayrent": {
                        "Price": 240,
                        "Discount": 25
                    },
                    "metrics": {
                        "yoymaintenancecost": 3190.76,
                        "depreciation": 2156.43,
                        "rentalcount": {
                            "lastweek": 4,
                            "yeartodate": 211
                        }
                    }
                },
                {
                    "make": "Tesla",
                    "model": "Electric",
                    "vin": "64735NHGFH61289034SDF",
                    "metadata": {
                        "Color": "Blue",
                        "Notes": "Scratches123 on the front side of the car"
                    },
                    "perdayrent": {
                        "Price": 140,
                        "Discount": 15
                    },
                    "metrics": {
                        "yoymaintenancecost": 1190.76,
                        "depreciation": 2116.43,
                        "rentalcount": {
                            "lastweek": 4,
                            "yeartodate": 211
                        }
                    }
                },
                {
                    "make": "Tesla",
                    "model": "Hybrid",
                    "vin": "7860NMXCVBNXMKJDSKFJHEW",
                    "metadata": {
                        "Color": "RED",
                        "Notes": "Scratches7860 on the front side of the car"
                    },
                    "perdayrent": {
                        "Price": 280,
                        "Discount": 35
                    },
                    "metrics": {
                        "yoymaintenancecost": 4190.76,
                        "depreciation": 1256.43,
                        "rentalcount": {
                            "lastweek": 4,
                            "yeartodate": 201
                        }
                    }
                }
            ]
        }

        for cars in range(len(car['Car'])):
            self.assertTrue(car['Car'][cars]['make']=='Tesla' and \
            car['Car'][cars]['metadata']['Color'])=='Blue'
        #Blue=car['Car'][cars]['make']=='Tesla' and car['Car'][cars]['metadata']['Color']
        #self.assertEqual(blueTeslaWithNotes(car),Blue)

if __name__=='__main__':
    unittest.main()
