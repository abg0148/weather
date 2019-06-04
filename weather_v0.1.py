from bs4 import BeautifulSoup
import requests
import xlrd
loc=r"C:\Users\gupta\Desktop\funstuff\weather_codes.xlsx"
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(0)
codes=[str(sheet.cell(i,0))[6:-1] for i in range((sheet.nrows)) if i%2==0]
cities=[str(sheet.cell(i,0))[6:-1].upper() for i in range((sheet.nrows)) if i%2!=0]
print("Enter the name of city: ")
city=codes[cities.index(input().upper())]
link="https://weather.com/en-IN/weather/today/l/"+city
page_response=requests.get(link)
page_content=BeautifulSoup(page_response.content,"html.parser")
print(page_content.find("h1",class_="h4 today_nowcard-location").text)
print(page_content.find("p",class_="today_nowcard-timestamp").text)
print("\n TEMPERATURE: ",end="")
print(page_content.find("div",class_="today_nowcard-temp").text)
print("\n FEELS LIKE: ",end="")
print(page_content.find("span",class_="deg-feels").text)
print("\n WEATHER: ",end="")
print(page_content.find("div",class_="today_nowcard-phrase").text)
input()

