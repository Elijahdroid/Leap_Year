def Leap_Year_Check(year, revenue):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
             if revenue > 1000000 :
                print("Platinum Year")
             elif year % 400 == 0:
                if revenue < 500000:
                    print("Redistribution Year")
             else:
                 print("Standard Cycle")
    else:
        y = str(year)
        r = str(revenue)
        last_2_digits_y = y[len(y)-2] + y[len(y)-1]
        last_2_digits_r = r[len(r)-2] + r[len(r)-1]
        if int(last_2_digits_y) != 0:
            if int(last_2_digits_r) % int(last_2_digits_y) == 0:
                print("Statistical Anomaly")
        else:
            print("Standard Cycle")




Leap_Year_Check(2000, 400000)
Leap_Year_Check(2024, 1200000)
Leap_Year_Check(1925, 50)
Leap_Year_Check(1900, 1500000)
