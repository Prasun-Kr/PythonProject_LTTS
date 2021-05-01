from covid import Covid

import csv
import pandas as pd
from matplotlib.pyplot import ylabel, bar, plot, scatter, show, xlabel
import pyttsx3 as s

cv = Covid()
l2 = []
l1 = ['id', 'country', 'confirmed', 'active', 'deaths', 'recovered', 'latitude', 'longitude', 'last_update']


def world():
    f = s.init()

    print("covid Analysis")
    print()
    f.say("covid Analysis")
    f.runAndWait()

    cv = Covid()
    act = cv.get_total_active_cases()
    rec = cv.get_total_recovered()
    death = cv.get_total_deaths()
    con = cv.get_total_confirmed_cases()
    wl = []
    wll = ['active', 'recovered', 'deaths', 'confirmed']
    wl.append(act)
    wl.append(rec)
    wl.append(death)
    wl.append(con)
    f.say("Total covid details of world are shown in the screen")
    f.runAndWait()
    print(f"cases in world:{dict(zip(wll, wl))}")


def add_col():
    value = [('IN', 'india'),
             ('US', 'United States'),
             ('AF', 'Afghanistan'),
             ('AL', 'Albania'),
             ('DZ', 'Algeria'),
             ('AS', 'American Samoa'),
             ('AD', 'Andorra'),
             ('AO', 'Angola'),
             ('AI', 'Anguilla'),
             ('AQ', 'Antarctica'),
             ('AG', 'Antigua And Barbuda'),
             ('AR', 'Argentina'),
             ('AM', 'Armenia'),
             ('AW', 'Aruba'),
             ('AU', 'Australia'),
             ('AT', 'Austria'),
             ('AZ', 'Azerbaijan'),
             ('BS', 'Bahamas'),
             ('BH', 'Bahrain'),
             ('BD', 'Bangladesh'),
             ('BB', 'Barbados'),
             ('BY', 'Belarus'),
             ('BE', 'Belgium'),
             ('BZ', 'Belize'),
             ('BJ', 'Benin'),
             ('BM', 'Bermuda'),
             ('BT', 'Bhutan'),
             ('BO', 'Bolivia'),
             ('BA', 'Bosnia And Herzegowina'),
             ('BW', 'Botswana'),
             ('BV', 'Bouvet Island'),
             ('BR', 'Brazil'),
             ('BN', 'Brunei Darussalam'),
             ('BG', 'Bulgaria'),
             ('BF', 'Burkina Faso'),
             ('BI', 'Burundi'),
             ('KH', 'Cambodia'),
             ('CM', 'Cameroon'),
             ('CA', 'Canada'),
             ('CV', 'Cape Verde'),
             ('KY', 'Cayman Islands'),
             ('CF', 'Central African Rep'),
             ('TD', 'Chad'),
             ('CL', 'Chile'),
             ('CN', 'China'),
             ('CX', 'Christmas Island'),
             ('CC', 'Cocos Islands'),
             ('CO', 'Colombia'),
             ('KM', 'Comoros'),
             ('CG', 'Congo'),
             ('CK', 'Cook Islands'),
             ('CR', 'Costa Rica'),
             ('CI', 'Cote D`ivoire'),
             ('HR', 'Croatia'),
             ('CU', 'Cuba'),
             ('CY', 'Cyprus'),
             ('CZ', 'Czech Republic'),
             ('DK', 'Denmark'),
             ('DJ', 'Djibouti'),
             ('DM', 'Dominica'),
             ('DO', 'Dominican Republic'),
             ('TP', 'East Timor'),
             ('EC', 'Ecuador'),
             ('EG', 'Egypt'),
             ('SV', 'El Salvador'),
             ('GQ', 'Equatorial Guinea'),
             ('ER', 'Eritrea'),
             ('EE', 'Estonia'),
             ('ET', 'Ethiopia'),
             ('FK', 'Falkland Islands (Malvinas)'),
             ('FO', 'Faroe Islands'),
             ('FJ', 'Fiji'),
             ('FI', 'Finland'),
             ('FR', 'France'),
             ('GF', 'French Guiana'),
             ('PF', 'French Polynesia'),
             ('TF', 'French S. Territories'),
             ('GA', 'Gabon'),
             ('GM', 'Gambia'),
             ('GE', 'Georgia'),
             ('DE', 'Germany'),
             ('GH', 'Ghana'),
             ('GI', 'Gibraltar'),
             ('GR', 'Greece'),
             ('GL', 'Greenland'),
             ('GD', 'Grenada'),
             ('GP', 'Guadeloupe'),
             ('GU', 'Guam'),
             ('GT', 'Guatemala'),
             ('GN', 'Guinea'),
             ('GW', 'Guinea-bissau'),
             ('GY', 'Guyana'),
             ('HT', 'Haiti'),
             ('HN', 'Honduras'),
             ('HK', 'Hong Kong'),
             ('HU', 'Hungary'),
             ('IS', 'Iceland'),
             ('IN', 'India'),
             ('ID', 'Indonesia'),
             ('IR', 'Iran'),
             ('IQ', 'Iraq'),
             ('IE', 'Ireland'),
             ('IL', 'Israel'),
             ('IT', 'Italy'),
             ('JM', 'Jamaica'),
             ('JP', 'Japan'),
             ('JO', 'Jordan'),
             ('KZ', 'Kazakhstan'),
             ('KE', 'Kenya'),
             ('KI', 'Kiribati'),
             ('KP', 'Korea (North)'),
             ('KR', 'Korea (South)'),
             ('KW', 'Kuwait'),
             ('KG', 'Kyrgyzstan'),
             ('LA', 'Laos'),
             ('LV', 'Latvia'),
             ('LB', 'Lebanon'),
             ('LS', 'Lesotho'),
             ('LR', 'Liberia'),
             ('LY', 'Libya'),
             ('LI', 'Liechtenstein'),
             ('LT', 'Lithuania'),
             ('LU', 'Luxembourg'),
             ('MO', 'Macau'),
             ('MK', 'Macedonia'),
             ('MG', 'Madagascar'),
             ('MW', 'Malawi'),
             ('MY', 'Malaysia'),
             ('MV', 'Maldives'),
             ('ML', 'Mali'),
             ('MT', 'Malta'),
             ('MH', 'Marshall Islands'),
             ('MQ', 'Martinique'),
             ('MR', 'Mauritania'),
             ('MU', 'Mauritius'),
             ('YT', 'Mayotte'),
             ('MX', 'Mexico'),
             ('FM', 'Micronesia'),
             ('MD', 'Moldova'),
             ('MC', 'Monaco'),
             ('MN', 'Mongolia'),
             ('MS', 'Montserrat'),
             ('MA', 'Morocco'),
             ('MZ', 'Mozambique'),
             ('MM', 'Myanmar'),
             ('NA', 'Namibia'),
             ('NR', 'Nauru'),
             ('NP', 'Nepal'),
             ('NL', 'Netherlands'),
             ('AN', 'Netherlands Antilles'),
             ('NC', 'New Caledonia'),
             ('NZ', 'New Zealand'),
             ('NI', 'Nicaragua'),
             ('NE', 'Niger'),
             ('NG', 'Nigeria'),
             ('NU', 'Niue'),
             ('NF', 'Norfolk Island'),
             ('MP', 'Northern Mariana Islands'),
             ('NO', 'Norway'),
             ('OM', 'Oman'),
             ('PK', 'Pakistan'),
             ('PW', 'Palau'),
             ('PA', 'Panama'),
             ('PG', 'Papua New Guinea'),
             ('PY', 'Paraguay'),
             ('PE', 'Peru'),
             ('PH', 'Philippines'),
             ('PN', 'Pitcairn'),
             ('PL', 'Poland'),
             ('PT', 'Portugal'),
             ('PR', 'Puerto Rico'),
             ('QA', 'Qatar'),
             ('RE', 'Reunion'),
             ('RO', 'Romania'),
             ('RU', 'Russian Federation'),
             ('RW', 'Rwanda'),
             ('KN', 'Saint Kitts And Nevis'),
             ('LC', 'Saint Lucia'),
             ('VC', 'St Vincent/Grenadines'),
             ('WS', 'Samoa'),
             ('SM', 'San Marino'),
             ('ST', 'Sao Tome'),
             ('SA', 'Saudi Arabia'),
             ('SN', 'Senegal'),
             ('SC', 'Seychelles'),
             ('SL', 'Sierra Leone'),
             ('SG', 'Singapore'),
             ('SK', 'Slovakia'),
             ('SI', 'Slovenia'),
             ('SB', 'Solomon Islands'),
             ('SO', 'Somalia'),
             ('ZA', 'South Africa'),
             ('ES', 'Spain'),
             ('LK', 'Sri Lanka'),
             ('SH', 'St. Helena'),
             ('PM', 'St.Pierre'),
             ('SD', 'Sudan'),
             ('SR', 'Suriname'),
             ('SZ', 'Swaziland'),
             ('SE', 'Sweden'),
             ('CH', 'Switzerland'),
             ('SY', 'Syrian Arab Republic'),
             ('TW', 'Taiwan'),
             ('TJ', 'Tajikistan'),
             ('TZ', 'Tanzania'),
             ('TH', 'Thailand'),
             ('TG', 'Togo'),
             ('TK', 'Tokelau'),
             ('TO', 'Tonga'),
             ('TT', 'Trinidad And Tobago'),
             ('TN', 'Tunisia'),
             ('TR', 'Turkey'),
             ('TM', 'Turkmenistan'),
             ('TV', 'Tuvalu'),
             ('UG', 'Uganda'),
             ('UA', 'Ukraine'),
             ('AE', 'United Arab Emirates'),
             ('UK', 'United Kingdom'),
             ('UY', 'Uruguay'),
             ('UZ', 'Uzbekistan'),
             ('VU', 'Vanuatu'),
             ('VA', 'Vatican City State'),
             ('VE', 'Venezuela'),
             ('VN', 'Viet Nam'),
             ('VG', 'Virgin Islands (British)'),
             ('VI', 'Virgin Islands (U.S.)'),
             ('EH', 'Western Sahara'),
             ('YE', 'Yemen'),
             ('YU', 'Yugoslavia'),
             ('ZR', 'Zaire'),
             ('ZM', 'Zambia'),
             ('ZW', 'Zimbabwe'), ('RW', 'Russia')
             ]
    global lc
    lc = []
    for i in range(len(value)):
        for j in range(1):
            lc.append((value[i][1]).lower())
    with open("p.csv", mode='w') as f:
        g = csv.writer(f)
        g.writerow(l1)


