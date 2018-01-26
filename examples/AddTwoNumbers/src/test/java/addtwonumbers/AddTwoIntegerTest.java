package addtwonumbers;


import org.junit.Test;

import static org.junit.Assert.*;


public class AddTwoIntegerTest 
{
	@Test
    public void test01( ){
    	Integer x= AddTwoInteger.AddTwoNumbers(10, 3);
    	assertEquals(new Integer(13),x);	
    }
	@Test
    public void test02( ){
		try{
			Integer x= AddTwoInteger.AddTwoNumbers(null, null);
		    fail("Fail:n1 and n2 should not be null");
		}catch (NullPointerException e){
			System.err.println("catch: n1 and n2 must not equall to Null\n");
			
		}
    }
}
