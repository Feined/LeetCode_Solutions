class Solution {
    public boolean uniformArray(int[] nums1) {
        int min = Integer.MAX_VALUE;
        for(int i=0;i<nums1.length;i++){
            if(min>nums1[i]){
                min = nums1[i];
            }
        }
        System.out.println(min);
        if(min%2==1){
            return true; // All odd possible
        }
        else{
            for(int j=0;j<nums1.length;j++){
                if(nums1[j]%2==1){
                    return false;
                }
            }
        }
        return true;
    }
}