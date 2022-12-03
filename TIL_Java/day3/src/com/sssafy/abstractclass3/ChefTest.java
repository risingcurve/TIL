package com.sssafy.abstractclass3;

public class ChefTest {
	public static void main(String[] args) {
		Chef[] chefs = new Chef[2];
		
		chefs[0] = new KFoodChef();
		chefs[1] = new KFoodChef();
		
		for(Chef chef : chefs) {
			chef.eat();
			
			if (chef instanceof KFoodChef) {
				KFoodChef k = (KFoodChef) chef;
				k.cook();
				
			} else if (chef instanceof JFoodChef) {
				((JFoodChef)chef).cook();
			}
			
			
		}
	}
}
