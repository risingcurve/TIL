package com.ssafy.interface3;

public interface IStudentManager {

	void add(Student s);
	Student[] getList();
	Student searchByName(String name);
	
	boolean remove(String name);
}
