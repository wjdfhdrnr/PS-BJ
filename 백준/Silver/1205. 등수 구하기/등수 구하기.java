import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int score = sc.nextInt();
		int P = sc.nextInt();
		Integer[] score_box = new Integer[N];
		int rank = 1;
		
		
		for (int i = 0; i < N; i++) {
			score_box[i] = sc.nextInt();
		}
		Arrays.sort(score_box,Comparator.reverseOrder());
		
		if(N==P &&  score <= score_box[N-1]) {
			System.out.println(-1);
		}
		else {
			for(int i=0;i<N;i++) {
				if(score < score_box[i]) 
					rank +=1;
				
				else 
					break;
			}
			System.out.println(rank);
		}
		
	}
	}
