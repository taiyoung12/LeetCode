class Solution {
    fun successfulPairs(spells: IntArray, potions: IntArray, success: Long): IntArray {
        val answer = IntArray(spells.size)
        val sortedPotions = potions.sorted()
        val total = potions.size
        
        for(i in spells.indices){
            val comp = spells[i].toLong()
            
            val m = sortedPotions.binarySearch{
                if(it*comp >= success) 1 else -1
            }
            
            answer[i] = total - (-(m+1))
        }
        
        return answer
    }
}