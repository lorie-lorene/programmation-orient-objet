import game.*;
import java.util.ArrayList;
import java.util.Random;
//import java.util.List;

public class Cat_game{
	private static int size = 10;

	// function to print a line corresponding to the size of a matrice
	private static void print_line(int size){
		for(int i= 0; i< size * 4.2; i++) // 4.2 represents the number of '-' per cell
			System.out.print("-");
		System.out.println();
	}

	// function to print the map
	private static void print_grid(int[][] grid, ArrayList<Cat> c, ArrayList<Mouse> m){				   
		System.out.println("\033\143"); // Code to clear the screen
		System.out.print("\n\t\t");
		print_line(grid.length);
		for(int i = 0; i < grid.length; i++){
			System.out.print("\t\t|");
			for(int j = 0; j < grid.length; j++){
				if(grid[i][j] == 0)
					System.out.print("   |");
				else if(grid[i][j] == 1)
					System.out.print(" O |");
				else if(grid[i][j] == 2)
					System.out.print(" o |");
				else if(grid[i][j] == 3)
					System.out.print(" x |");
				else if(grid[i][j] == 4)
					System.out.print(" × |");
				else if(grid[i][j] == 5)
					System.out.print(" . |");
			}
			System.out.print("\n\t\t");
			print_line(grid.length);
		}
		System.out.println("\nKey :");
		System.out.println("\t'O' = male cat, 'o' = female cat, 'x' = male mouse, '×' = female mouse, '.' = maize");
		System.out.println("\n\n");
		for(int i = 0; i < c.size(); i++){
			if(c.get(i).isAlive)
				System.out.print("cat"+(i+1)+" TTL = "+c.get(i).TTL+"\t");
		}
		System.out.println("\n\n");
		for(int i = 0; i < m.size(); i++){
			if(m.get(i).isAlive)
				System.out.print("mouse"+(i+1)+" TTL = "+m.get(i).TTL+"\t");
		}
		System.out.println("\n");
		//while waiting to implement threads, i will sleep the following way.
		long i=0,x;
		while(i<32000){x = 0;while(x<i){x++;}i++;}
	}
	public static void main(String[] args){
		Random rand = new Random();
		int[][] grid = new int[size][size];
		int pos[] = new int[2], x;
		ArrayList<Mouse> m = new ArrayList<>() ;
		ArrayList<Cat> cat = new ArrayList<>();
		ArrayList<Maize> mais = new ArrayList<>();

		for(int i = 0; i < 5; i++){
			pos[0] = rand.nextInt(size);
			pos[1] = rand.nextInt(size);
			while(grid[pos[0]][pos[1]] != 0){
				pos[0] = rand.nextInt(size);
				pos[1] = rand.nextInt(size);
			}
			x = rand.nextInt();
			if(x<=0)
				cat.add(new Cat(1,pos,grid));
			else
				cat.add(new Cat(2, pos, grid));
		}

		for(int i = 0; i < 5; i++){
			pos[0] = rand.nextInt(size);
			pos[1] = rand.nextInt(size);
			while(grid[pos[0]][pos[1]] != 0){
				pos[0] = rand.nextInt(size);
				pos[1] = rand.nextInt(size);
			}

			m.add(new Mouse(rand.nextInt(2)+3, pos, grid));
		}

		for(int i = 0; i < 5; i++){
			pos[0] = rand.nextInt(size);
			pos[1] = rand.nextInt(size);
			while(grid[pos[0]][pos[1]] != 0){
				pos[0] = rand.nextInt(size);
				pos[1] = rand.nextInt(size);
			}
			mais.add(new Maize(pos,grid));
		}

		int j;
		while(true){
			for(int i = 0; i < cat.size(); i++){
				if(cat.get(i).isAlive){
					j = -1;
					j = cat.get(i).reproduce(cat,grid);
					print_grid(grid, cat, m);
					if(j != -1){
						grid[cat.get(i).pos[0]][cat.get(i).pos[1]] = cat.get(i).gender;
						grid[cat.get(j).pos[0]][cat.get(j).pos[1]] = cat.get(j).gender;
						print_grid(grid, cat, m);
					}
					cat.get(i).move(grid);
					cat.get(i).eat(m);
					print_grid(grid, cat, m);
				}
			}

			for(int i = 0; i < m.size(); i++){
				if(m.get(i).isAlive){
					j = -1;
					j = m.get(i).reproduce(m,grid);
					print_grid(grid, cat, m);
					if(j != -1){
						grid[m.get(i).pos[0]][m.get(i).pos[1]] = m.get(i).gender;
						grid[m.get(j).pos[0]][m.get(j).pos[1]] = m.get(j).gender;
						print_grid(grid, cat, m);
					}
					m.get(i).move(grid);
					m.get(i).eat(mais);
					print_grid(grid, cat, m);
				}
			}
		}

	}

}
