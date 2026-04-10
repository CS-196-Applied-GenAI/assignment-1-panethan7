import unittest
from currency_converter import CurrencyConverter

class TestCurrencyConverter(unittest.TestCase):
    
    def setUp(self):
        self.converter = CurrencyConverter()
    
    def test_conversion_to_usd(self):
        self.assertEqual(self.converter.convert_to_usd(100, "EUR"), 110)  
    
    def test_conversion_from_usd(self):
        self.assertEqual(self.converter.convert_from_usd(100, "GBP"), 76.92)  
    def test_invalid_currency_conversion(self):
        self.assertEqual(self.converter.convert_to_usd(100, "XYZ"), "Error: Invalid currency")
    
    def test_get_rate(self):
        self.assertEqual(self.converter.get_rate("JPY"), 0.008)  
    def test_add_currency(self):
        self.converter.add_currency("INR", 0.012)
        self.assertEqual(self.converter.get_rate("INR"), 0.012)  
    
    def test_remove_currency(self):
        self.converter.remove_currency("EUR")
        self.assertEqual(self.converter.get_rate("EUR"), None) 
    
    def test_update_rate(self):
        self.converter.update_rate("GBP", 1.4)
        self.assertEqual(self.converter.get_rate("GBP"), 1.4)  
    
    def test_convert_list_to_usd(self):
        self.assertEqual(self.converter.convert_list_to_usd([50, 75], ["CAD", "AUD"]), 80.25)  
    
    def test_batch_convert(self):
        result = self.converter.batch_convert([{ "amount": 20, "currency": "EUR"}, { "amount": 50, "currency": "GBP"}])
        self.assertEqual(result, [22.0, 65.0])  
    
    def test_convert_and_check_threshold_above(self):
        self.assertEqual(self.converter.convert_and_check_threshold(200, "GBP", 250), "Above threshold")
    
    def test_convert_and_check_threshold_below(self):
        self.assertEqual(self.converter.convert_and_check_threshold(10, "JPY", 20), "Below threshold")
    
    def test_unreachable_code(self):
        self.assertNotEqual(self.converter.convert_and_check_threshold(100, "EUR", 500), "Unreachable code")
    
    def test_broken_function(self):
        self.assertEqual(self.converter.convert_and_check_threshold(100, "CAD", 75), "Below threshold")
    
    def test_broken_function_logic(self):
        self.assertEqual(self.converter.convert_and_check_threshold(100, "CAD", 50), "Above threshold")
    
    def test_broken_function_prime(self):
        self.assertTrue(self.converter.get_rate("GBP") > 1.2) 
    
if __name__ == "__main__":
    unittest.main()