
/*
 * TimeTable.java
 *
 */
package calendar;
/**
 * 
* This class collects appointments between given two dates.
* 
*/

import java.util.*;


public class TimeTable {

	
    public TimeTable() {

    }
	
    
    /**
     * Retrieves a range of appointments between two dates.
     * @return A list of all of the CalDays between firstDate (inclusive)
     *  and lastDate (exclusive) with their respective appointments. 
     * @throws DateOutOfRangeException If any of the days constructed by the
     *  given values are invalid, or if lastDay is not after firstDay.
     **/
	  public LinkedList<CalDay> getApptRange(LinkedList<Appt> appts,GregorianCalendar firstDay, GregorianCalendar lastDay)throws DateOutOfRangeException{
		  
		     //Create a linked list of calendar days <CalDay> to return
	        LinkedList<CalDay> calDays = new LinkedList<CalDay>();
	     

	        
	        //Make sure that the first day is before the last day
	        if (!firstDay.before(lastDay)) {
	        	throw new DateOutOfRangeException ("Second date specified is not  before the first date specified.");
	        }
	        
	        
	        //Create the first CalDay object with the starting date and add to list
	        GregorianCalendar nextDay = (GregorianCalendar) firstDay.clone();
	        while (nextDay.before(lastDay)) {

	            calDays.add(new CalDay(nextDay));
	            nextDay.add(nextDay.DAY_OF_MONTH, 1);
	        }
	        
	        //Retrieve the appts - <appt> 
		for (int i = 0; i < appts.size(); i++) {
			Appt appt=appts.get(i);
			if(!appt.getValid()) continue;
			// Figure out which days the appointment occurs on
			LinkedList<GregorianCalendar> apptOccursOnDays = getApptOccurences(
					appt, firstDay, lastDay);

			// For each day in the list, calculate the difference between the
			// first day and the day of occurrence and add the appointment to
			// the correct CalDay
			int daysDifference = 0;
			nextDay = (GregorianCalendar) firstDay.clone();
			Iterator<GregorianCalendar> itr = apptOccursOnDays.iterator();
			while (itr.hasNext()) {
				GregorianCalendar apptOccursOn = (GregorianCalendar) itr.next();

				while (nextDay.before(apptOccursOn)) {
					daysDifference++;
					nextDay.add(nextDay.DAY_OF_MONTH, 1);
				}

				CalDay calDayOfAppt = (CalDay) calDays.get(daysDifference);
				calDayOfAppt.addAppt(appt);

			}

		}
		  return calDays;
	  }
	   /**
	     * This takes the given appointment and constructs a linked list of 
	     * GregorianCalendar's, each of which represent a day when the appointment
	     * occurs. The days are guaranteed to be between firstDay (inclusive) and
	     * lastDay (exclusive). They are guaranteed to be in order.
	     **/
	    private static LinkedList<GregorianCalendar> getApptOccurences(Appt appt, 
	        GregorianCalendar firstDay, GregorianCalendar lastDay) {
	        
	        LinkedList<GregorianCalendar> result = new LinkedList<GregorianCalendar>();
	        
	        //Make sure that the firstDay is before the last day
	        if (!firstDay.before(lastDay)) {
	            return result;
	        }
	        
	        //Get the first recurrence taken care of
	        GregorianCalendar occurrenceDay = 
	                new GregorianCalendar(appt.getStartYear(), appt.getStartMonth(), 
	                    appt.getStartDay());
	        
	        //If the first occurrence is after the last day, then it doesn't matter
	        //when it recurs because those dates must be after the last day too
	        if (!occurrenceDay.before(lastDay)) {
	            return result;
	        }
	        
	            

	            //Make sure that there is a limited number of recurrences
	            for (int i = 0; i < appt.getRecurNumber()+1; i++) {
	                
	                //Add the day of occurrence to the list if it is after the first day
	                if (!occurrenceDay.before(firstDay)) {
	                    result.add(occurrenceDay);
	                }
	                
	                //Calculate the next recurrence day
	                occurrenceDay = getNextApptOccurrence(appt, occurrenceDay);
	                if (occurrenceDay == null) {
	                    break;
	                }
	                            
	                //Keep cycling while the occurence day is in range
	                if (!occurrenceDay.before(lastDay)) {
	                    break;
	                }
	            }        
	        return result;
	    }
	    /**
	     * Calculates the next recurring day in the given appointment. If the 
	     * appointment does not recur it returns null. If the date cannot be 
	     * calculated for some reason it returns null.
	     **/
	    private static GregorianCalendar getNextApptOccurrence(Appt appt, 
	            GregorianCalendar day) {
	        //If the appointment does not recur then return null
	        if (!appt.isRecurring()) {
	            return null;
	        }	        
	        //Leave the original day untouched.
	        GregorianCalendar nextDay = (GregorianCalendar)day.clone();
	        
	        //This depends on the recurrence settings
	        switch (appt.getRecurBy()) {
	            case Appt.RECUR_BY_WEEKLY:
	                int[] recurDays = appt.getRecurDays();
	                
	                //If the user specified weekly recurrence and didn't specify
	                //which week days, then assume it is the same week day of the
	                //first occurrence
	                if (recurDays.length == 0) {
	                    //Add 7 days and return that by default
	                    nextDay.add(nextDay.DAY_OF_MONTH, 7);
	                    return nextDay;
	                }
	                
	                //The user did specify weekly recurrence, so increment the
	                //day until it falls on a weekday the user specified
	                for (int k = 0; k < 7; k++) {
	                    nextDay.add(nextDay.DAY_OF_MONTH, 1);
	                    int newDayOfWeek = nextDay.get(nextDay.DAY_OF_WEEK);
	                
	                    for (int i = 0; i < recurDays.length; i++) {
	                        //If the calendar is set to a day of the week that the
	                        //appt recurs on then return that day.
	                        if (recurDays[i] == newDayOfWeek) {
	                            return nextDay;
	                        }
	                    }
	                }
	                
	                //The loop above should have found a day. If the program 
	                //execution is here then the weekdays specified are not in the
	                //range of valid Gregorian Calendar Days. Return null here.
	                return null;
	            case Appt.RECUR_BY_MONTHLY:
	                //Just increment the month and return the day. Not sure what
	                //happens when the day is 31 and the next month has 30 days...
	                nextDay.add(nextDay.MONTH, 1);
	                return nextDay;
	            case Appt.RECUR_BY_YEARLY:
	                //Just increment the year. The only possible problem is an 
	                //appointment that recurs on February 29.
	                nextDay.add(nextDay.YEAR, 1);
	                return nextDay;
	        }
	  
	        return null;
	    }

	    
	    /**
	     * Deletes the appointment's information from the appointments data list. 
	     * @return updated list of appointments if the appointment is deleted successfully, otherwise null.
	     **/
	    public LinkedList<Appt> deleteAppt(LinkedList<Appt> appts,Appt appt) {
	    	//Do not do anything to appts equals to null 
	        if(appts==null||appt==null)
        		return null;
	    	//Do not do anything to invalid appointments
	        if (!appt.getValid()) {
	            return null;
	        }

	        //Remove the appointment from the list appts if applicable
	        
	        for(int i=1;i<appts.size()-1;i++){
	        	Appt tempAppt=appts.get(i);
	        	if(tempAppt.equals(appt)){
	        		appts.remove(i);
	        		return appts;
	        	}
	        		
	        }
	        return null;
	    }
	    
	    public LinkedList<Appt> permute(LinkedList<Appt> appts, int[] pv){
	    	/* pv is an array of integers that specify a permutation (a
	    	   rearrangement or shuffling) of the appointments
	    	   
	    	   If the ith element of pv is k, then the ith element of 
	    	   appointments should be placed in the kth position.
	    	*/
	    	LinkedList<Appt> apptsUpdatedList=new LinkedList<Appt>(appts);   
	    	if(pv.length != appts.size())
	    	    throw new IllegalArgumentException();

	    	int nexti =  0;
	    	for(int i = 0;i<pv.length;i++){
	    	    int newi = pv[nexti];
	    	    newi = pv[nexti];
	    	   Collections.swap(apptsUpdatedList,newi,newi);
	    	   nexti = newi;
	    	} 
     		return apptsUpdatedList;

	        }

}
