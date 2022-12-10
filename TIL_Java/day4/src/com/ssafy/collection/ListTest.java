package com.ssafy.collection;

import java.util.ArrayList;
import java.util.List;

public class ListTest {
	public static void main(String[] args) {
		List<String> names = new ArrayList<>();
		// 데이터의 빈번한 출입이 있을 경우 ArrayList는 좋은 선택이 아니다.
		
		
		names.add("Park");
		names.add("Yoo");
		names.add("Kim");
		names.add("Cheon");
		names.add(4, "Ha");
		
		System.out.println(names);
		
		// 비어있는지 체크
		System.out.println(names.isEmpty());
		System.out.println(names.size());
		
//		for(int i = 0 ; i<names.size(); i++) {
//			System.out.println(names.get(i));
//		}
		
		names.set(4, "Lee");
		
		names.remove(1);
		names.remove("Kim");
		
		for(String name : names) {
			System.out.println(name);
		}
		
		// 삭제할 때
		
		names.clear();
		names.add("Yang");
		names.add("Yang");
		names.add("Kim");
		
		// 앞에서부터 지워본다.
		for(int i = 0; i<names.size(); i++) {
			if(names.get(i).equals("Yang")) {
				names.remove(i);
			}
		}
		
		// 뒤에서부터 보면서 지운다.
		for(String name : names) {
			System.out.println(name);
		}
		
	}
}
