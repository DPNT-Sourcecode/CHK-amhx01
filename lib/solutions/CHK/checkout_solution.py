
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
            
            


        



