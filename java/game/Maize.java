package game;

public class Maize{
    public int[] pos = new int[2];
    public boolean isAlive;
    public Maize(int[] position, int[][] grid){
        this.pos[0] = position[0];
        this.pos[1] = position[1];
        grid[this.pos[0]][this.pos[1]] = 5;
        this.isAlive = true;
    }
}