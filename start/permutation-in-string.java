import java.util.*;

class Solution {
    public boolean checkInclusion(String s1, String s2) {
        Map<Character, Integer> s1Freq = new HashMap<>();
        for (char c : s1.toCharArray()) {
            s1Freq.put(c, s1Freq.getOrDefault(c, 0) + 1);
        }

        int left = 0;
        int count = 0;

        for (int right = 0; right < s2.length(); right++) {
            char currentChar = s2.charAt(right);

            // Decrement the frequency of the current character in s1Freq
            if (s1Freq.containsKey(currentChar)) {
                s1Freq.put(currentChar, s1Freq.get(currentChar) - 1);
                if (s1Freq.get(currentChar) >= 0) {
                    count++;
                }
            }

            // Shrink the sliding window from the left if it becomes larger than s1
            if (right - left + 1 > s1.length()) {
                char leftChar = s2.charAt(left);
                if (s1Freq.containsKey(leftChar)) {
                    s1Freq.put(leftChar, s1Freq.get(leftChar) + 1);
                    if (s1Freq.get(leftChar) > 0) {
                        count--;
                    }
                }
                left++;
            }

            // If all characters from s1 are found in s2 in the same order, return true
            if (count == s1.length()) {
                return true;
            }
        }

        return false;
    }
}