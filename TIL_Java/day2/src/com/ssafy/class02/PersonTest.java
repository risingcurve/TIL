package com.ssafy.class02;

import java.util.Iterator;

// 이러한 다양한 자료형을 가질 수 있는 자료형을 만들고 싶다.
public class PersonTest {
	public static void main(String[] args) {
		
		String name1 = "Yang";
		String name2 = "Hong";
		
		int age1 = 45;
		int age2 = 25;
		
		String hobby1 = "youtube";
		String hobby2 = "Golf";
		
		int size = 2;
		String[] names = new String[size];
		names[0] = "Yang";
		names[1] = "Hong";
		
		int[] ages = new int[size];
		ages[0] = 45;
		ages[1] = 25;
		
		String[] hobbies =new String[size];
		hobbies[0] = "Youtube";
		hobbies[1] = "Golf";
		
//		System.out.println("나의 이름은" + names[0] + "입니다.");
//		System.out.println("나이는" + ages[0] + "세, 취미는 "+ hobbies[0] + "입니다.");
//		System.out.println("나의 이름은" + names[1] + "입니다.");
//		System.out.println("나이는" + ages[1] + "세, 취미는 "+ hobbies[1] + "입니다.");
//		
//		
//		for(int i = 0; i<size; i++) {
//			System.out.println("나의 이름은" + names[i] + "입니다.");		
//			System.out.println("나이는" + age + 세, "취미는" + hobby + "입니다.");
//		}
		
		for(int i = 0; i<size; i++) {
			info(names[i], ages[i], hobbies[i]);
		}
	}
	
	static void info(String name, int age, String hobby) {
		System.out.println("나의 이름은" + name + "입니다.");
		System.out.println("나이는" + age +"세, 취미는" + hobby + "입니다.");
	}
}
