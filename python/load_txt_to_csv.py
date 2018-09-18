import csv
import sys

txt_file = input("TXT file path ")
csv_file = input("CSV file path ")
separator = input("Separator ")
headers = input("List of headers, separated by comma ")

# txt_file = 'unique_artists.txt'
# csv_file = 'unique_artists.csv'
# separator = ','
# headers = 'artist_id, artist_mbid, track_id, artist_name'

with open(txt_file, 'r') as inputFile:
	inputContent = inputFile.readlines()
	inputContent = [line.strip() for line in inputContent]
	inputContent = [line.split(separator) for line in inputContent]
with open(csv_file, 'w') as outputFile:
	writer = csv.writer(outputFile)
	writer.writerow(headers.split(','))
	for line in inputContent:
		writer.writerow(line)

