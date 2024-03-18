import java.util.LinkedList;
import java.util.Arrays;

public class Menu{
    public String date;
    public String[] food;
    public int nb_times;
    public float water_qty;
    public float qty_liquid;
    public boolean fruits_legumes;
    public int nb_bowel;
    public String health;
    public Menu next_f;

    public Menu(String date, String[] food, int nb_times,float  water_qty, float qty_liquid, boolean fruits_legumes, int nb_bowel, String health){ 
        this.date =date;
        this.food= food;
        this.nb_times=nb_times;
        this.water_qty=water_qty;
        this.qty_liquid=qty_liquid;
        this.fruits_legumes=fruits_legumes;
        this.nb_bowel=nb_bowel;
        this.health=health;
        this.next_f=null;
    }
    public String toString(){
        String val = "Date : "+this.date+"\nFood(s) : ";

        for (int i=0;i< food.length;i++){
            val += i+", ";
        
        val += "\nNb of times food eaten per day : "+this.nb_times+"\nQty of water drank : "+this.water_qty+"L\nQty of other liquid drank : "+this.qty_liquid+"L";
        
        if (this.fruits_legumes){
            val += "\nEating fruits and legumes : yes";
        }
        else{
            val += "\nEating fruits and legumes : no";
        }
        
        val+= "\nNb of bowel movements : "+this.nb_bowel+"\nHealth problems : "+this.health+"\n";
        
        return val;
        }
    } 
}      
