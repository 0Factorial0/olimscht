//import libraries
package content;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Timer;
import java.util.TimerTask;

public class test extends JFrame implements ActionListener {
    
    //create elements
    private JButton buttonGet1, buttonGet2, buttonGet3, buttonMenu, buttonClose;
    private JTextArea outputArea;
    private static Timer timer;
    static int seconds = 0;
    
    public test(){
        
        //set value of elements
        super("Test Menu");
        setLayout(new BorderLayout());

        //button definitions
        buttonGet1 = new JButton("Windows");
        buttonGet1.addActionListener(this);
        buttonGet2 = new JButton("MacOS");
        buttonGet2.addActionListener(this);
        buttonGet3 = new JButton("Linux");
        buttonGet3.addActionListener(this);
        buttonMenu = new JButton("Test Menu 2");
        buttonMenu.addActionListener(this);
        buttonClose = new JButton("Exit Program");
        buttonClose.addActionListener(this);

        //timer definitions
        timer = new Timer();

        //set button positions in jpanels
        JPanel buttonPanel1 = new JPanel(new GridLayout(1, 3));
        buttonPanel1.add(buttonGet1);
        buttonPanel1.add(buttonGet2);
        buttonPanel1.add(buttonGet3);
        
        JPanel buttonPanel2 = new JPanel(new GridLayout(1,1));
        buttonPanel2.add(buttonClose);
        buttonPanel2.add(buttonMenu);

        //set text area for output
        outputArea = new JTextArea();
        JScrollPane scrollPane = new JScrollPane(outputArea);

        //set element positions
        add(buttonPanel1, BorderLayout.NORTH);
        add(scrollPane, BorderLayout.CENTER);
        add(buttonPanel2, BorderLayout.SOUTH);

        //set page properties
        setSize(640, 480);
        setVisible(true);
    }

    //getting event actions
    public void actionPerformed(ActionEvent e){
        
        //set command as null for now
        String command = "";

        //get push button events
        if(e.getSource() == buttonGet1){
            //speedtest for windows
            command = "content/speedtest/win/speedtest.exe";
        }else if(e.getSource() == buttonGet2){
            //speedtest for macOS
            command = "content/speedtest/mac/speedtest";
        }else if(e.getSource() == buttonGet3){
            //speedtest for archlinux
            command = "content/speedtest/linux/speedtest";
        }else if(e.getSource() == buttonMenu){
            //open test menu 2
            command = "java content/test2.java";
        }else if(e.getSource() == buttonClose){
            //button for closing the program
            System.exit(0);
        }

        //create a terminal and run the command
        try{
            //build a process terminal and give the command
            ProcessBuilder builder = new ProcessBuilder("bash", "-c", command);
            //connect error stream to this
            builder.redirectErrorStream(true);
            //start process with the given command
            Process process = builder.start();
            //get output stream
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            String line;
            //get the output to the textbox
            while ((line = reader.readLine()) != null){
                outputArea.append(line + "\n");
            }
        //print input output error
        } catch (IOException ex){
            ex.printStackTrace();
        }
    }

    //main method
    public static void main(String[] args) {
        //push execute function
        new test();
    }

    //timer function
    public static void killTimer(JTextArea outputArea){
        //create task
        TimerTask task;
        //define task
        task = new TimerTask(){
            private final int MAX_SECONDS = 360;
            @Override
            //define run function
            public void run(){
                //run for 100 seconds
                if(seconds < MAX_SECONDS){
                    System.out.println("Time Left: "+(MAX_SECONDS - seconds));
                    seconds++;
                }else{
                    //kill terminal
                    String command = "pkill -9 -f spider/crawler.py";
                    //create a terminal and run the command
                    try{
                        //build a process terminal and give the command
                        ProcessBuilder builder = new ProcessBuilder("bash", "-c", command);
                        //connect error stream to this
                        builder.redirectErrorStream(true);
                        //start process with the given command
                        Process process = builder.start();
                        //get output stream
                        BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
                        String line;
                        //get the output to the textbox
                        while ((line = reader.readLine()) != null){
                            outputArea.append(line + "\n");
                        }
                    //print input output error
                    }catch(IOException ex){
                        ex.printStackTrace();
                    }
                    // stop the timer
                    cancel();
                }
            }
        };
        timer.schedule(task, 1000, 1000);
    }
}
