class Solution:
    def distMoney(self, money: int, children: int) -> int:
        child = 0
        
        if children > money:
            return -1
        money -= children
        
        for i in range(children - 1):
            if money >= 7:
                child += 1
                money -= 7
            else:
                return child
        
        if money == 3:
            if child > 0:
                child -= 1
            else:
                return -1
        
        if money == 7:
            child += 1
        
        return child
