import java.awt.geom.Rectangle2D;
import java.io.File;
import java.io.IOException;

import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.PDPage;
import org.apache.pdfbox.text.PDFTextStripperByArea;

//import org.apache.pdfbox.multipdf.Splitter;
//import java.io.IOException;
//import java.util.List;
//import java.util.Iterator;

public class ExtractText {

    public static void main(String[] args) throws IOException {


        // Parameters
        String filepath = args[0];

        int x = 350;
        int y = 140;
        int width = 150;
        int height = 5;

        PDDocument document = PDDocument.load(new File(filepath));

        PDFTextStripperByArea textStripper = new PDFTextStripperByArea();
        Rectangle2D rect = new java.awt.geom.Rectangle2D.Float(x, y, width, height);
        textStripper.addRegion("region", rect);


        int pageNum = 0;
        int startPageNum = 1;
        String previousInvoice = new String("");
        int last_page_no = document.getNumberOfPages();
        int last_page_saved = 0;


        for( PDPage page : document.getPages() ) {
            textStripper.extractRegions(page);

            String textForRegion = textStripper.getTextForRegion("region");
            textForRegion = textForRegion.replace("\n", ""); 
            textForRegion = textForRegion.replace("Invoice Number", ""); 

            if(!previousInvoice.equals(textForRegion)) {
                if(!previousInvoice.equals("")) {
                    System.out.println("Save " + previousInvoice + " start " + startPageNum + " end " + pageNum);
                    PDDocument ndocument =  new PDDocument();
                    for(int i = startPageNum; i < pageNum; i++) {
                        ndocument.addPage(document.getPage(i));
                    }
                    ndocument.save("/home/vikas/projects/testing_env/testfiles/radio_pdfs/"+previousInvoice + ".pdf");
                    ndocument.close();
                    last_page_saved = pageNum;
                }
                previousInvoice = textForRegion;
                startPageNum = pageNum;
            }
            System.out.println(pageNum + "-'" + textForRegion + "'");
            pageNum++;
        }
        PDPage page1 = document.getPages().get(pageNum-1);
        textStripper.extractRegions(page1);
        String textForRegion = textStripper.getTextForRegion("region");
        textForRegion = textForRegion.replace("\n", ""); 
        textForRegion = textForRegion.replace("Invoice Number", ""); 
        PDDocument ndocument =  new PDDocument();
        System.out.println("last page saved "+ last_page_saved);
        System.out.println("Save "+textForRegion+" start "+(pageNum-1)+" end "+last_page_no);
        for(int i = last_page_saved; i < last_page_no; i++) {
                ndocument.addPage(document.getPage(i));
                }
        ndocument.save("/home/vikas/projects/testing_env/testfiles/radio_pdfs/"+textForRegion + ".pdf");
        ndocument.close();

    }
}
