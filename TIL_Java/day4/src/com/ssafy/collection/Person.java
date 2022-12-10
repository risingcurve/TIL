package com.ssafy.collection;

public class Person {
	String name;
	String pNum;
	
	
	public Person() {
		
	}
	
	public Person(String name, String pNum) {
		this.name = name;
		this.pNum = pNum;
	}

	@Override
	public String toString() {
		return "name=" + name + ", pNum=" + pNum;
	}
	
	public boolean equals(Object obj) {
		if(this == obj) return true;
		if(obj == null) return false;
		Person other = (Person) obj;
		return pNum.equals(other.pNum);
	}
}
