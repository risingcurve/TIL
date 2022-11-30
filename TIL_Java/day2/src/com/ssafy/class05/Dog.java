package class05;

public class Dog {
    String name;
    int age;

    Dog() {
        this("해피");
        
    }

    Dog(String n, int a) {
        name = n;
        age = a;        
    }

    Dog(int age) {
        this.age = age;
    }

    Dog(String name) {

    }

    void info() {
        System.out.println(this.name);
    }

}
