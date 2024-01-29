class Solution {
    public String shiftingLetters(String s, int[][] shifts) {
        int n = s.length();
        int[] characters = new int[n];
        
        for (int[] operation : shifts) {
            int start = operation[0];
            int end = operation[1];
            int direction = operation[2];
            if (direction == 1) {
                characters[start] += 1;
                if (end != n - 1)
                    characters[end + 1] -= 1;
            } else {
                characters[start] -= 1;
                if (end != n - 1)
                    characters[end + 1] += 1;
            }
        }
        
        for (int i = 0; i < n - 1; i++) {
            characters[i + 1] += characters[i];
        }
        
        StringBuilder ans = new StringBuilder(s);
        for (int j = 0; j < n; j++) {
            int c = (int) ans.charAt(j);
            c -= 'a';
            c += characters[j];
            while (c < 0) c += 26;
            ans.setCharAt(j, (char) (c % 26 + 'a'));
        }
        
        return ans.toString();
    }
}