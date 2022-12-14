import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashSet;
import java.util.List;

public class day09 {
    public static void part1and2() {
        Point[] lstRope = new Point[10];
        for(int i = 0;i<lstRope.length;i++)
            lstRope[i] = new Point(0, 0); 
        HashSet<Point> tailVisited0 = new HashSet<Point>();
        HashSet<Point> tailVisited8 = new HashSet<Point>();
        Instruction[] instructions = getDay09Input();
        for (Instruction instruction : instructions) {
            for (int i = 0; i < instruction.steps; i++) {
                lstRope[0].x += instruction.offset.x;
                lstRope[0].y += instruction.offset.y;

                for (int j = 1; j < lstRope.length; j++) {
                    if (Math.abs(lstRope[j-1].x - lstRope[j].x) >1 || Math.abs(lstRope[j-1].y - lstRope[j].y) >1){
                        lstRope[j] = calcNextKnot(lstRope[j - 1], lstRope[j]);
                    }else{
                        break;
                    }
                    
                }
                tailVisited0.add(lstRope[1].Copy());
                tailVisited8.add(lstRope[9].Copy());
            }
        }
        System.out.println("Part1: " + tailVisited0.size() + "\nPart2: " + tailVisited8.size());
    }

    private static Point calcNextKnot(Point head, Point tail) {
        if ((head.x - tail.x == 2) && (head.y - tail.y == 2)) { // UP/R diagonal check
            tail.x += 1;
            tail.y += 1;
        } else if ((head.x - tail.x == -2) && (head.y - tail.y == 2)) { // UP/L diagonal check
            tail.x -= 1;
            tail.y += 1;
        } else if ((head.x - tail.x == 2 && head.y - tail.y == -2)) { // DOWN/R diagonal check
            tail.x += 1;
            tail.y -= 1;
        } else if ((head.x - tail.x == -2 && head.y - tail.y == -2)) { // DOWN/L diagonal check
            tail.x -= 1;
            tail.y -= 1;
        } else if ((head.y - tail.y > 1 && Math.abs(head.x - tail.x) == 1)) { // UP L check
            tail.x = head.x;
            tail.y += 1;
        } else if ((head.y - tail.y < -1 && Math.abs(head.x - tail.x) == 1)) { // DOWN L check
            tail.x = head.x;
            tail.y -= 1;
        } else if ((head.y != tail.y) && (head.x - tail.x > 1)) { // Right L check
            tail.x += 1;
            tail.y = head.y;
        } else if ((head.y != tail.y) && head.x - tail.x < -1) { // Left L check
            tail.x -= 1;
            tail.y = head.y;
        } else if (head.x - tail.x == 2) { // moved 1 up
            tail.x += 1;
        } else if (head.x - tail.x == -2) { // moved 1 down
            tail.x -= 1;
        } else if (head.y - tail.y == 2) { // moved 1 right
            tail.y += 1;
        } else if (head.y - tail.y == -2) { // moved 1 left
            tail.y -= 1;
        }
        return tail;
    }

    // *Create a list of offsets on the Head node */
    private static Instruction[] getDay09Input() {
        try {
            List<String> lines = Files.readAllLines(Path.of("2022", "09", "inputs", "input.txt"));
            Instruction[] pointList = new Instruction[lines.size()];
            int i = 0;

            for (String line : lines) {
                String[] _lineData = line.split(" ");
                Character c = _lineData[0].toCharArray()[0];
                int steps = Integer.parseInt(_lineData[1]);
                switch (c) {
                    case 'R' -> pointList[i] = new Instruction(new Point(1, 0), steps);
                    case 'U' -> pointList[i] = new Instruction(new Point(0, 1), steps);
                    case 'L' -> pointList[i] = new Instruction(new Point(-1, 0), steps);
                    case 'D' -> pointList[i] = new Instruction(new Point(0, -1), steps);
                    default -> throw new IllegalArgumentException("Invalid move");
                }
                i++;
            }
            return pointList;
        } catch (Exception e) {
            return null;
        }
    }

    public static void main(String[] args) {
        System.out.println("START PROGRAM");
        if (args.length > 0){
            for(String s :args)
                System.out.println("args: "+s);
        }
        long timeA = System.nanoTime();
        day09.part1and2();
        long timeB = System.nanoTime();
        System.out.println("Elapsed time: " + (timeB - timeA) / 1000000+" ms");
    }

    public static class Instruction {
        public Point offset;
        public int steps;

        public Instruction(Point offset, int steps) {
            this.offset = offset;
            this.steps = steps;
        }
    }

    public static class Point {
        public int x;
        public int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public Point Copy(){
            return new Point(this.x,this.y);
        }

        @Override
        public String toString() {
            return x + "," + y;
        }

        @Override
        public boolean equals(Object other) {
            if ((other == null) || !(other instanceof Point)) {
                return false;
            }
            return ((Point) other).x == (this.x) && ((Point) other).y == (this.y);
        }

        // https://stackoverflow.com/questions/113511/best-implementation-for-hashcode-method-for-a-collection
        @Override
        public int hashCode() {
            int result = -1;
            result = 37 * result + (int) x;
            result = 73 * result + (int) y;
            return result;
        }
    }
}