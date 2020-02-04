Nic Chiolerio

Assignment 3 - Requirements analysis


Users:
        1) Students
            -view assignments
            -view grades
            -turn in assignments
        
        2) TAs
            -grade assignments
            -comment on assignments
            -make announcements
        
        3) Instructors
            -create a course
            -everything a TA can do
            -create assignments
            -post assignments
            -add TA and student accounts to a course
        
        4) Non-instructor faculty
            -view course material
            
        5) All users
            -connect to email to message each other
            
            
            
Entities and attributes:
  1) Each user needs and account to log into the system
    -accounts would have username, email, password and permission attributes
    -permissions would determine what an account can do, like students can't grade assignments or post announcments, etc. think like canvas
  2) Assignments
    -an assignment would be a post for each student to turn in a file
    -assignments would have grades and instructor/TA comments
  
  3) Announcements
    -non assingment posts meant to convey information, can be posted by instructors or TAs
            
            
            
System requirements:
  -internet connectivity
  -a powerful enough machine for students to browse the web and upload completed assignments
  -a database to house all the students turned in assignments and all information associated with it, that staff can view
   and a student can view their own information
  -an email service to allow users to communicate if they need to before meeting in person again / if the class is online
