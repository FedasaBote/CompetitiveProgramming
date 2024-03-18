/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution : GuessGame {
    public int GuessNumber(int n) {
        int Left = 1, Right = n;
        
        while(Left <= Right){
            int Mid = Left + (Right - Left)/2;
            int g =guess(Mid);
            if (g == 0){
                return Mid;
            }
            else if(g == -1){
                Right = Mid -1;
            }else{
                Left = Mid +1;
            }
        }

        return -1;
    }
}