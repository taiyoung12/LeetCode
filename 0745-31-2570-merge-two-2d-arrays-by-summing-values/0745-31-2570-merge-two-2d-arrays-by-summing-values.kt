class Solution {
    fun mergeArrays(nums1: Array<IntArray>, nums2: Array<IntArray>): Array<IntArray> {
        val target = mutableMapOf<Int, MutableList<Int>>()

        for(num in nums1){
            if(num[0] !in target){
                target[num[0]] = mutableListOf(num[1])
            }else{
                target[num[0]]!!.add(num[1])
            }
        }

        for(num in nums2){
            if(num[0] !in target){
                target[num[0]] = mutableListOf(num[1])
            }else{
                target[num[0]]!!.add(num[1])
            }
        }

        val sortedTarget = target.toSortedMap()

        val answer = mutableListOf<IntArray>()
        for((key, values) in sortedTarget){
            answer.add(intArrayOf(key, values.sum()))
        }
        
        return answer.toTypedArray()
    }
}