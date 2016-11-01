"""
Author: Portions of code by teamDEET adapted by Pejmon Hodaee
Special thanks to teamDEET

Description: Adapts CSVs to workable goodness

Generates 3 CSVs
master.csv: contains lat, lon, year, month, day, T_max, T_min, PrecipMM, T_ave, PrecipCM, RelHum
MoLS_comp.csv: year, month, day, T_max, T_min, PrecipMM, T_ave, PrecipCM, RelHum
lat_lon.csv (same number of rows as MoLS_comp): lat, lon

Ensure your single point CSVs are in the same directory as this code. 

Tested on macOS 10.11.6, Python 3.5

"""
import csv, os
import math

def get_month(day):
    if day < 32:
        return 1, day
    if day < 60:
        return 2, day - 31
    if day < 91:
        return 3, day - 59
    if day < 121:
        return 4, day - 90
    if day < 152:
        return 5, day - 120
    if day < 182:
        return 6, day - 151
    if day < 213:
        return 7, day - 181
    if day < 244:
        return 8, day - 212
    if day < 274:
        return 9, day - 243
    if day < 305:
        return 10, day - 273
    if day < 335:
        return 11, day - 304
    else:
        return 12, day - 334


def main():
    """
    Fill in lat and lon ranges and the step below.
    Running the code on a Unix system should correctly call bash script to run the CSV retrieval
    """
    master_csv = open("master.csv", "w")
    master_csv.write("lat, lon, year, month, day, T_max, T_min, PrecipMM, T_ave, PrecipCM, RelHum\n")
    MoLS_comp_csv = open("MoLS_comp.csv", "w")
    lat_lon_csv = open("lat_lon.csv", "w")

    for csvFilename in os.listdir('.'):

        if not csvFilename.endswith('.csv') or csvFilename == "master.csv" or csvFilename == "MoLS_comp.csv" or csvFilename == "lat_lon.csv":
            continue  # skip non-csv files

        csvFileObj = open(csvFilename)
        readerObj = csv.reader(csvFileObj)
        print("Currently parsing " + str(csvFilename))
        for row in readerObj:
            if readerObj.line_num <= 8 :
                continue

            year = int(row[0])
            vp = float(row[8]) / 1000.0
            month, day = get_month(int(row[1]))
            T_ave = (float(row[6]) + float(row[7])) / 2
            PrecipCM = float(row[3]) / 10
            svp = .611 * math.e ** (5321 * ((1 / 273.0) - (1 / (T_ave + 273.15))))
            rh_ave = round((vp / svp) * 100, 2)

            # print([[csvFilename], , row[0], row[1], row[3], row[6], row[7], row[8]])
            # print(readerObj.line_num)
            # print([csvFilename.split("_")[0], csvFilename.split("_")[1].split(".csv")[0], row[0], row[1], row[3],
            #       row[6], row[7], row[8]])

            master_csv.write(str(csvFilename.split("_")[0]) + "," + str(csvFilename.split("_")[1].split(".csv")[0]) +
                            "," + str(year) + "," + str(month) + "," + str(day) + "," + str(row[6]) + "," + str(row[7])
                            + "," + str(row[3]) + "," + str(T_ave) + "," + str(PrecipCM) + "," + str(rh_ave) + "\n")
            MoLS_comp_csv.write(str(year) + "," + str(month) + "," + str(day) + "," + str(row[6]) + "," + str(row[7])
                         + "," + str(row[3]) + "," + str(T_ave) + "," + str(PrecipCM) + "," + str(rh_ave) + "\n")
            lat_lon_csv.write(str(csvFilename.split("_")[0]) + "," + str(csvFilename.split("_")[1].split(".csv")[0]) + "\n")

    master_csv.close()
    MoLS_comp_csv.close()
    lat_lon_csv.close()
if __name__ == '__main__':
    main()
