class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        try:
            valid_items = ['A', 'B', 'C', 'D', 'E']
            sku_special_items_count_dict = {
                'A': 0,
                'B': 0,
                'E': 0,
            }
            standard_items = {'C':20, 'D': 15, 'E': 40}
            total_value = 0
            if type(skus) == list:
                for string in skus:
                    sku_special_items_count_dict, total_value = self.sort_data_from_string(string, valid_items, standard_items, sku_special_items_count_dict)
            else: 
                sku_special_items_count_dict, total_value = self.sort_data_from_string(string, valid_items, standard_items, sku_special_items_count_dict)

        except Exception as e:
            return -1
        
        sku_special_items_count_dict = self.edit_dict_for_gof_deal(sku_special_items_count_dict['E'], 2, 'B', sku_special_items_count_dict)
        total_value += self.get_value_for_special_offers(130, [3, 5], 50, sku_special_items_count_dict['A'])
        total_value+= self.get_value_for_special_offers(45, [2], 30, sku_special_items_count_dict['B'])

        return total_value
    
    def sort_data_from_string(self, skus:str, valid_items: list, standard_items: dict, sku_special_items_count_dict: dict, total_value: int):
        for sku in skus:
            if sku not in valid_items:
                return -1
            if sku in standard_items:
                total_value += standard_items[sku]
            if sku in sku_special_items_count_dict:
                sku_special_items_count_dict[sku] +=1
        return sku_special_items_count_dict, total_value
    
    def edit_dict_for_gof_deal(self, amount:int, offer_amount:int, free_item: str, dict_result: dict)->dict:
        if amount == 0:
            return dict_result
        free_items_amount = amount // offer_amount
        dict_result[free_item]= dict_result[free_item] - free_items_amount
        return dict_result

    
    def get_value_for_special_offers(self, special_values: list, offer_amount: int, normal_value: int, amount: int) -> int:
        if amount == 0:
            return 0
        if amount < offer_amount:
            return amount * normal_value
        else:
            offer_value = amount // offer_amount * special_value
            normal_value = amount % offer_amount * normal_value
            return  normal_value + offer_value


        
CheckoutSolution().checkout(['EEB'])