def add_row():
    global l3
    while 1:
        f = s.init()
        print()

        print("enter country name or enter no to stop")
        f.say("enter country name or enter no to stop")
        print()
        f.runAndWait()
        name = input().lower()
        if name == "no":
            f.say("we stop showing covid details on the screen")
            f.runAndWait()

        elif name not in lc:
            f.say("you entered invalid country name please enter again")
            f.runAndWait()
        else:

            f.say(f"covid details of {name} are showing on the screen")
            f.runAndWait()
        if name in lc:

            n = cv.get_status_by_country_name(name)

            for i in n.values():
                l2.append(i)
                l3 = l2.copy()
            print(dict(zip(l1, l3)))
            with open("p.csv", mode='a') as f:
                g = csv.writer(f)
                g.writerow(l3)

            l2.clear()

        elif name == "no":
            break

        else:
            print("invalid country")


def menu():
    f = s.init()
    df = pd.read_csv("p.csv")
    print(df.head())
    print("enter 1 for bar plot:")
    f.say("enter one for bar plot:")
    f.runAndWait()
    print("enter 2 for scatter plot:")
    f.say("enter two for scatter plot:")
    f.runAndWait()
    print("enter 3 for plot:")
    f.say("enter three for plot:")
    f.runAndWait()
    print("enter 4 for exit:")
    f.say("enter four for exit:")
    f.runAndWait()


