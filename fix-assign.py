import random

class Equipment:
    def __init__(self, item_level, type, refine_level):
        self.ItemLevel = item_level
        self.Type = type
        self.RefineLevel = refine_level
        
    def upgrade_level(self, rand_int, rate, is_vip):
        if rand_int < rate:
            if self.Type in ["Weapon", "Armor"]:
                return 1
        else:
            if is_vip:
                return -1
            else:
                return 0

class RefineCalculator:
    def RefineEquipments(self, equipments, isVIP):
        for e in equipments:
            rand_int = random.randint(0, 100)
            if e.ItemLevel < 10:
                if e.Type == "Weapon":
                    if (e.ItemLevel == 1) or (e.ItemLevel == 2):
                        if e.RefineLevel < 7:
                            e.ItemLevel += 1
                        elif e.RefineLevel < 9:
                            if e.ItemLevel == 1:
                                e.ItemLevel += e.upgrade_level(rand_int, 60, isVIP)
                            else:
                                e.ItemLevel += e.upgrade_level(rand_int, 30, isVIP)
                        else:
                            if e.ItemLevel == 1:
                                e.ItemLevel += e.upgrade_level(rand_int, 20, isVIP)
                            else:
                                e.ItemLevel += e.upgrade_level(rand_int, 15, isVIP)
                    else:
                        if e.RefineLevel < 5:
                            e.ItemLevel += 1
                        elif e.RefineLevel < 7:
                            e.ItemLevel += e.upgrade_level(rand_int, 40, isVIP)
                        else:
                            e.ItemLevel += e.upgrade_level(rand_int, 10, isVIP)

                elif e.Type == "Armor":
                    rate = (10 - e.RefineLevel) * 10
                    if e.RefineLevel < 5:
                        e.ItemLevel += 1
                    else:
                        e.ItemLevel += e.upgrade_level(rand_int, rate, isVIP)