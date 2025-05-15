
class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        try:
            sku_special_items_count_dict = {
                'A': 0,
                'B': 0,
                'E': 0,
            }
            standard_items = {'C':20, 'D': 15, 'E': 40}
            total_value = 0
            for sku in skus:
                if sku in standard_items:
                    total_value += standard_items[sku]
                if sku in sku_special_items_count_dict:
                    sku_special_items_count_dict[sku] +=1
        except Exception as e:
            return e
        
        sku_special_items_count_dict = self.edit_dict_for_gof_deal(sku_special_items_count_dict['E'], 2, 'B', sku_special_items_count_dict)
        total_value += self.get_value_for_special_offers(130, 3, 50, sku_special_items_count_dict['A'])
        total_value+= self.get_value_for_special_offers(45, 2, 30, sku_special_items_count_dict['B'])

        return total_value
    
    def edit_dict_for_gof_deal(self, amount:int, offer_amount:int, free_item: str, dict_result: dict)->dict:
        free_items_amount = amount // offer_amount
        return dict_result[free_item] - free_items_amount

    
    def get_value_for_special_offers(self, special_value: int, offer_amount: int, normal_value: int, amount: int) -> int:
        if amount == 0:
            return 0
        if amount < offer_amount:
            return amount * normal_value
        else:
            offer_value = amount // offer_amount * special_value
            normal_value = amount % offer_amount * normal_value
            return  normal_value + offer_value


        



