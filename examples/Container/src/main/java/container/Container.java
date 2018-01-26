package container;

import java.util.LinkedList;

public class Container {
	
	private LinkedList<Integer> list = new LinkedList<Integer>();
	/* a constructor returns Container object*/
	public Container(){
		
	}
	/* returns 1 and adds n to the Container if n not in the Container, otherwise returns 0*/
	public int put(int n){
		if(!list.contains(n)){
			list.add(n);
			return 1;
		}
			
		return 0;		
	}
    /*returns 1 if n is in the Container, 0 otherwise*/
	public int get(int n){
		if(list.contains(n))
			return 1;
		
		return 0;
	}
	/* returns 1 if n was in the Container; after return n is not in the Container! */
	public int remove(int n){
		if(list.contains(n)){
			list.remove(list.indexOf(n));
			//list.removeFirstOccurrence(n);
			return 1;
		}
		return 0;
		
	}
	/* returns the number of elements in this Container.*/
	public int size(){
		return list.size();
	}

	public void printContainer() {
	        
	     for(int i=0;i<list.size();i++)
       		 	System.out.print(list.get(i)+", ");
	     System.out.println();

	}
}
