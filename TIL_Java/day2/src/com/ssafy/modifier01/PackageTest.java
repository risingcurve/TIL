package com.ssafy.modifier01;

// import java.lang.*; 자동으로 들어있어서 System.out.println();

import java.util.Arrays;
// 스캐너를 사용하기 위해서 import해서 가져온다.
import java.util.Scanner;
// import java.util.*;  이것 안에 모든 것을 넣을래.
import java.util.function.Function;

import com.ssafy.class03.Person;


public class PackageTest {
    public static void main(String[] args) {
		Scanner sc;

		Arrays arr;

		Function f;

		Person p; // class03dp 있는 Person 이라는 것을 가지고 옴.

		com.ssafy.class02.Person p2; // import를 하지 않고 여기에 풀패키지명을 작성할 수 있음.

	}
}
