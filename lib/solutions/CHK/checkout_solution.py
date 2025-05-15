
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
        
        if sku_count_dict['A'] <3:
            total_value += sku_count_dict['A'] * 50
        else:
            a_offer_value = sku_count_dict['A'] // 3 * 130
            a_normal_value = sku_count_dict['A'] % 3 * 50
            total_value = total_value + a_normal_value + a_offer_value
        

        return total_value
    
    def get_value_for_special_offers(special_value: int, offer_amount: int, normal_value: int, amount: int) -> int:
        if amount < offer_amount:
            return amount * normal_value
        else:
            offer_value = amount // offer_amount * special_value
            normal_value = amount % offer_amount * normal_value
            return  normal_value + offer_value


        






