class Solution {
    companion object { 
        lateinit var answer: MutableList<MutableList<Int>>
        lateinit var list: MutableList<Int>
        var limit = 0 
        var sum = 0
    }

    fun combinationSum3(k: Int, n: Int): List<List<Int>> {
        answer = mutableListOf()
        list = MutableList(k) { 0 }

        limit = k
        sum = n

        dfs(0, 0, 1)
        return answer 
    }

    private fun dfs(s: Int, n: Int, index: Int){
        if(n == limit){
            if(s == sum){
                answer.add(ArrayList(list))
            }
            return 
        }

        for(i in index..9){
            list[n] = i
            dfs(s+i, n+1, i+1)
        }
    }
}