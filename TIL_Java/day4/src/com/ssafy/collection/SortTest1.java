package com.ssafy.collection;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class SortTest1 {
	public static void main(String[] args) {
		List<String> list = new ArrayList<>();
		
		list.add("Kim");
		list.add("Lee");
		list.add("Hyeon");
		list.add("Oh");
		list.add("Nam");
		list.add("samsung");
		list.add("SAMSUNG");
		
		Collections.sort(list);
		
		System.out.println(list);
	}
}
