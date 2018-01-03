/**
*	CalendarUtil.java
**/

package calendar;


/**
*	A class containing utility methods that a calendar might
*	need to function
*	
**/
public class CalendarUtil {
	
	/** integers specifying the number of days in each month **/
	public static int DaysInMonth[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	
	/** static var used for February **/
	public static final int FEBRUARY = 1;

	/** 
	*	Get number of days in specified year and month
	*	
	*	@param year the year in integer form
	*	@param month the month in integer form (0 is January, etc...)
	*	@return the number of days in the specified month and year
	**/
	public static int NumDaysInMonth(int year, int month) {
		
		int baseDays = DaysInMonth[month];
	
		if(IsLeapYear(year) && (month == FEBRUARY)) {
				baseDays = baseDays + 1;
		}
	
		return baseDays;
	}
	/**
	*	Determines if the specified year is a Leap Year
	*	
	*	@param year the year
	*	@return true if the year is a Leap Year, false otherwise
	**/
	public static boolean IsLeapYear(int year) {
	//if the year is a multiple of 100, the year is a leap year if its also a multiple of 400
		if ((year % 100) == 0) {
			
			if((year % 400) == 0) {
				return true;
			}
			else{
				return false;
			}
		}
	
		//year is also leap year if multiple of 4
		if ((year % 4) == 0) {
			return true;
		}
		else{
			return false;
		}
	}
}
