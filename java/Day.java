import java.util.LinkedList;

public class Day{ 
    public String date;
    public Day node;
        public Day(String date, Day node ){ 
       
            this.date=date;
            this.node=node;
        }
        public static void add_Menu(Day node,Menu food_data){ 
            Menu pt=new Menu();
            if (node==null){
                node=food_data;
            }
            else { 
                pt = node;
                while(pt.next_f!=null){
                        pt= pt.next_f;
                        pt.next_f= food_data;
                }
            }

        }
    
}