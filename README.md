



<h4 align="center">Django Implementation of Online Exam Center for Students</h4>


<p align="center">
  <a href="#description">Description</a> •
  <a href="#key-features">Key Features</a> •

</p>

![ main page screenshot](https://github.com/salarjf/zistiha/blob/master/Screenshots/mainpage.png)

## Description
Here is a website I had written it as the project manager of a startup in Iran. I have left the project from late 2016 so I am not supporting it anymore, but the backend is still the same as I left (just some features that are not working anymore!).
The main goal of website is to hold exams for students from different locations through their web browsers. Because of business constraints we were not able to set accounts for users, so we were tracing them through a set of cookies (which could get refreshed with designated routes). Website has also <b>payment</b> module connecting to a third-party service provider (similar to paypal for Iran). Because of synchronized exam  for all students, website should have performed well under huge requests number.


## Key Features

* <b>High performance </b> under overload condition needed. During certian periods of time (holding exam) website should have performed well. Many different considerations in different levels have been made for this purpose:
  - Putting  computation load on the client side with following principles of <a href='http://tutorials.jenkov.com/software-architecture/ria-architecture.html'>RIA</a> architecture 
  - Proper database structure
  - Indexing of data entities in database
 
  
* <b>Security</b>
  - Encoding JavaScript to avoid browser manipulations during exam 
  - DDOS attack
  - HTTPS connection was not feasible by the company constraints so a simple handshaking protocole developed in order to reasurance of connection
  
* <b> Timing </b>  
* <b> Payment Gateway </b>



## Contact
> GitHub [@salarjf](https://github.com/salarjf) &nbsp;&middot;&nbsp;
> Linkedin [@salarjafarlou](https://www.linkedin.com/in/salarjafarlou/)


