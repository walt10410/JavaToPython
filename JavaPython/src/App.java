
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class App {
    
    public static void main(String[] args) throws Exception {
        try{
        ProcessBuilder builder = new ProcessBuilder("python", "-u" System.getProperty("user.dir") + "/PythonScripts/HMITests.py", "HMI3", "HMI5");
        Process process = builder.start();
        // process.waitFor();
        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
        BufferedReader readerErrors = new BufferedReader(new InputStreamReader(process.getErrorStream()));

        String lines = null;
        while((lines = reader.readLine())!=null) {
            System.out.println("lines" +lines);
        }

         while((lines = readerErrors.readLine())!=null) {
            System.out.println("Error lines" +lines);
        }

    } catch(Exception e) {
        e.printStackTrace();
        }
    }
}
