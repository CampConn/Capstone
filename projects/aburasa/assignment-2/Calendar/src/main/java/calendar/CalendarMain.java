package calendar;
/*
 * CalendarMain.java
 *  Adapted from  Paul Miles
 */
import java.util.Calendar;
import java.util.Collections;
import java.util.GregorianCalendar;
import java.util.LinkedList;




public class CalendarMain {
	public static void main(String[] args) throws DateOutOfRangeException {
        //Internal Diagnostic Messages turned on when true
		 boolean diagnose = true;

		/** Collection of all of the appointments for the calendar day */		
		LinkedList<Appt> listAppts = new LinkedList<Appt>();
		System.out.println("Calendar Main: \n" );
		
		
     	/** the month the user is currently viewing **/
     	int thisMonth;
    	
    	/** the year the user is currently viewing **/
    	 int thisYear;
    	
    	/** todays date **/
    	int thisDay;
    	
		//get todays date
    	Calendar rightnow = Calendar.getInstance();
    	//current month/year/date is today
    	thisMonth = rightnow.get(Calendar.MONTH)+1;
		thisYear = rightnow.get(Calendar.YEAR);
		thisDay = rightnow.get(Calendar.DAY_OF_MONTH);
		
		 int startHour=15;
		 int startMinute=30;
		 int startDay=thisDay+1;  	
		 int startMonth=thisMonth; 	
		 int startYear=thisYear; 	
		 String title="Birthday Party";
		 String description="This is my birthday party.";
		 //Construct a new Appointment object with the initial data	 
         Appt appt = new Appt(startHour,
                  startMinute ,
                  startDay ,
                  startMonth ,
                  startYear ,
                  title,
                 description);
          if(diagnose){
          	System.out.println(appt.toString());
          } 
         
         listAppts.add(appt);
          
      // create another appointment
         startHour=14;
		 startMinute=30;
		 startDay=thisDay;  	
		 startMonth=thisMonth; 	
		 startYear=thisYear; 	
		 title="Class";
		 description="Rescheduled class.";
		 //Construct a new Appointment object with the initial data	 
         appt = new Appt(startHour,
                  startMinute ,
                  startDay ,
                  startMonth ,
                  startYear ,
                  title,
                 description);
        
         if(diagnose){
         	System.out.println(appt.toString());
         }
         listAppts.add(appt);
         // create another appointment
         startHour=13;
		 startMinute=30;
		 startDay=thisDay;		
		 startMonth=thisMonth;	
		 startYear=thisYear;	
		 title="Meeting Today";
		 description="Meeting with the students.";
		 //Construct a new Appointment object with the initial data	 
         appt = new Appt(startHour,
                  startMinute ,
                  startDay ,
                  startMonth ,
                  startYear ,
                  title,
                 description);
         
         if(diagnose){
         	System.out.println(appt.toString());
         }
         listAppts.add(appt);
         // create another appointment
         startHour=16;
		 startMinute=30;
		 startDay=thisDay+1;		
		 startMonth=thisMonth+1;	
		 startYear=thisYear;	
		 title="Visit";
		 description="Visiting my parents!";
		 //Construct a new Appointment object with the initial data	 
         appt = new Appt(startHour,
                  startMinute ,
                  startDay ,
                  startMonth ,
                  startYear ,
                  title,
                 description);
         int[] recurDaysArr={2,3,4};
         appt.setRecurrence( recurDaysArr, Appt.RECUR_BY_WEEKLY, 2, Appt.RECUR_NUMBER_FOREVER);
        
         if(diagnose){
         	System.out.println(appt.toString());
         }
         listAppts.add(appt);
 		if(diagnose){
			System.out.println("The Appointments are not sorted!");
         	System.out.println(listAppts.toString());
	
            Collections.sort(listAppts);
			System.out.println("The Appointments are sorted!");
         	System.out.println(listAppts.toString());
            
 		
 		}



         
		//get a list of appointments for one day, which is today
		GregorianCalendar today = new GregorianCalendar(thisYear,thisMonth,thisDay);
		GregorianCalendar tomorrow = (GregorianCalendar)today.clone();
		tomorrow.add(Calendar.DAY_OF_MONTH,1);
		String todatDate=today.get(Calendar.MONTH)+ "/"+ today.get(Calendar.DAY_OF_MONTH)+"/"+today.get(Calendar.YEAR);
		String tomorrowDate=tomorrow.get(Calendar.MONTH)+ "/"+ tomorrow.get(Calendar.DAY_OF_MONTH)+"/"+tomorrow.get(Calendar.YEAR);

		if(diagnose){
			System.out.println("today is:" + todatDate);
			System.out.println("tomorrow is:" + tomorrowDate);
		}
		
		TimeTable timeTable=new TimeTable();
        //Create a linked list of calendar days to return
        LinkedList<CalDay> calDays = new LinkedList<CalDay>();

		
 		
		if (diagnose) {
	

			System.out.println("The number of appointments between "+ todatDate +" and " + tomorrowDate);
			calDays = new LinkedList<CalDay>();
			calDays = timeTable.getApptRange(listAppts, today, tomorrow);
			for (int i = 0; i < calDays.size(); i++)
				System.out.println(calDays.get(i).toString());
		}
		//delete a particular appointment from the list
		if(diagnose){
			System.out.println("Delete  "+ listAppts.get(2) );
		}
		LinkedList<Appt> listDeletedAppts=timeTable.deleteAppt(listAppts, listAppts.get(2));
		if(diagnose){
			System.out.println("The number of appointments:  "+ listDeletedAppts.size() );

		}
		if (diagnose) {
			System.out.println("The number of appointments between "+ todatDate +" and " + tomorrowDate);

			calDays = new LinkedList<CalDay>();
			calDays = timeTable.getApptRange(listAppts, today, tomorrow);
			for (int i = 0; i < calDays.size(); i++)
				System.out.println(calDays.get(i).toString());
		}
        System.exit(0);
		
	}
}
