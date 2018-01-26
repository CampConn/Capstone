# Lesson04: Think-piece
You are given a class, Container and the following methods signatures:

  public Container();/* a constructor returns Container object*/

  public int put(int n)/* returns 1 and adds n to the Container if n not in the Container, otherwise returns 0*/

  public int get(int n);/* returns 1 if n is in the Container, 0 otherwise */

  Public int remove(int n); /* returns 1 if n was in the Container; after return n is not in the Container! */

  public int size()/* returns the number of elements in this Container.*/

ContainerRandomTest.java contains the differential testing, and HashSet is used to assert the final results with the target file Container.

To run only ContainerTest.java:  mvn -Dtest=ContainerTest test

To run only ContainerRandomTest.java:  mvn -Dtest=ContainerRandomTest test

To run both: mvn test



