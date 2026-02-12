# customer_class.py
# The customer class represents a customer at the lemondade stand.
# The customer has preferences for lemonade sweetness and ice level,
# and a price point they are willing to pay.
# All of these attributes will influence their purchasing decision and
# are returned as a list of attributes.

import random

class Customer:
    def custmer(self, sweetness_preference=None, ice_preference=None, price_point=None, lemonness=None):
        self.sweetness_preference = (
            sweetness_preference if sweetness_preference is not None
            else random.randint(1, 3)
        )
        self.ice_preference = (
            ice_preference if ice_preference is not None
            else random.randint(0, 3)
        )
        self.price_point = (
            price_point if price_point is not None
            else round(random.uniform(0.25, 4.0),2)
        )
        self.lemonness = (
            lemonness if price_point is not None
            else random.randint(1,3)
        )
        return {
            "sweet": self.sweetness_preference,
            "ice": self.ice_preference,
            "price": self.price_point,
            "lemon": self.lemonness
        }
