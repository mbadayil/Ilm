import requests
import json
response=requests.get('http://api.bart.gov/api/etd.aspx?cmd=etd&orig=MONT&key=ZPBV-5PUE-9ZIT-DWE9&json=y')
#Model api used from bart, the above step will get response object from the model api
car = response.json()#converting response in to json format
#Sample response after conversion is below. We will be using the below sample to
#write remaining functionsl for
# 1- Print all the blue Teslas received in the web service response. Also print
#the notes
# 2- Return all cars which have the lowest per day rental cost for both cases:
#    - a. Price only :
#    - b. Price after discounts
# Find the highest revenue generating car. year over year maintenance cost +
#epreciation is the total expense per car for the full year for the rental car company.car
car={
    "Car": [
        {
            "make": "Audi",
            "model": "A7",
            "vin": "234JKSJDFJKHSDFKJHSDFK",
            "metadata": {
                "Color": "Black",
                "Notes": "Scratches right on the front side of the car"
            },
            "perdayrent": {
                "Price": 340,
                "Discount": 15
            },
            "metrics": {
                "yoymaintenancecost": 2190.76,
                "depreciation": 2256.43,
                "rentalcount": {
                    "lastweek": 4,
                    "yeartodate": 221
                }
            }
        },
        {
            "make": "Tesla",
            "model": "Hybrid",
            "vin": "4758693013VIF897234987",
            "metadata": {
                "Color": "Blue",
                "Notes": "Scratches left on the front side of the car"
            },
            "perdayrent": {
                "Price": 240,
                "Discount": 25
            },
            "metrics": {
                "yoymaintenancecost": 3190.76,
                "depreciation": 2156.43,
                "rentalcount": {
                    "lastweek": 4,
                    "yeartodate": 211
                }
            }
        },
        {
            "make": "Tesla",
            "model": "Electric",
            "vin": "64735NHGFH61289034SDF",
            "metadata": {
                "Color": "Blue",
                "Notes": "Scratches123 on the front side of the car"
            },
            "perdayrent": {
                "Price": 140,
                "Discount": 15
            },
            "metrics": {
                "yoymaintenancecost": 1190.76,
                "depreciation": 2116.43,
                "rentalcount": {
                    "lastweek": 4,
                    "yeartodate": 211
                }
            }
        },
        {
            "make": "Tesla",
            "model": "Hybrid",
            "vin": "7860NMXCVBNXMKJDSKFJHEW",
            "metadata": {
                "Color": "RED",
                "Notes": "Scratches7860 on the front side of the car"
            },
            "perdayrent": {
                "Price": 280,
                "Discount": 35
            },
            "metrics": {
                "yoymaintenancecost": 4190.76,
                "depreciation": 1256.43,
                "rentalcount": {
                    "lastweek": 4,
                    "yeartodate": 201
                }
            }
        }
    ]
}


def blueTeslaWithNotes(car):
    """This function takes the json response and lists all Tesla car with COLOR
    Blue. Its also prints the notes that are attached to Tesla Blue cars

    """
    print("\nListing all Blue color Tesla with Notes: \n")
    print("MAKE:           COLOR:           MODEL:                  VIN:        \
                 NOTES: ")
    for cars in range(len(car['Car'])):
        if car['Car'][cars]['make']=='Tesla' and car['Car'][cars]['metadata'] \
        ['Color']=='Blue':
            print(car['Car'][cars]['make'],"\t\t", car['Car'][cars]['metadata']\
            ['Color'],"\t\t",car['Car'][cars]['model'],"\t\t",car['Car'][cars]\
            ['vin'],"\t\t",car['Car'][cars]['metadata']['Notes'])


def perDayRent(car):
    """This function takes the json response and lists all cars those have the
    cheapest perday rent. Function also make sure to list only the first 10
    best rates for the day:
    
    :param count: int - this variable is used to list as ID as well as used to count to list
    up to first best 10 deals.

    """
    count=0
    prices=[car['Car'][cars]['perdayrent']['Price'] for cars in range\
    (len(car['Car']))]#Storing perdDay rent to list
    prices=sorted(prices)#sorting the list so that lower comes first
    print("\nListing all Cars those are cheapest per day price and with discout" \
    " added: \n")
    print("ID       Car Model    Rental-Price-Today ")
    for price in prices:
        for cars in range(len(car['Car'])):
            if car['Car'][cars]['perdayrent']['Price']==price:
                count+=1#counting the number of Cars
                sum1=car['Car'][cars]['perdayrent']['Price']-car['Car'][cars] \
                ['perdayrent']['Discount']
                if count<=10:#making sure to lists first best 10 deals
                    print(count,"\t",car['Car'][cars]['make'],car['Car'][cars] \
                    ['metadata']['Color'],"\t$",car['Car'][cars]['perdayrent'] \
                    ['Price'],"\t\t\t")



def perDayRentwithDiscount(car):
    """This function takes the json response and lists all cars those have the
    cheapest perday rent with discout added. Function also make sure to list
    only the first 5 best rates for the day:
    
    : param count: int- this variable is used to list as ID as well as used to count to list
    up to first best 5 deals.

    """
    count=0
    prices=[car['Car'][cars]['perdayrent']['Price'] for cars in
    range(len(car['Car']))] #Storing perdDay rent to list
    prices=sorted(prices)#sorting the list so that lower comes first
    print("\nListing all Cars those are cheapest per day price and with discout"\
    " added: \n")
    print("ID       Car Model    Rental-Price-Today    After-Discount   ")
    for price in prices:
        for cars in range(len(car['Car'])):
            if car['Car'][cars]['perdayrent']['Price']==price:
                count+=1 #counting the number of Cars
                diff=car['Car'][cars]['perdayrent']['Price']-car['Car'][cars] \
                ['perdayrent']['Discount']
                if count<=5:#making sure to lists first best 5 deals
                    print(count,"\t",car['Car'][cars]['make'],car['Car'][cars] \
                    ['metadata']['Color'],"\t$",car['Car'][cars]['perdayrent'] \
                    ['Price'],"\t\t\t$",diff)



def revenueYoY(car):
    """This function takes the json response and calculates the YearOverYear
    revenue. Idea is to find out which car produced highest profit.

  
    : param expenses:list- is used to store year over year maintenance cost + depreciation.

    """
    expenses=[]
    for cars in range(len(car['Car'])):
        expenses.append(round(car['Car'][cars]['metrics']['yoymaintenancecost']+
        car['Car'][cars]['metrics']['depreciation'],2))#Used round function to store only 2 digits after decimal
    print("\nListing all  cars that produced the highest profit in the last year:"\
     "\n")
    print("MAKE:           COLOR:           MODEL:")
    for exp in expenses:
        for rev in range(len(car['Car'])):
            if round(car['Car'][rev]['metrics']['yoymaintenancecost']+car['Car']\
            [rev]['metrics']['depreciation'],2)==exp: #Used round function to store only 2 digits after decimal
                print(car['Car'][rev]['make'],"\t\t",car['Car'][rev]['metadata']\
                ['Color'],"\t\t",car['Car'][rev]['model'])



#Running each function  one after another and listing output.
if __name__=='__main__':
    blueTeslaWithNotes(car)
    perDayRent(car)
    perDayRentwithDiscount(car)
    revenueYoY(car)
