class Solution {
    public String breakPalindrome(String palindrome) {
        StringBuilder s = new StringBuilder(palindrome);
        int n = s.length();
        if (n == 0 || n == 1) return "";  

        for (int i = 0; i < n; i++) {
            if (n % 2 == 1 && i == n / 2) {
                continue;  
            }
            if (s.charAt(i) != 'a') {
                s.setCharAt(i, 'a'); 
                return s.toString();
            }
        }

        
        s.setCharAt(n - 1, 'b');
        return s.toString();
    }
}