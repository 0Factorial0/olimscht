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

public class execute extends JFrame implements ActionListener{

    //create elements
    private JButton buttonRouter, buttonRequest, buttonRouter2, buttonClose;
    public JTextArea outputArea;
    private static Timer timer;
    static int seconds = 0;

    public execute(){

        //set values of elements
        super("Traffic Generator");
        setLayout(new BorderLayout());

        //button definitions
        buttonRouter = new JButton("Crawler Spider Menu");
        buttonRouter.addActionListener(this);
        buttonRouter2 = new JButton("Information Menu");
        buttonRouter2.addActionListener(this);
        buttonRequest = new JButton("Start Traffic");
        buttonRequest.addActionListener(this);
        buttonClose = new JButton("Exit Program");
        buttonClose.addActionListener(this);

        //timer definitions
        timer = new Timer();
       
        //set button positions in jpanels
        JPanel buttonPanel1 = new JPanel(new GridLayout(1, 3));
        buttonPanel1.add(buttonRouter);
        buttonPanel1.add(buttonRouter2);
        buttonPanel1.add(buttonClose);

        JPanel buttonPanel2 = new JPanel(new GridLayout(1, 1));
        buttonPanel2.add(buttonRequest);

        //set text area for output
        outputArea = new JTextArea();
        //make it not editable
        outputArea.setEditable(false);
        JScrollPane scrollPanel = new JScrollPane(outputArea);

        //set element positions
        add(buttonPanel2, BorderLayout.NORTH);
        add(scrollPanel, BorderLayout.CENTER);
        add(buttonPanel1, BorderLayout.SOUTH);

        //set page properties
        setSize(800, 600);
        setVisible(true);
    }

    //getting event actions
    public void actionPerformed(ActionEvent e){
        
        //set command as null for now
        String command = "";

        //get push button events
        if(e.getSource() == buttonRouter){
            //button for menu 2
            command = "java content/generate.java";
        }else if(e.getSource() == buttonRequest){
            //start timer
            killTimer(outputArea);
            //button for start request
            command = "python3 content/requester.py --list spider/link/links.txt";
        }else if(e.getSource() == buttonRouter2){
            //button for menu 2
            command = "java content/show.java";
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
            while((line = reader.readLine()) != null){
                outputArea.append(line + "\n");
            }
        //print input output error
        }catch(IOException ex){
            ex.printStackTrace();
        }
    }

    //main method
    public static void main(String[] args) {
        //push execute function
        new execute();
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
                    String command = "pkill -9 -f requester.py";
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
