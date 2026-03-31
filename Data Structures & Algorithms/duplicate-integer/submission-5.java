class Solution {
    public boolean hasDuplicate(int[] nums) {
        List<Integer> values = new ArrayList<>();
        for (int num : nums){
            if (values.contains(num)){
                return true;
            } else {
                values.add(num);
            }

        }
        return false;
    
}
    
}