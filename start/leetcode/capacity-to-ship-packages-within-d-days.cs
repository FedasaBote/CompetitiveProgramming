public class Solution {
    public int ShipWithinDays(int[] weights, int days) {
        int Low = weights.Max(),High = weights.Sum();

        while(Low < High) {
            int Mid = Low + (High - Low)/2;
            int currentWeights = 0;
            int currentDays = 1;

            foreach(var weight in weights) {
                if (currentWeights + weight > Mid){
                    currentWeights = weight;
                    currentDays += 1;
                }else{
                    currentWeights += weight;
                }
            }

            if(currentDays >days){
                Low = Mid +1;
            }else{
                High = Mid;
            }
        }

        return Low;
    }
}