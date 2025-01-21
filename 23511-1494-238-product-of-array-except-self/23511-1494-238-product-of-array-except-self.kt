class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        if(nums.count{ it == 0 } > 1){
            return IntArray(nums.size)
        }

        val answer = IntArray(nums.size)
        val comp = nums.reduce { acc, num -> acc*num }
        val zero = nums.filter{ it != 0 }.reduce{ acc, num -> acc*num }

        for(index in nums.indices){
            if(nums[index] == 0){
                answer[index] = zero
                continue
            }
            answer[index] = comp/nums[index]
        }

        return answer
    }
}