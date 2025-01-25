class Solution {
    fun maxOperations(nums: IntArray, k: Int): Int {
        val nums = nums.sorted()
        var start = 0 
        var end = nums.size-1
        var answer = 0

        while(start < end){
            val comp = nums[start] + nums[end]

            if(comp == k){
                answer++
                start++
                end--
            }else if(comp < k){
                start++
            }else if(comp > k){
                end--
            }
        }

        return answer
    }
}