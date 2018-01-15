/*
 * Appt.java
 */

package calendar;

import java.util.Comparator;


/**
 *  This class represents a single appointment that might be stored in
 *  a timetable.  The appointment consists of startHour, startMinute,
 *   startDay, startMonth, startYear, title, and description
 *   
 *   
 */
/**
 * Stores the data of an appointment
 */
public class Appt implements  Comparable<Appt>{
    
    /** Used for knowing whether or not an appointment is valid or not */
    private boolean valid;
    
	/** The starting hour of the appointment */
    private int startHour;
    
    /** The starting minute of the appointment */
    private int startMinute;
    
    /** The starting day of the appointment */
    private int startDay;
    
    /** The starting month of the appointment */
    private int startMonth;
    
    /** The starting year of the appointment */
    private int startYear;

    /** The title or caption of the appointment */
    private String title;

    /** The description of the appointment */
    private String description;
    
    /** Used for setting appointments to recur weekly */
    public static final int RECUR_BY_WEEKLY = 1;
    
    /** Used for setting appointments to recur monthly */
    public static final int RECUR_BY_MONTHLY = 2;
    
    /** Used for setting appointments to recur yearly */
    public static final int RECUR_BY_YEARLY = 3;
    
    /** Used for setting appointments to recur forever */
    public static final int RECUR_NUMBER_FOREVER = 1000;
    
    /** Used for setting appointments to never recur */
    public static final int RECUR_NUMBER_NEVER = 0;
    /** Day(s) of the week that the appointment recurs on */
    private int[] recurDays;
    
    /** What the appointment recurs on (weeks/months/years) */
    private int recurBy;
    
    /** How often the appointment recurs on (every ? weeks/months/years) */
    private int recurIncrement;
    
    /** How many recurrences (-1 for infinite, 0 by default) */
    private int recurNumber;

    // ----------------------------------------------------------
    /**
     * Constructs a new appointment that starts at a specific time on the 
     * date specified. The appointment is constructed with no recurrence 
     * information by default. To set recurrence information, construct the
     * appointment and then call setRecurrence(...) method.
     * @param startHour The hour that the appointment starts on. The hours are
     *      numbered 0-23 to represent 12a.m. to 11pm on the day specified.
     * @param startMinute The minute of the hour the appointment starts on.
     * @param startDay The day of the month the appointment starts on.
     * @param startMonth The month of the year the appointment starts on.
     * @param startYear The year the appointment starts on.
     * @param title The title or caption to give the appointment
     * @param description The appointment's details
     */
    public Appt(int startHour, int startMinute, 
            int startDay, int startMonth, int startYear,String title, String description)
    {
        //Sets all instance variables 
    	this.startHour = startHour;
    	this.startMinute = startMinute; 
    	this.startDay = startDay; 
    	this.startMonth = startMonth;
    	this.startYear = startYear; 
        setTitle(title);
        setDescription(description);
   
        //Set default recurring information
        int[] recurringDays = new int[0];
        setRecurrence(recurringDays, RECUR_BY_MONTHLY, 0, RECUR_NUMBER_NEVER);

        
        isValid();
    }


  
    /**
     * @sets valid to true if the appointment is valid
     */
    private void isValid() {
    	int NumDaysInMonth= CalendarUtil.NumDaysInMonth(startYear,startMonth-1);
    				
    	if(startHour<0 || startHour>23)
    		this.valid=false;
    	else
        	if(startMinute<0 || startMinute>59)
        		this.valid=false;
        	else
            	if(startDay<1 || startDay>NumDaysInMonth)
            		this.valid=false;
            	else
                	if(startMonth<1 || startMonth>12)
                		this.valid=false;
                	else
                		this.valid=true;
    }
    


    /** Sets startHour */
    public void setStartHour(int startHour) {
    	this.startHour = startHour;
    	 isValid();
    }
    
    /** Sets startHour */
    public void setStartMinute(int startMinute) {   	
        this.startMinute = startMinute;
        isValid();
    }

    /** Sets startDay */
    public void setStartDay(int startDay) {
        this.startDay = startDay;
        isValid();
    }
    
    /** Sets startMonth */
    public void setStartMonth(int startMonth) {
        this.startMonth = startMonth;
        isValid();
    }
    
