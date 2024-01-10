class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        List<int[]> result = new ArrayList<>();
        int i = 0;
        int j = 0;
        
        while (i < firstList.length && j < secondList.length) {
            int start1 = firstList[i][0];
            int end1 = firstList[i][1];
            int start2 = secondList[j][0];
            int end2 = secondList[j][1];
            
            if (end1 < start2) {
                i++;
            } else if (end2 < start1) {
                j++;
            } else {
                int start = Math.max(start1, start2);
                int end = Math.min(end1, end2);
                result.add(new int[]{start, end});
                if (end1 > end2) {
                    j++;
                } else {
                    i++;
                }
            }
        }
        
        int[][] output = new int[result.size()][2];
        for (int k = 0; k < result.size(); k++) {
            output[k] = result.get(k);
        }
        
        return output;
    }
}