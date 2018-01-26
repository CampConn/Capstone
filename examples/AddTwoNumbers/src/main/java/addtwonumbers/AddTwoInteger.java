package addtwonumbers;

//There are three states that your test case can end up in
//
//Passed : The function under test executed successfully and returned data as expected
//Not Passed : The function under test executed successfully but the returned data was not as expected
//Failed : The function did not execute successfully and this was not intended 

public class AddTwoInteger 
{
	public static Integer AddTwoNumbers(Integer n1, Integer n2){
		Integer x=null;
	// You need to comment out the following line to see the differences!
	//	if((n1==null)||(n2==null) ) throw new NullPointerException("return value is null at method AddTwoNumbers ");
		
		try {
				x= new Integer(n1+n2);

		} catch(NullPointerException e){
			System.err.println("Source Code:n1 and n2 must not equall to Null\n");
			
		}
		
	//	System.out.println("after catch statement");

		return x;
	}
	
	
	
}
