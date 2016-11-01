"""

Author: Pejmon Hodaee

Description: Gather CSVs from Daymet site.



Fill in lat and lon ranges and the step in main().

Running the code on a Unix system should correctly call bash script to run the CSV retrieval



Tested on macOS 10.11.6, Python 2.7



"""



from subprocess import call  # allows running bash scripts/etc





def fill_conf(lat_start, lon_start, lat_end, lon_end, step):  # fills config file of single pixel downloader

    confFile = open("latlon.txt", "w") # wipes file

    confFile.close()



    confFile = open("latlon.txt", "w")



    lat_range_start = int(lat_start*10000)

    lat_range_end = int(lat_end*10000)



    lon_range_start = int(lon_start*10000)

    lon_range_end = int(lon_end*10000)



    step_range = int(step*10000)

    lat_bin = []

    lon_bin = []



    for i in range(lat_range_start, lat_range_end+20, step_range):

        lat_bin.append(float(i) / 10000)



    for i in range(lon_range_start, lon_range_end + 20, step_range):

        lon_bin.append(float(i) / 10000)



    for i in range(len(lat_bin)):

        for j in range(len(lon_bin)):

            confFile.write(str(lat_bin[i]) + "_" + str(lon_bin[j]) + ".csv, " + str(lat_bin[i]) + "," + str(lon_bin[j]) +

                           "\n")

    confFile.close()





def download_files():  # downloads the CSVs

    call(['bash', 'daymet_multiple_extraction.sh'])

    call(['ls', '-l'])



def main():

    """

    Fill in lat and lon ranges and the step below.

    Running the code on a Unix system should correctly call bash script to run the CSV retrieval

    """



    lat_start = 32.731

    lat_end = 32.741



    lon_start = -114.6847

    lon_end = -114.4611



    step = 0.01



    fill_conf(lat_start, lon_start, lat_end, lon_end, step)

    download_files()



if __name__ == '__main__':

    main()
