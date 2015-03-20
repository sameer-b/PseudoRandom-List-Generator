'''
	Copyright (C) 2015 Sameer Balasubrahmanyam
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 '''
import random
#Largest number in the list.
MAX_NUMBER = 1000
#Smallest number in the list.
MIN_NUMBER = 1
#Size of the list.
LIST_SIZE = 35

def generateRandomList(MIN_NUMBER, MAX_NUMBER, LIST_SIZE):
	list = random.sample(range(MIN_NUMBER,MAX_NUMBER),LIST_SIZE)

	output = ""
	for i in range(0,len(list)):
		if( i==0 ):
			output = str(list[i])
		else:	
			output +=  " "+str(list[i])
	return output		



f = open('randomList.txt','w')
f.write(generateRandomList(MIN_NUMBER, MAX_NUMBER, LIST_SIZE))
f.close();