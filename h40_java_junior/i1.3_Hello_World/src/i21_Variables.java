public class i21_Variables {
    public static void main(String[] args) {
        /*
        int a = 5;
        int b = a + 5;
        System.out.println("b = " + b);

        int john = 100;
        int nick = john * 5;
        System.out.println("sum = " + (john + nick));

        a = 10;
        b = 3;
        int c = a / b;
        System.out.println("c = " + c);

        int d = 10;
        float e = 3;
        float f = d / e;
        System.out.println("f = " + f);

        int g = 10;
        int h = 4;
        int i = g % h;
        System.out.println("i = " + i);

        int j = 10 % 2 * 3;
        System.out.printf("j = " + j);
        */
        // task-1
        // дни перевести в-года,месяцы,дни.
        int days = 10000;
        int year = 365;
        int month = 30;
        System.out.println("years: " + days / year);
        System.out.println("months: " + days % year / month);
        System.out.println("days: " + days % year % month);
    }
}
