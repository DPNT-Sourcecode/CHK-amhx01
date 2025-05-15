class CheckoutSolution:

    # skus = unicode string
    def checkout(self, skus):
        try:
            a_pricing_rules = {
                1: 50,
                3: 130,
                5: 200
            }
            b_pricing_rules = {
                1: 30,
                2: 45
            }
            f_pricing_rules = {
                1:10
            }
            valid_items = ['A', 'B', 'C', 'D', 'E', 'F']
            sku_special_items_count_dict = {
                'A': 0,
                'B': 0,
                'E': 0,
                'F': 0,
            }
            standard_items = {'C':20, 'D': 15, 'E': 40}
            total_value = 0
            if type(skus) == list:
                for string in skus:
                    sku_special_items_count_dict, total_value = self.sort_data_from_string(string, valid_items, standard_items, sku_special_items_count_dict, total_value)
            else: 
                sku_special_items_count_dict, total_value = self.sort_data_from_string(skus, valid_items, standard_items, sku_special_items_count_dict, total_value)

        except Exception as e:
            return -1
        
        sku_special_items_count_dict = self.edit_dict_for_gof_deal(sku_special_items_count_dict['F'], 3, 'F', sku_special_items_count_dict)
        sku_special_items_count_dict = self.edit_dict_for_gof_deal(sku_special_items_count_dict['E'], 2, 'B', sku_special_items_count_dict)
        total_value += self.get_value_for_special_offers(sku_special_items_count_dict['F'], f_pricing_rules)
        total_value += self.get_value_for_special_offers(sku_special_items_count_dict['A'], a_pricing_rules)
        total_value+= self.get_value_for_special_offers(sku_special_items_count_dict['B'], b_pricing_rules)

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
        if amount == 0 or dict_result[free_item] == 0:
            return dict_result
        free_items_amount = amount // offer_amount
        dict_result[free_item]= dict_result[free_item] - free_items_amount
        return dict_result

    
    def get_value_for_special_offers(self, amount: int, pricing_rule: dict) -> int:
        total = 0
        remaining = amount
        for group_size in sorted(pricing_rule.keys(), reverse=True):
            num_groups = remaining // group_size
            total += num_groups * pricing_rule[group_size]
            remaining = remaining % group_size
        return total
    

CheckoutSolution().checkout(['FFF'])

