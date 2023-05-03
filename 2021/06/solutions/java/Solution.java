import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;

public class Solution {
    static public int MAX_AGE_DAYS = 8;
    static public int CALCULATION_DAYS = 256; //1048576

    public static void main(String[] args) {
        long timeA = System.nanoTime();
        long[] lstFishDatabase = getInput2();
        for (int i = 0; i < CALCULATION_DAYS + 1; i++) {
            long _newFish = lstFishDatabase[0];
            System.arraycopy(lstFishDatabase, 1, lstFishDatabase, 0, 8);
            lstFishDatabase[MAX_AGE_DAYS] = _newFish;
            lstFishDatabase[6] += _newFish;
        }
        long total = 0;
        for (int i = 0; i < MAX_AGE_DAYS; i++) {
            total += lstFishDatabase[i];
        }
        System.out.println(total);
        long timeB = System.nanoTime();
        System.out.println("Elapsed time: " + (timeB - timeA)/1000);
    }



    private static long[] getInput2() {
        long[] result = new long[9];

        try {
            Arrays.stream(Files.readAllLines(Path.of("2021","06","inputs","input.txt")).get(0).split(","))
                    .mapToInt(Integer::parseInt).forEach(val -> result[val]++);
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }

        return result;
    }

}