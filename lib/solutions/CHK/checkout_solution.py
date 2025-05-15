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
            h_pricing_rules = {
                1: 10,
                5: 45,
                10: 80
            }
            k_pricing_rules = {
                1: 80,
                2: 150
            }
            m_pricing_rules = {
                1: 15
            }
            n_pricing_rules = {
                1: 40
            }
            p_pricing_rules = {
                1: 50,
                5: 200
            }
            q_pricing_rules = {
                1: 30,
                3: 80
            }
            r_pricing_rules = {
                1: 50
            }
            u_pricing_rules = {
                1: 40
            }
            v_pricing_rules = {
                1: 50,
                2: 90,
                3: 130
            }
            valid_items = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            sku_special_items_count_dict = {
                'A': 0,
                'B': 0,
                'E': 0,
                'F': 0,
                'H': 0,
                'K': 0,
                'M': 0,
                'N': 0,
                'P': 0,
                'Q': 0,
                'R': 0,
                'U': 0,
                'V': 0,
            }
            price_combo_letter_dict_values = {
                'S': 20,
                'T': 20,
                'X': 17,
                'Y': 20,
                'Z': 21,
            }
            combo_letter_count_dict = {
                'S': 0,
                'T': 0,
                'X': 0,
                'Y': 0,
                'Z': 0, 
            }
            standard_items = {'C':20, 'D': 15, 'E': 40, 'G': 20, 'I': 35, 'J': 60,'L': 90, 'O': 10, 'W': 20}
            total_value = 0
            if type(skus) == list:
                for string in skus:
                    special_and_combo_dict, total_value = self.sort_data_from_string(string, valid_items, standard_items, sku_special_items_count_dict, combo_letter_count_dict, total_value)
            else: 
                special_and_combo_dict, total_value = self.sort_data_from_string(skus, valid_items, standard_items, sku_special_items_count_dict, combo_letter_count_dict, total_value)

        except Exception as e:
            return -1
        
        sku_special_items_count_dict = special_and_combo_dict['special_dict']
        combo_letter_count_dict = special_and_combo_dict['combo_dict']
        
        sku_special_items_count_dict = self.edit_dict_for_gof_deal(sku_special_items_count_dict['U'], 4, 'U', sku_special_items_count_dict)
        sku_special_items_count_dict = self.edit_dict_for_gof_deal(sku_special_items_count_dict['R'], 3, 'Q', sku_special_items_count_dict)
        sku_special_items_count_dict = self.edit_dict_for_gof_deal(sku_special_items_count_dict['F'], 3, 'F', sku_special_items_count_dict)
        sku_special_items_count_dict = self.edit_dict_for_gof_deal(sku_special_items_count_dict['N'], 3, 'M', sku_special_items_count_dict)
        sku_special_items_count_dict = self.edit_dict_for_gof_deal(sku_special_items_count_dict['E'], 2, 'B', sku_special_items_count_dict)
        total_value += self.get_value_for_special_offers(sku_special_items_count_dict['R'], r_pricing_rules)
        total_value += self.get_value_for_special_offers(sku_special_items_count_dict['N'], n_pricing_rules)
        total_value += self.get_value_for_special_offers(sku_special_items_count_dict['M'], m_pricing_rules)
        total_value += self.get_value_for_special_offers(sku_special_items_count_dict['F'], f_pricing_rules)
        total_value += self.get_value_for_special_offers(sku_special_items_count_dict['U'], u_pricing_rules)
        total_value += self.get_value_for_special_offers(sku_special_items_count_dict['A'], a_pricing_rules)
        total_value+= self.get_value_for_special_offers(sku_special_items_count_dict['B'], b_pricing_rules)
        total_value+= self.get_value_for_special_offers(sku_special_items_count_dict['H'], h_pricing_rules)
        total_value+= self.get_value_for_special_offers(sku_special_items_count_dict['K'], k_pricing_rules)
        total_value+= self.get_value_for_special_offers(sku_special_items_count_dict['P'], p_pricing_rules)
        total_value+= self.get_value_for_special_offers(sku_special_items_count_dict['Q'], q_pricing_rules)
        total_value+= self.get_value_for_special_offers(sku_special_items_count_dict['V'], v_pricing_rules)

        return total_value
    
    def sort_data_from_string(self, skus:str, valid_items: list, standard_items: dict, sku_special_items_count_dict: dict, combo_count_letter_dict: dict, total_value: int):
        for sku in skus:
            if sku not in valid_items:
                return -1
            if sku in standard_items:
                total_value += standard_items[sku]
            if sku in sku_special_items_count_dict:
                sku_special_items_count_dict[sku] +=1
            if sku in combo_count_letter_dict:
                combo_count_letter_dict +=1

        
        return {'special_dict': sku_special_items_count_dict, 'combo_dict': combo_count_letter_dict}, total_value
    
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
    

CheckoutSolution().checkout(['NNNM'])