def show():
    while 1:
        f = s.init()

        f.say("enter options:")
        f.runAndWait()

        ch = int(input("enter options:"))
        df = pd.read_csv("p.csv")

        if ch == 1:
            xlabel("Countries")
            ylabel("Active Cases")
            bar(df['country'], df['active'])
            show()
            xlabel("Countries")
            ylabel("confirmed Cases")
            bar(df['country'], df['confirmed'])
            show()
            xlabel("Countries")
            ylabel("deaths")
            bar(df['country'], df['deaths'])
            show()
            xlabel("Countries")
            ylabel("recovered ")
            bar(df['country'], df['recovered'])
            show()
        if ch == 3:
            xlabel("Countries")
            ylabel("Active Cases")
            plot(df['country'], df['active'])
            show()
            xlabel("Countries")
            ylabel("confirmed Cases")
            plot(df['country'], df['confirmed'])
            show()
            xlabel("Countries")
            ylabel("deaths")
            plot(df['country'], df['deaths'])
            show()
            xlabel("Countries")
            ylabel("recovered ")
            plot(df['country'], df['recovered'])
            show()
        elif ch == 2:
            xlabel("Countries")
            ylabel("Active Cases")
            scatter(df['country'], df['active'])
            show()
            xlabel("Countries")
            ylabel("confirmed Cases")
            scatter(df['country'], df['confirmed'])
            show()
            xlabel("Countries")
            ylabel("deaths")
            scatter(df['country'], df['deaths'])
            show()
            xlabel("Countries")
            ylabel("recovered ")
            scatter(df['country'], df['recovered'])
            show()
        elif ch == 4:
            print("Thankyou I hope you liked this project")
            f.say("Thankyou I hope you liked this project")
            f.runAndWait()
            break
        else:
            print("invalid option try again")
            f.say("invalid option try again")
            f.runAndWait()

world()
add_col()
add_row()
menu()
show()
