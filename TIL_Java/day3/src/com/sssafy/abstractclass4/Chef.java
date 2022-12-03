package com.sssafy.abstractclass4;

public class Chef {
	String name;
	int age;
	String speciality;
	
	public void eat() {
		System.out.println("음식을 먹는다.");
	}
	
	// 미완성 메서드임을 밝힌다.
	public abstract void cook();
	
	
}
