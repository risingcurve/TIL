package com.ssafy.ploymorphism2;

class SuperClass {
	String x = "super";
	
	public void method() {
		System.out.println("super class method");
	}
}

class SubClass extends SuperClass {
	String x = "sub";
	
	@Override
	public void method() {
		System.out.println("sub class method");
	}
}


public class MemberBindingTest {
	
	public static void main(String[] args) {
		SubClass subClass = new SubClass();
		System.out.println(subClass.x);
		subClass.method();
		
		SuperClass superClass = subClass;
		System.out.println(superClass.x);
		superClass.method();
	}
}
