class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> freq_map =new HashMap<>();
        for(int i=0;i<nums.length;i++){
            freq_map.put(nums[i],freq_map.getOrDefault(nums[i],0)+1);
        }
        List<List<Integer>> buckets = new ArrayList<>();
        for(int i=0;i<nums.length +1;i++){
            buckets.add(new ArrayList<>());
        }
        for(Map.Entry<Integer,Integer> entry: freq_map.entrySet()){
            buckets.get(entry.getValue()).add(entry.getKey());

        }
        List<Integer> values = new ArrayList<>();
        for(int j =nums.length;j>=0;j--){
           for (int i=0;i<buckets.get(j).size();i++){
            values.add(buckets.get(j).get(i));
            if (values.size() ==k){
                int[] result = new int[k];
                    for (int x = 0; x < k; x++) {
                        result[x] = values.get(x);
                    }
                    return result;
            }
           }
        }
        return new int[0];
        
    }
}
