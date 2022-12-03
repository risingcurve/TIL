package com.ssafy.interface1;

public interface MyInterface {
	public static final int MEMBER1 = 10;
	// public static fianl 이 생략된 것일 뿐 알아서 들어감.
	int MEMBER2 = 10;
	
	public abstract void method1(int param);
	// public abstract 이 생략된 것일 뿐
	void method2(int param);
}
