# Entry Management System

Entry Management software (GUI application) with email and sms facility.
The software starts with the entry of the visitor email address which will be furthur used as a key to identify the visitor along with the email entry there are two buttons one for ***CheckIn*** and one for ***CheckOut***

***If **CheckIn** is pressed   :***
A form to fill the details appear in the frontend with a submit button whereas at the back end, once the user enters the information in the form, the backend should store all of the information with time stamp of the entry i.e checkin time. After clicking the Submit Button an email and an SMS should be triggered to the host informing him of the details of the visitor

***If **CheckOut** is pressed   :*** After validating the key the Checkout time if filled in the database and this should trigger an email to the guest with the complete form which should include:

* Name 
* Phone No
* Check-in time
* Checkout time
* Host name 
* Address visited.




## Prequisites

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required packages mentioned in reqirement.txt in my repository and run the following command in the command promt .

```bash
python -m pip install -r requirements.txt
```
**Note**-*Please read setup.txt file before running the code.*
## API and Language used

* Python
* Tkinter for GUI
* Twilio for SMS service
* SMTP for email service

## API requirements ##
* MySQL
* Python 3.6

## Account Requirements for API
* Twilio Account 
* Gmail Account 
 
## Reason to use above mentioned APIs over others 
#### Tkinter #### 
It is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

#### Twilio ####
Twilio is a cloud based service that enables powerful communication between mobile devices, applications, services, and systems.Twilio seeks to rid businesses of the messy telecom hardware by providing a telephony infrastructure web service via a globally available cloud API, allowing web developers to use standard web languages to integrate phone calls, text messages and IP voice communications into their web, mobile and traditional phone applications.

#### SMTP ####
If you want to use your own company "reply to" address. For example, if I want my messages to have a reply to address of help@paloalto.com, I can change that in the Mailbox setup but the problem is that those email messages are really coming from help@paloaltosoftware.emailcenterpro.com. The difference between the Reply To address and the real address can cause messages to be detected as spam or spoofed email messages. Setting up an SMTP connection so that email are sent through my @paloalto.com mail server

## Working video
Check the following video to see how  the software performs!
[Watch the video here](https://youtu.be/abjHnQS5038)

## Some Screenshots of UI

Start Screen of the Application where Visitor can check in and check out by entering the email address
![alt text](https://github.com/gautambhatia2502/Entry-Management-System/blob/master/images/new%20main.png)

Screen after user click the checkin button
![Check-Out Screen of the Software](https://github.com/gautambhatia2502/Entry-Management-System/blob/master/images/checkin.png)

## Database Columns entries:

![alt text](https://github.com/gautambhatia2502/Entry-Management-System/blob/master/images/database.png)

## Corner Test Cases taken care of:

1) If the user tries to checkin with invalid email address ( i.e just a text)

![alt text](https://github.com/gautambhatia2502/Entry-Management-System/blob/master/images/wrong_mail.png)


2) If the user tries to checkout without checking in

![alt text](https://github.com/gautambhatia2502/Entry-Management-System/blob/master/images/Checkout_without_checkin.png)



3) If the user is already checked in and and tries to checkin again

![alt text](https://github.com/gautambhatia2502/Entry-Management-System/blob/master/images/Already_checkedin.png)



4) The details will not get submitted until all the details are completely filled


## Email and SMS Screenshots
**Email host**

![alt text](https://github.com/gautambhatia2502/Entry-Management-System/blob/master/images/Visitor_info_mail.png)

**SMS host**

![alt text](https://github.com/gautambhatia2502/Entry-Management-System/blob/master/images/SMS.png)

**Email visitor**

![alt text](https://github.com/gautambhatia2502/Entry-Management-System/blob/master/images/Visit_report.png)



# Additional Feature
The software also has an export data to excel sheet option in the file menu in the navigation bar.What it does is to export all the data from mysql to MS Excel

![alt text](https://github.com/gautambhatia2502/Entry-Management-System/blob/master/images/New%20Main%202.png)

The database will look like:

![alt text](https://github.com/gautambhatia2502/Entry-Management-System/blob/master/images/databasenew.png)


# Why this feature was added?
One can export the whole visitor database into an excel sheet. This export operation is generally used for taking database backup. We can use this backup later for various purposes. For example, this will help to reuse backup for restoring the database in the future.

