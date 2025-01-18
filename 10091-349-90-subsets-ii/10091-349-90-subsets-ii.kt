class Solution {
    fun subsetsWithDup(nums: IntArray): List<List<Int>> {
        val answer = mutableListOf<List<Int>>()
        nums.sort() 
        
        fun backtrack(start: Int, current: MutableList<Int>) {
            answer.add(current.toList())

            for(i in start until nums.size){
                if(i > start && nums[i] == nums[i-1])
                    continue 
                
                current.add(nums[i])
                backtrack(i+1, current)
                current.removeAt(current.size-1)
            }

        }
        
        backtrack(0, mutableListOf())
        return answer
    }
}