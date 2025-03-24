public class i23_data_typesInteger {
    public static void main(String[] args) {
        // посчитайте свет пройдет за-1-год какое-расстояние ?
        long speed_light = 300_000;
        System.out.println(speed_light * 365 * 24 * 60 * 60);

        int a = 5;
        a = a + 1;
        // OR
        a += 1;

        // оператор инкримента.
        a++;    // a += 1;

        // оператор де-кримента
        a--;
        System.out.println(a);


        // что если переполнить byte ?
        byte b = 127;
        b += 1;
        System.out.println(b);
        // отсчет начался заново с -128


        // привести:явно к-типу
        byte c = 127;
        c = (byte) (c + 10);
        c++;
        System.out.println(c);
    }
}
