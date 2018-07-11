import requests
import bs4
import string
from os import system

rating = input('Enter Your Codechefs Username: ')
res = requests.get('https://www.codechef.com/users/' + rating)
soup = bs4.BeautifulSoup(res.text, 'lxml')
name = soup.select('h2')

system('clear')

if not name:
	print('Name: ' + name[1])
else:
	print('No user found!')

for i in soup.select('.rating-number'):
	print('Your Rating is: ' + i.text)
