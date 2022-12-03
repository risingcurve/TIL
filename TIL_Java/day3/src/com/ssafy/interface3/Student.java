package com.ssafy.interface3;

public class Student {
	private String name;
	private int age;
	private String major;
	
	// 접근자 / 설정자를 만들어 사용한다.
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public String getMajor() {
		return major;
	}
	public void setMajor(String major) {
		this.major = major;
	}
	
	
}
