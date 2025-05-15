from lib.solutions.CHK.checkout_solution import CheckoutSolution


class TestCheckout():
    def test_checkouts_with_just_special_prices(self):
        assert CheckoutSolution().checkout(['A', 'A', 'A','B','B']) == 175
    
    def test_checkouts_with_just_regular_prices(self):
        assert CheckoutSolution().checkout(['A','B', 'C', 'D']) == 115

    def test_checkouts_with_special_prices_and_extra(self):
        assert CheckoutSolution().checkout(['A', 'A', 'A', 'A']) == 180

