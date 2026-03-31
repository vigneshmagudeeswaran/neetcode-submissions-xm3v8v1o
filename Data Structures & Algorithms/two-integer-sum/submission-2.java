class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> numValue = new HashMap<>();
        for(int i=0; i< nums.length;i++){
            int value =target - nums[i];
            if (numValue.containsKey(value)){
                return new int[]{numValue.get(value),i};
            }
            numValue.put(nums[i],i);

        }
        return new int[] {};
    }
}
