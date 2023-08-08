class Solution:

    def calculate_pascal_layer_total (self, layer):
        # Your code goes here
        return 2**layer if layer >= 0 else -1