import java.util.HashSet;

class Solution {
    public int maxVowels(String s, int k) {
        int maxCount = 0;
        int count = 0;
        int left = 0;
        HashSet<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));

        for (int end = 0; end < s.length(); end++) {
            char c = s.charAt(end);
            if (vowels.contains(Character.toLowerCase(c))) {
                count++;
            }
            if (end - left + 1 > k) {
                char leftChar = s.charAt(left);
                if (vowels.contains(Character.toLowerCase(leftChar))) {
                    count--;
                }
                left++;
            }
            maxCount = Math.max(maxCount, count);
        }

        return maxCount;
    }
}