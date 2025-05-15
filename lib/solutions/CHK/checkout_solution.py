
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
        
        if sku_count_dict['B'] < 2:
            total_value += sku_count_dict['B'] * 30
        else:
            b_offer_value = sku_count_dict['A'] // 3 * 45
            b_normal_value = sku_count_dict['A'] % 2 * 30
            total_value = total_value + b_normal_value + b_offer_value

        return total_value
            


        





