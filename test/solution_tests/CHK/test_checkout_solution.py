from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_incorrect_input_returns_negative_one(self):
        assert CheckoutSolution().checkout('1') == -1
        
    def test_checkout_for_singular_item(self):
        assert CheckoutSolution().checkout('A') == 50

    def test_checkouts_with_just_special_prices(self):
        assert CheckoutSolution().checkout('AAABB') == 175
    
    def test_checkouts_with_just_regular_prices(self):
        assert CheckoutSolution().checkout('ABCD') == 115

    def test_checkouts_with_special_prices_and_extra(self):
        assert CheckoutSolution().checkout('AAAA') == 180
