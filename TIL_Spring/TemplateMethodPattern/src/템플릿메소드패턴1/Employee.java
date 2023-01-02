package 템플릿메소드패턴1;

public class Employee extends Person {

	@Override
	public void doSomething() {
		// TODO Auto-generated method stub
		System.out.println("입실체크한다.");
		System.out.println("일을 한다.");
		System.out.println("점심을 먹는다.");
		System.out.println("퇴실체크한다.");
	}

}
