class flightaware(object):
    """
    Flightaware data scraper
    """
    def __init__(self):
        super(flightaware, self).__init__()

    def get(self, flight):
        return self.__load(flight)

    def __load(self, flight):
        import urllib2
        url = 'http://uk.flightaware.com/live/flight/' + flight
        conn = urllib2.urlopen(url)
        response = conn.read()
        return self.__parse(response)

    def __parse(self, html):
        import re
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html)
        self.flight_general = {
        'Name': soup.find('div', class_='track-panel-header-title')\
        .find('span').text,
        'Duration': soup.find('div', class_='track-panel-duration')\
        .text.strip().replace('Duration: ',''),
        'Flight Date': soup.find('div', class_='track-panel-date').text.strip(),
        'Flight Status': soup.find('table', class_='layout-table track-panel-data')\
        .contents[0].find('td', class_='smallrow1').text.strip(),
        'Flight Aircraft': soup.find('td', class_="smallrow2").a.text
        }
        self.flight_departure = {
        'Airport': soup.find('td', class_='track-panel-departure')\
        .find('div', class_="track-panel-airport").text,
        'Terminal': soup.find('td', class_='track-panel-departure')\
        .find('div', class_="track-panel-terminal").text,
        'Time': soup.find_all('td', class_='track-panel-actualtime')[0].text,
        'Scheduled Time': (soup.find_all\
            ('tr', class_='track-panel-scheduledtime')[0]).find('td').text,
        }
        self.flight_arrival = {
        'Airport': soup.find('td', class_='track-panel-arrival')\
        .find('div', class_="track-panel-airport").text,
        'Terminal': soup.find('td', class_='track-panel-arrival')\
        .find('div', class_="track-panel-terminal").text,
        'Time': soup.find_all('td', class_='track-panel-actualtime')[1].text,
        'Scheduled Time': (soup.find_all\
            ('tr', class_='track-panel-scheduledtime')[1]).find('td').text,
        }
        #fix utf
        self.flight_departure = { k:v.encode('ascii','ignore').strip()\
         for k, v in self.flight_departure.iteritems() }
        self.flight_arrival = { k:v.encode('ascii','ignore').strip()\
         for k, v in self.flight_arrival.iteritems() }
        return self.flight_departure, self.flight_arrival, self.flight_general
