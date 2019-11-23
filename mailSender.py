import psycopg2
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

connection = psycopg2.connect(user = "office",
                              password = "####",
                              host = 'localhost',
                              port = "5432",
                              database = "myoffice1")

print("You are connected to - myoffice1 \n")
cursor = connection.cursor()
cursor.execute("set search_path to public")

def showVisits():
	query = "select office_visitor.email, office_visit.check_in, office_visit.check_out, office_host.id, office_host.name, office_visit.visit_addr, office_host.email, office_host.phone  from office_visitor join office_visit on office_visit.visitor_id = office_visitor.id join office_host on office_host.id = office_visit.host_id where office_visit.send_mail_opt = '2';"
	cursor.execute(query)
	rows = cursor.fetchall()
	return rows

def sendMail():
	k = showVisits()
	msg = MIMEMultipart()
	msg['From'] = "hw59053@gmail.com"
	msg['To'] = k[0][0]
	msg['Subject'] = "subject"
	msg1 = "check-in time: " + str(k[0][1]) + "\n" + "check-out time: " + str(k[0][2]) + "\n" + "host_person-id: " + str(k[0][3]) + "host_person-name: " + str(k[0][4]) + "\n" + "visit-address: " + str(k[0][5]) + "\n" + "host_person-email: " + str(k[0][6]) + "\n" + "host_person-phone: " + str(k[0][7]) + "\n"
	msg.attach(MIMEText(msg1, 'plain'))
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls()
	s.login("####@gmail.com", "####")  
	text = msg.as_string()
	s.sendmail("####@gmail.com", k[0][0], text)  
	s.quit() 
	query = "update office_visit set send_mail_opt = '1' where send_mail_opt ='2';"
	cursor.execute(query)
	query = "select office_visitor.email, office_visit.check_in, office_visit.check_out, office_host.id, office_host.name, office_visit.visit_addr, office_host.email, office_host.phone  from office_visitor join office_visit on office_visit.visitor_id = office_visitor.id join office_host on office_host.id = office_visit.host_id where office_visit.send_mail_opt = '1';"
	cursor.execute(query)
	rows = cursor.fetchall()
	for r in rows:
		print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}\t{r[5]}\t{r[6]}\t{r[7]}\t")

sendMail()

if(connection):
	cursor.close()
	connection.close()
	print("PostgreSQL connection is closed")