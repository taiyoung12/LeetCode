class Solution {
    companion object { 
        lateinit var target: MutableList<Boolean>
    }

    fun canVisitAllRooms(rooms: List<List<Int>>): Boolean {
        target = MutableList(rooms.size){ false }
        target[0] = true 

        dfs(rooms, rooms[0])
        
        return target.all{ it }
    }

    private fun dfs(rooms: List<List<Int>>, room: List<Int>){
        for(r in room){
            if(!target[r]){
                target[r] = true
                dfs(rooms, rooms[r])
            }
        }
    }
}