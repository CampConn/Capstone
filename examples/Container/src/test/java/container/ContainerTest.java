package container;
/**
 *  This class provides a basic set of test cases for the
 *  Container class.
 */
import org.junit.Test;

import static org.junit.Assert.*;

public class ContainerTest {
    /**
     * Test if  the put method returns 1 and adds n to the Container if n not in the Container, otherwise returns 0
     */
	 @Test
	  public void test01()   {
		 Container c=new Container();
		 int r=c.put(0);
		 assertEquals(1, r);
		 r=c.put(0);
		 assertEquals(0, r);
		 
	 }
	    /**
	     * Test that the get method returns 1 if n is in the Container, 0 otherwise
	     */
	 @Test
	  public void test02()   {
		 Container c=new Container();
		 int r=c.put(0);
		 r=c.get(0);
		 assertEquals(1, r);
    		
	 }	
	    /**
	     * Test that the remove method returns 1 if n was in the Container; after return n is not in the Container! .
	     */
	 @Test
	  public void test03(){
		 Container c=new Container();
		 int r=c.put(0);
		 r=c.remove(0);
		 assertEquals(1, r);
		 r=c.get(0);
		 assertEquals(0, r);	 		
	 }	
	 @Test
	  public void test04(){
		 Container c=new Container();
		 int r=c.put(0);
		 assertEquals(1, r);
		 assertEquals(1, c.size());
		 r=c.put(0);
		 assertEquals(0, r);	
		 r=c.put(1);
		 r=c.put(2);
		 r=c.put(3);
		 r=c.put(4);
		 r=c.put(5);
		 r=c.put(6);
		 r=c.put(7);
		 r=c.put(8);
		 r=c.put(9);
		 assertEquals(10, c.size());
		 
		 
		 
		 
		 
	 }
	
}
