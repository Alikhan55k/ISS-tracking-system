import requests
import datetime
import smtplib
import time

#Check time and Calculate total minutes from hours and minutes

datetime=datetime.datetime.now()
hour=datetime.hour
minute=datetime.minute+hour*60


#Check sunset time from website and Add 5 in hours because karachi time standerd is ahead 5 hours from UTC again calculate total mintues

MY_LAT=31.656408
MY_LNG=71.326153
response = requests.get('https://api.sunrise-sunset.org/json',params={'lat':MY_LAT, 'lng':MY_LNG,'formatted':0})
response.raise_for_status()

sunset=response.json()['results']['sunset']
sunset_list=sunset.split('T')
sunset_list=sunset_list[1].split(':')
sunset_hour=int(sunset_list[0])+5
sunset_min=int(sunset_list[1])+sunset_hour*60
end=False
#Use API System to check the Current location of ISS
while not end:
    time.sleep(15)
    response2=requests.get('https://api.wheretheiss.at/v1/satellites/25544')
    response2.raise_for_status()
    iss_lat=float(response2.json()['latitude'])
    iss_lng=float(response2.json()['longitude'])

    #send mail if ISS is above our range and it is the time after Sunset

    if MY_LAT-5<=iss_lat<=MY_LAT+5 and MY_LNG-5<=iss_lng<=MY_LNG+5 and minute>sunset_min :
        print('ISS is close to your Location')
        connection=smtplib.SMTP('smtp.gmail.com')
        connection.starttls()
        my_mail = 'programmer5727ghs@gmail.com'
        password = 'nflq mgwz zjcw zmzu'
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail, to_addrs=my_mail,
                            msg=f'Subject:Look Up!\n\nThe ISS is above your location so look up and Analyze it')
        connection.close()
        end=True
    else:
        print('ISS is not close to your Location')