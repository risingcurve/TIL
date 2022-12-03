package com.ssafy.abstractclass2;

public class ChefTest {
	public static void main(String[] args) {
		Chef[] chefs = new Chef[2];
		
		chefs[0] = new KFoodChef();
		chefs[1] = new KFoodChef();
		
		for(Chef chef : chefs) {
			chef.eat();
			chef.cook();
		}
	}
}
