from bs4 import BeautifulSoup
import requests
import xlrd
codes=['INXX0193', 'INXX0074', 'INXX0038', 'INXX0102', 'INXX0087', 'INXX0202', 'INXX0203', 'INXX0139', 'USIL0225', 'NLXX0002']
cities=['LUDHIANA', 'LUCKNOW', 'DELHI', 'PUNE', 'MUMBAI', 'CHENNAI', 'AGRA', 'PATIALA', 'CHICAGO', 'AMSTERDAM']
exit="-1"
while(exit!=""):   #do exception handling here to get out of loop using some exit status
    print("\n Enter the name of city: ")
    city=input().upper()
    if(city in cities):
        city=codes[cities.index(city)]
    else:
        loc=r"C:\Users\gupta\Desktop\funstuff\weather_codes.xlsx"
        wb=xlrd.open_workbook(loc)
        sheet=wb.sheet_by_index(0)
        for rowno in range(sheet.nrows):
            rowvalue = str(sheet.cell(rowno,0))[6:-1].upper()
            if rowvalue == city:
                city=str(sheet.cell(rowno-1,0))[6:-1]
                print(city)
            
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
    exit=input()