    /** Sets startYear */
    public void setStartYear(int startYear) {
        this.startYear = startYear;
        isValid();
    }

    /** Sets title */
    public void setTitle(String title) {
        if (title == null) 
            this.title = "";
        else
            this.title = title;
    }
    
    /** Sets description */
    public void setDescription(String description) {
        if (description == null)
            this.description = "";
        else
            this.description = description;
    }
 
    
    /** Gets startHour */
    public int getStartHour() {
        return startHour;
    }
    
    /** Gets startHour */
    public int getStartMinute() {
        return startMinute;
    }
    
    /** Gets startDay */
    public int getStartDay() {
        return startDay;
    }
    
    /** Gets startMonth */
    public int getStartMonth() {
        return startMonth;
    }
    
    /** Gets startYear */
    public int getStartYear() {
        return startYear;
    }
 
    /** Gets title */
    public String getTitle() {
        return title;
    }
    
    /** Gets description */
    public String getDescription() {
        return description;
    }
    /** Gets description */
    public boolean getValid() {
        return this.valid;
    }
    /**
     * Sets the recurring information with the correct information
     */
    public void setRecurrence(int[] recurDays, int recurBy, int recurIncrement, int recurNumber) {
        setRecurDays(recurDays);
        setRecurBy(recurBy);
        setRecurIncrement(recurIncrement);
        setRecurNumber(recurNumber);
    }
    private void setRecurDays(int[] recurDays) {
        if (recurDays == null) {
            this.recurDays = new int[0];
        }
        else {
            this.recurDays = recurDays;
        }
    }
    /** Sets recurBy */
    private void setRecurBy(int recurBy) {
        this.recurBy = recurBy;
    }
    /** Sets recurIncrement */
    private void setRecurIncrement(int recurIncrement) {
        this.recurIncrement = recurIncrement;
    }
    
    /** Sets recurNumber */
    private void setRecurNumber(int recurNumber) {
        this.recurNumber = recurNumber;
    }
    /** Gets recurNumber */
    public int getRecurNumber() {
        return recurNumber;
    }
    /** Gets recurBy */
    public int getRecurBy() {
        return recurBy;
    }
    /** Gets recurDays */
    public int[] getRecurDays() {
        return recurDays;
    }    
    /**
     * Checks to see if an appointment recurrs or not
     * @return True if the appointment does occur more than once
     */
    public boolean isRecurring() {
        return getRecurNumber() != RECUR_NUMBER_NEVER;
    }
    /** Gets recurIncrement */
    public int getRecurIncrement() {
        return recurIncrement;
    }   
    // ----------------------------------------------------------
    /**
     * Generate a string representation for this appointment, with the
     * form "11am: dentist" or "2:00pm: class".  The string consists of the
     * 12-hour time representation with a (lower case) "am" or "pm"
     * designator, followed by a colon and space, and then the appointment
     * description.
     * @return a printable representation of this appointment
     */
    private String represntationApp(){
        String half = (getStartHour() > 11) ? "pm" : "am";
        int printableHour = getStartHour();
        if (printableHour > 11)
        {
            printableHour -= 12;
        }
        if (printableHour == 0)
        {
            printableHour = 12;
        }
        String represntationApp= printableHour +":"+ getStartMinute() + half;
        return represntationApp;
    	
    }
    public String toString()
    {
		if (!getValid()) {
		    return null;
		}
         String day= this.getStartMonth()+"/"+this.getStartDay()+"/"+this.getStartYear() + " at ";
        return "\t"+ day +  this.represntationApp()  + " ," +  getTitle()+ ", "+  getDescription()+"\n";
    }

 //   The compareTo() method is hard to explain, in integer sorting, just remember
 //   startMinute+startHour+day+month+year is ascending order.
	public int compareTo(Appt compareAppt) {
		int startMinute=	this.startMinute - ((Appt) compareAppt).getStartMinute();
		int startHour=	this.startHour - ((Appt) compareAppt).getStartHour();
		int day = this.getStartDay()-((Appt) compareAppt).getStartDay();
		int month = this.startMonth -((Appt) compareAppt).getStartMonth();
		int year = this.startYear -((Appt) compareAppt).getStartYear();


		//ascending order

		return startMinute+startHour+day+month+year;

	}


}
