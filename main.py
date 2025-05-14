def main():
    sunspot_dict = {}
    file_str = raw_input("Open what data file: ")
    keep_going = True
    while keep_going:
        try:
            init_dictionary(file_str, sunspot_dict)
        except IOError:
            print "Data file error, try again"
            file_str = raw_input("Open what data file: ")    
            continue
        print "Jan, 1900-1905:", avg_sunspot(sunspot_dict, (1900,1905),(1,1))
        print "Jan-June, 2000-2011:", avg_sunspot(sunspot_dict, (2000,2011), (1,6))
        print "All years, Jan:", avg_sunspot(sunspot_dict, month_tuple=(1,1))
        print "All months, 1900-1905:", avg_sunspot(sunspot_dict, year_tuple=(1900,1905))
        try:
            print "Bad Year Key example:", avg_sunspot(sunspot_dict, (100,1000), (1,1))
        except KeyError:
            print "Bad Key raised"
        try:
            print "Bad Month Index example:", avg_sunspot(sunspot_dict, (2000,2011), (1,100))
        except IndexError:
            print "Bad Range raised"
        keep_going = False
    print "Main function finished normally."
