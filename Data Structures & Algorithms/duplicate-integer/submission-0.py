class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_map={}
        for i in nums:
            hash_map[i]=hash_map.get(i,0)+1
        for i in hash_map.values():
            if i>1:
                return True
        return False