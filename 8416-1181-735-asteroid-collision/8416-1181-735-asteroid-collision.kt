import kotlin.math.abs

class Solution {
    fun asteroidCollision(asteroids: IntArray): IntArray {
        val stack = mutableListOf<Int>()
        stack.add(asteroids[0])

        for(i in 1 until asteroids.size){
            var asteroid = asteroids[i]
            
            if (stack.isEmpty()) {
                stack.add(asteroid)
                continue
            }

            while (stack.isNotEmpty() && asteroid < 0 && stack.last() > 0) {
                val target = abs(stack.last())
                val comp = abs(asteroid)

                if (target > comp) {
                    asteroid = 0
                    break
                } else if (target < comp) {
                    stack.removeAt(stack.lastIndex)
                } else {
                    stack.removeAt(stack.lastIndex)
                    asteroid = 0
                    break
                }
            }

            if (asteroid != 0) {
                stack.add(asteroid)
            }
        }

        return stack.toIntArray()
    }
}