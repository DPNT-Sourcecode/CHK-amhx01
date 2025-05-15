
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        sku_count_dict = {
            'A': 0,
            'B': 0,
            'C': 0,
            'D': 0
        }
        for sku in skus:
            sku_count_dict[sku] +=1

        


