class Solution {
    fun compress(chars: CharArray): Int {
        var read = 0 
        var write = 0 

        while(read < chars.size){
            var count = 0 
            val target = chars[read]

            while (read < chars.size && chars[read] == target) {
                count++
                read++
            }

            chars[write] = target
            write++

            if (count > 1) {
                for (c in count.toString()) {
                    chars[write] = c
                    write++
                }
            }
        }

        return write
    }
}