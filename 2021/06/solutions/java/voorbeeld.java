import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;

public class voorbeeld {

    public static void main(String[] args) throws IOException {
        long timeA = System.nanoTime();
        System.out.println(part1());
        long timeB = System.nanoTime();
        System.out.println("Elapsed time: " + (timeB - timeA)/1000);
       //System.out.println(part2());
        
    }

    private static long part1() throws IOException {
        long[] fishCounts = getInput();

        for (int i = 0; i < 1048576; i++) {
            handleStep(fishCounts);
        }

        return Arrays.stream(fishCounts).reduce(Long::sum).getAsLong();
    }

    private static long part2() throws IOException {
        long[] fishCounts = getInput();

        for (int i = 0; i < 1048576; i++) {
            handleStep(fishCounts);
        }

        return Arrays.stream(fishCounts).reduce(Long::sum).getAsLong();
    }

    private static void handleStep(long[] counts) {
        long newBorn = counts[0];
        System.arraycopy(counts, 1, counts, 0, 8);

        counts[6] += newBorn;
        counts[8] = newBorn;
    }

    private static long[] getInput() throws IOException {
        long[] result = new long[9];

        Arrays.stream(Files.readAllLines(Path.of("6/input.txt")).get(0).split(","))
                .mapToInt(Integer::parseInt).forEach(val -> result[val]++);

        return result;
    }

}
