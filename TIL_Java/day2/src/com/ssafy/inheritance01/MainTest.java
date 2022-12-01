package com.ssafy.inheritance01;

public class MainTest {
    public static void main(String[] args) {
//        Person p = new Person() ;
        Student st = new Student();

//        st.study();
        st.major = "법학";
        st.name = "양";
        st.age = 45;

        st.eat();
        st.eat("햄버거");

        System.out.println(st.toString());
    }
}
