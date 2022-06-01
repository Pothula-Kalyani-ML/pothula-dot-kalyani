def print_banner(NAME):
    """ Conditionally print the banner to stdout """
    global OPTS
    if OPTS.is_unit_test:
        return

    print("|==============================================================================|")
    print("|=========" + NAME.center(60) + "=========|")
    print("|=========" + " ".center(60) + "=========|")
    print("|=========" + "VLSI Design and Automation Lab".center(60) + "=========|")
    print("|=========" + "Computer Science and Engineering Department".center(60) + "=========|")
    print("|=========" + "University of California Santa Cruz".center(60) + "=========|")
    print("|=========" + " ".center(60) + "=========|")
    user_info = "Usage help: openram-user-group@ucsc.edu"
    print("|=========" + user_info.center(60) + "=========|")
    dev_info = "Development help: openram-dev-group@ucsc.edu"
    print("|=========" + dev_info.center(60) + "=========|")
    temp_info = "Temp dir: {}".format(OPTS.openram_temp)
    print("|=========" + temp_info.center(60) + "=========|")
    print("|=========" + "See LICENSE for license info".center(60) + "=========|")
    print("|==============================================================================|") 
if __name__ == "__main__":
    print_banner("kalyani")