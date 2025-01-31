import java.util.*;
class Solution {
    static int[] circularElements;
    static Set<Integer> set = new HashSet<>();
    static int max;
    public int solution(int[] elements) {
        max = elements.length;
        circularElements = new int[max * 2];
        for(int i = 0; i < max; i++){
            circularElements[i] = elements[i];
        }
        for(int i = max; i < max * 2; i++){
            circularElements[i] = elements[i - max];
        }
        
        int [] prefixSum = new int [max * 2 + 1];
        for(int i = 1; i <= max * 2; i++){
            prefixSum[i] = prefixSum[i-1] + circularElements[i-1];
        }
        for(int i = 0; i <= max * 2; i++){
            for(int j = i+1; j <= max *2; j++){
                if(j - i > max) break;
                set.add(prefixSum[j] - prefixSum[i]);
            }    
        }
        return set.size();
    }
}
