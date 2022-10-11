import java.util.Arrays;

public class PermProdCombHomoSubs {
	static int N=5, R=3, C;
	static int[] a = {1, 2, 3, 4, 5};
	static boolean[] v = new boolean[N];
	static int[] b = new int[R];
	
	public static void main(String[] args) {
		C = 0;
		perm(0); // 4P3 순열 (Permutation): 순서중요(123!=321), 중복미허용
		System.out.println(C);
		System.out.println();
		
		C = 0;
		prod(0); // 4ㅠ3 중복순열 (Product): 순서중요(123!=321), 중복허용
		System.out.println(C);
		System.out.println();
		
		C = 0;
		comb(0, 0); // 4C3 조합 (Combination): 순서미중요(123==321), 중복미허용
		System.out.println(C);
		System.out.println();
		
		C = 0;
		homo(0, 0); // 4H3=4+3-1C3=6C3중복조합 (homogeneous): 순서미중요(123==321), 중복허용
		System.out.println(C);
		System.out.println();
		
		C = 0;
		subs(0); // 2^n 부분집합(subset) 
		System.out.println(C);
		System.out.println();
	}
	
	static void perm(int depth ) {
		if(depth == R) {
			System.out.println(Arrays.toString(b));
			C++;
			return;
		}
		
		for(int i = 0; i <N; i++) {
			if(!v[i]) {
				v[i] = true;
				b[depth] = a[i];
				perm(depth+1);
				v[i] = false;
			}
		}
	}
	static void prod(int depth ) {
		if(depth == R) {
			System.out.println(Arrays.toString(b));
			C++;
			return;
		}
		
		for(int i = 0; i <N; i++) {
			//if(!v[i]) {
				//v[i] = true;
				b[depth] = a[i];
				prod(depth+1);
				//v[i] = false;
			}
		}
	static void comb(int depth, int start) {
		if(depth == R) {
			System.out.println(Arrays.toString(b));
			C++;
			return;
		}
		
		for(int i = start; i < N; i++) {
			b[depth] = a[i];
			comb(depth+1, i+1);
		}
	}
	static void homo(int depth, int start) {
		if(depth == R) {
			System.out.println(Arrays.toString(b));
			C++;
			return;
		}
		
		for(int i = start; i < N; i++) {
			b[depth] = a[i];
			homo(depth+1, i);
		}
	}
	static void subs(int depth) {
		if(depth == N) {
			//System.out.println(Arrays.toString(v));
			for(int i = 0; i < N; i++) System.out.print(v[i]?a[i]:"X");
			System.out.println();
			C++;
			return;
		}
		
		for(int i = 0; i < 1; i++) {
			v[depth] = true;
			subs(depth+1);
			v[depth] = false;
			subs(depth + 1);
		}
	}
}
