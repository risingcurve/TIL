package java05.array;

public class Array03_copy {
	public static void main(String[] args) {
		int[] arr = { 77, 50, 10, 12, 64, 15 };
		
		int[] tmp = new int[arr.length*2];
		// 셀프 (반복문을 이용해서 복사해 보기)
		
		int[] tmp2 = new int[arr.length*2];
		
		System.arraycopy(arr, 0, tmp2, 0, arr.length);
		
		System.out.println(Arrays.toString(tmp2));
	}
}
