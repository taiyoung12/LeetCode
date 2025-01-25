class Solution {
    fun maxVowels(s: String, k: Int): Int {
        val standards = listOf('a', 'e', 'i', 'o', 'u')
        var comp = 0
        var answer = 0
        
        for(i in 0 until k){
            if(s[i] in standards){
                comp++
            }
        }

        answer = comp

        for(i in k until s.length){
            if(s[i-k] in standards){
                comp--
            }
            if(s[i] in standards){
                comp++
            }

            if(comp > answer){
                answer = comp
            }

            if(answer == k){
                return k
            }
            
        }

        return answer
    }
}