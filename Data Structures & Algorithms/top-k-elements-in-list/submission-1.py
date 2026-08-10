class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
      
        freq_list = []
        for val, count in counts.items():
            freq_list.append((count, val))
        
  
        freq_list.sort(reverse=True)
        
        arr = []
        for i in range(k):
            arr.append(freq_list[i][1])

        return arr