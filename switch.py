#@author: Richard Anemam
#Data: Sep 6, 2018
#Description: switching text data (Well, I have no ideia how to set a better description XP)
#Useful tutorials to a better understanding:
#[0]: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html ("Documentations are always a good source of knowledge" - Lispector, Richard)
#[1]: Common errors in python (https://www2.cs.arizona.edu/people/mccann/errors-python#Four)
#[2]: 10 minutes to Pandas (https://pandas.pydata.org/pandas-docs/stable/10min.html)
#[3]: Pandas tutorial: DataFrames in python (https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python#question1)
#[4]: Python Pandas - DataFrame (https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm)

import pandas as pd 

class Switch:
	
	def __init__(self):
		self.usersDataList = []

	def setUsersDataList(self, users_phrase):
		self.usersDataList.append(users_phrase)

	def getUsersDataList(self):
		return self.usersDataList		

	def splitData(self):
		getDataList = self.getUsersDataList()
		splittedList = []
		for phrase in getDataList: 
			splittedList.append(phrase.split())
		return splittedList

	def setDataIntoDf(self):
		getSplittedList = self.splitData()
		flatListOut = [splittedPhrase for sublist in getSplittedList for splittedPhrase in sublist]
		columnsDict = {
						'User Input': flatListOut, 
						'Data Base' : ["ola", "meu", "nome", "eh", "Richard", "e", "eu", "quero", "cafe"]
						}
		
		df = pd.DataFrame(data = columnsDict)
		return df

	def switching(self):
		df = self.setDataIntoDf()
		strList = []

		for user_word in df["User Input"]:
			indexRow = df[df['User Input']==user_word].index.item()
			getDataBaseWord = df.at[indexRow, "Data Base"]
			strList.append(getDataBaseWord)	
		strList = ' '.join(strList)

		return strList

def main():
    
    test = Switch()
    test.setUsersDataList("olaaaa meeeeu noooome eh Richard eeee eeeeu queeeero cafeeeeeeeeeeeee")

    print (test.switching())

if __name__ == "__main__":
   main()