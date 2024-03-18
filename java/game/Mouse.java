package game;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Queue;
import java.util.Random;

public class Mouse{
	public boolean isAlive;
	public int  gender, pos[] = new int[2], TTL, Total_moves;
	private final int d_row[] = {1, -1, 0, 0, 1, 1, -1, -1}, d_column[] = {0, 0, 1, -1, 1, -1, 1, -1};

	public Mouse(int gender, int[] position, int[][] map){
		this.gender = gender; // either 3 for male or 4 for female
		this.pos[0] = position[0];
		this.pos[1] = position[1];
		map[this.pos[0]][this.pos[1]] = this.gender;
		this.TTL = 5;
		this.Total_moves = 0;
		this.isAlive = true;
	}

	private int minDistance(int[][] grid, int row, int col){
		QItem source = new QItem(row, col, 0);

		// Applying BFS on matrix cells starting from source
		Queue<QItem> queue = new LinkedList<>();
		queue.add(new QItem(source.row, source.col, 0));
		boolean[][] visited = new boolean[grid.length][grid.length];
		visited[source.row][source.col] = true;

		while(queue.isEmpty() == false){
			QItem p = queue.remove();

			if(grid[p.row][p.col] == 5) // 5 represents the maize
				return p.dist;
			
			// moving up
			if(isvalid(p.row - 1, p.col, grid, visited)){
				queue.add(new QItem(p.row-1, p.col, p.dist+1));
				visited[p.row-1][p.col] = true;
			}

			// moving down
			if(isvalid(p.row + 1, p.col, grid, visited)){
				queue.add(new QItem(p.row+1, p.col, p.dist+1));
				visited[p.row+1][p.col] = true;
			}

			// moving left
			if(isvalid(p.row, p.col - 1, grid, visited)){
				queue.add(new QItem(p.row, p.col - 1, p.dist+1));
				visited[p.row][p.col - 1] = true;
			}

			// moving right
			if(isvalid(p.row, p.col + 1, grid, visited)){
				queue.add(new QItem(p.row, p.col+1, p.dist+1));
				visited[p.row][p.col +1] = true;
			}
		}
		return -1;
	}

	public void move(int[][] grid){
		int dist;
		int row, column;

		if(this.TTL == 0){
			grid[this.pos[0]][this.pos[1]] = 0;
			this.isAlive = false;
		}
		if(this.isAlive){
			dist  = this.minDistance(grid, this.pos[0], this.pos[1]);

			for(int i = 0; i< 4; i++){
				row = this.pos[0] + d_row[i];
				column = this.pos[1] + d_column[i];

				if(row < 0 || column < 0) continue;
				if(row >= grid.length || column >= grid.length) continue;
				if(grid[row][column] == 1 || grid[row][column] == this.gender || grid[row][column] == 2) continue;

				if(this.minDistance(grid, row, column) == dist - 1){
					grid[this.pos[0]][this.pos[1]] = 0;
					grid[row][column] = this.gender;
					this.pos[0] = row;
					this.pos[1] = column;
					this.TTL--;
					this.Total_moves++;
					break;
				}
			}
		}
	}

 	private boolean isvalid (int row, int column, int[][] map, boolean[][] visited){
		boolean result = false;
		// check if cell is in the bounds of the matrix
		if (row >= 0 && row < map.length  && column >= 0 && column < map.length && visited[row][column] == false)
			//check if cell is not blocked and not previously tried
			if (map[row][column] == 0 || map[row][column] == 5)
	 			result = true;
		return result;

	}

	public void eat(ArrayList<Maize> m){
		if(this.isAlive){
			for(int i = 0; i < m.size(); i++){
				if(this.pos[0] == m.get(i).pos[0] && this.pos[1] == m.get(i).pos[1]){
					if(m.get(i).isAlive){
						m.get(i).isAlive = false;
						this.TTL += 4; //increases his lifetime by 3 when he eats
					}
				}
			}
		}
	}

	public int reproduce(ArrayList<Mouse> m, int[][] map){
		int j = -1, row, column, x, y;
		Random rand = new Random();
		
		for(int i = 0; i < m.size(); i++){
			if(this.isAlive){
				if(this.pos[0] == m.get(i).pos[0] && this.pos[1] == m.get(i).pos[1] && this.gender != m.get(i).gender){
					map[this.pos[0]][this.pos[1]] = 0;
					map[m.get(i).pos[0]][m.get(i).pos[1]] = 0;
					m.add(new Mouse(rand.nextInt(2)+3, this.pos , map));

					row = this.pos[0];
					column = this.pos[1];

					// the mouse moves to the next free adjacent cell
					for(int k = 0; k< 8; k++){
						x = row + d_row[k];
						y = column + d_column[k];
		
						if(x < 0 || y < 0) continue;
						if(x >= map.length || y >= map.length) continue;
						if(map[x][y] != 0) continue;

						this.pos[0] = x;
						this.pos[1] = y;
						break;
					}

					// his/her partner moves to the next free adjacent cell
					for(int k = 0; k< 8; k++){
						x = row + d_row[k];
						y = column + d_column[k];
		
						if(x < 0 || y < 0) continue;
						if(x >= map.length || y >= map.length) continue;
						if(map[x][y] != 0) continue;

						m.get(i).pos[0] = x;
						m.get(i).pos[1] = y;
						break;
					}

					j = i;
					break;
				}
			}
		}
		return j;
	}
}
