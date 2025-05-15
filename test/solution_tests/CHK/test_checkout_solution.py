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

    def test_checkout_with_lowercase(self):
        assert CheckoutSolution().checkout('a') == -1

    def test_checkout_with_array(self):
        assert CheckoutSolution().checkout(['a']) == -1

    def test_checkout_with_get_one_free_deal(self):
        assert CheckoutSolution().checkout('EEB') == 80

    def test_checkout_with_list_containing_string(self):
        assert CheckoutSolution().checkout(['AAAAA']) == 200

    def test_checkout_with_list_containing_string_and_list_two_special_items(self):
        assert CheckoutSolution().checkout(['EE']) == 80

    def test_checkout_with_2_fs(self):
        assert CheckoutSolution().checkout(['FF']) == 20
    
    def test_checkout_with_list_containing_string_and_3fs_one_free(self):
        assert CheckoutSolution().checkout(['FFF']) == 20

    def test_threeN_get_one_M_free(self):
        assert CheckoutSolution().checkout(['NNNM']) == 120
    
    def test_two_k_150(self):
        assert CheckoutSolution().checkout('KK') == 150