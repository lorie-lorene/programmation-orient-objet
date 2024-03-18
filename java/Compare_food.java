public class Compare_food{ 
    public List food;
    public List num;
    public Compare_food(){
        this.food=food;
        this.num=num;
    }
    for (int k=0;k< food.size();k++){ 
        this.food.add(i);
        this.num.add(1);
    }
        
    def add_food(self, food):
        for elt in food:
            if elt in self.food:
                i = self.food.index(elt)
                self.num[i]+=1
            else:
                self.food.append(elt)
                self.num.append(1)

}
