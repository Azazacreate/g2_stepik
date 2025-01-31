public class i22_operatorConditional {
    public static void main(String[] args) {
        int temperature = 25;
        if (temperature > 25) {
            System.out.println("включить кондиционер");
        }
        else if (temperature == 25) {
            System.out.printf("все зер гуд. температура = гуд.");
        }
        else if (temperature < 25) {
            System.out.printf("выключить кондиционер");
        }
        System.out.printf("\n\n");

        // hw
        int n = 30;
        if (n >= 10) {
            System.out.println("Pizza");
        }
        else if (n >= 6 & n < 10) {
            System.out.println("Hamburger");
        }
        else {
            System.out.println("Sandwich");
        }
    }
}
