package com.ssafy.modifier02;

import java.util.Scanner;
import java.util.SimpleTimeZone;

public class StudentTest {
    public static void main(String[] args) {

        Student[] students = new Student[10];
        int size = 0;

        Scanner sc = new Scanner(System.in);
        int sel;
        
        do {
            System.out.println("번호를 입력하세요.");
            System.out.println("1. 학생 추가");
            System.out.println("2. 학생 조회(이름으로)");
            System.out.println("3. 전공변경");
            System.out.println("0. 종료");
            sel = sc.nextInt();
            if(sel == 1) {
                // 학생 추가
                System.out.println("학생을 추가합니다.");
                System.out.print("이름 : ");
                String name = sc.next();
                System.out.print("나이 : ");
                int age = sc.nextInt();
                System.out.print("전공 : ");
                String major = sc.next();

                // 직접 빈껍떼기를 만들고 하나하나 세팅
//                Student st = new Student();
//                st.setName(name);
//                st.setAge(age);
//                st.setMajor(major);

                Student st = new Student(name, age, major);
                students[size++] = st;

            } else if (sel == 2) {
                // 학생 조회
                System.out.println("학생을 조회합니다.");
                System.out.print("이름 : ");
                String name = sc.next();

            }else if(sel == 3) {
                // 전공 변경
            }
        }while(sel!=0);
        
    } // main

    Student getStudent(String name) {
        for(int i = 0,
    }



}
