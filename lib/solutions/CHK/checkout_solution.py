
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        sku_count_dict = {
            'A': 0,
            'B': 0,
        }
        total_value = 0
        for sku in skus:
            if sku == 'C':
                total_value += 20
            elif sku == 'D':
                total_value += 15
            else:
                sku_count_dict[sku] +=1

        total_value += self.get_value_for_special_offers(130, 3, 50, sku_count_dict['A'])
        total_value+= self.get_value_for_special_offers(45, 2, 30, sku_count_dict['B'])

        return total_value
    
    def get_value_for_special_offers(self, special_value: int, offer_amount: int, normal_value: int, amount: int) -> int:
        if amount < offer_amount:
            return amount * normal_value
        else:
            offer_value = amount // offer_amount * special_value
            normal_value = amount % offer_amount * normal_value
            return  normal_value + offer_value


        







