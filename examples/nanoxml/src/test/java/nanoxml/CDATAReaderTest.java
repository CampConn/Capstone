package nanoxml;

import org.junit.Test;

import static org.junit.Assert.*;

public class CDATAReaderTest {
/*
	  @Test
	  public void test0()  throws Throwable  {
	      StdXMLReader stdXMLReader0 = (StdXMLReader)StdXMLReader.stringReader("M2{Ivt=OB$");
	      CDATAReader cDATAReader0 = new CDATAReader(stdXMLReader0);
	      char[] charArray0 = new char[6];
	      int int0 = cDATAReader0.read(charArray0, (int) 1, (int) 5);
	  }
*/	
	  @Test
	  public void test1()  throws Throwable  {
	      StdXMLReader stdXMLReader0 = (StdXMLReader)StdXMLReader.stringReader("]]>Ivt=OB$");
	      CDATAReader cDATAReader0 = new CDATAReader(stdXMLReader0);
	      char[] charArray0 = new char[6];
	      int int0 = cDATAReader0.read(charArray0, (int) 1, (int) 5);
	  }

	  @Test
	  public void test2()  throws Throwable  {
	      StdXMLReader stdXMLReader0 = (StdXMLReader)StdXMLReader.stringReader("]]1>Ivt=OB$");
	      CDATAReader cDATAReader0 = new CDATAReader(stdXMLReader0);
	      char[] charArray0 = new char[6];
	      int int0 = cDATAReader0.read(charArray0, (int) 1, (int) 5);
	  }
	  @Test
	  public void test3()  throws Throwable  {
	      StdXMLReader stdXMLReader0 = (StdXMLReader)StdXMLReader.stringReader("]]1>");
	      CDATAReader cDATAReader0 = new CDATAReader(stdXMLReader0);
	      char[] charArray0 = new char[6];
	      int int0 = cDATAReader0.read(charArray0, (int) 6, (int) 6);
	  }

	  @Test
	  public void test4()  throws Throwable  {
	      StdXMLReader stdXMLReader0 = (StdXMLReader)StdXMLReader.stringReader("]]>Ivt=OB$");
	      CDATAReader cDATAReader0 = new CDATAReader(stdXMLReader0);
	      char[] charArray0 = new char[6];
	      int int0 = cDATAReader0.read(charArray0, (int) 1, (int) 5);
		int0 = cDATAReader0.read(charArray0, (int) 1, (int) 5);
	  }

}
