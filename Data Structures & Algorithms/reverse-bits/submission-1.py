class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = bin(n)[2:].zfill(32) 
    
        lst = list(map(int, binary_str))
    
        lst.reverse()
    
        reversed_binary_str = ''.join([str(i) for i in lst])
        return int(reversed_binary_str, 2)