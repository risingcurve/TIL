package com.ssafy.modifier04;

import com.ssafy.modifier02.Student;

public class StudentManager {
    Student[] students = new Student[100];
    int size = 0;

    public void addStudent(Student s) {
        students[size++] = s;
    }

    void changeMajor(String name, String major) {
        Student s = getStudent(name);
        if (s != null) {
            s.setMajor(major);
        }
    }

    Student getStudent(String name) {
        for (int i = 0; i < size; i++) {
            if (name.equals(students[i].getName())){
                // 찾았어? 그럼 바로 리턴
                return students[i];
            }
        }

        return null;
    }


}
