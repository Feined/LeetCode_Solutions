class Solution {
    public boolean canJump(int[] nums) {
        int manstand = 0;
        for(int i=0;i<nums.length;i++){
            if(i>manstand) return false;
            if(manstand>i+nums[i]) manstand = manstand;
            else manstand = i+nums[i];
        }
        return true;
    }
}