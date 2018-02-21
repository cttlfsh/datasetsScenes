import csv
import glob
import os

def calculateRange(max_val, min_val):
	return max_val - min_val

def calculateNormalizer(ranges_x, ranges_z):
	return max(max(ranges_x, key = abs), max(ranges_z, key = abs))

def normalize(current, min, normalizer):
	return ("%.5f" % ((2 * (current - min) / normalizer) - 1))


### Arrays to represent the rows of the file for each scene
all_frames = []
all_personIDs = []
all_column_x = []
all_column_z = []
all_groupIDs = []
### Lists of ranges for each scene
ranges_x = []
ranges_z = []
### Lists of max/min values for each scene
maxs_x = []
mins_x = []
maxs_z = []
mins_z = []


### Get the current directory
cwd = os.getcwd() + "/World*.txt"
### List of all the .txt files
scenes = glob.glob(cwd)
for scene in scenes:
	frames = []
	personIDs = []
	column_x = []
	column_z = []
	groupIDs = []

	with open(scene, "r") as f:
		# Fill the lists with their correspondent values
		for line in f:
		###												 ###
		#		Parameters on square brackets will change  #
		#		depending on the txt file column order     #
		###												 ###
			if len(line.split("\t")) > 5:
				frames.append(int(line.split("\t")[0]))
				personIDs.append(int(line.split("\t")[1]))
				column_x.append(float(line.split("\t")[2]))
				column_z.append(float(line.split("\t")[4]))
				groupIDs.append(int(line.split("\t")[8]))


		### Fill the lists which will contain values for each
		#   scene
		all_frames.append(frames)
		all_personIDs.append(personIDs)
		all_column_x.append(column_x)
		all_column_z.append(column_z)
		all_groupIDs.append(groupIDs)

	# ### Find the max values of X and Z coordinates
	# maxs_x.append(max(column_x))
	# maxs_z.append(max(column_z))

	### Mins are saved for further usage 
	mins_x.append(min(column_x))
	mins_z.append(min(column_z))
	### Compute the range of disparity of X and Z
	ranges_x.append(calculateRange(max(column_x), min(column_x)))
	ranges_z.append(calculateRange(max(column_z), min(column_z)))

### Compute the normalizer factor over all scenes
normalizer = calculateNormalizer(ranges_x, ranges_z)

### Initialize the counter to scan the lists depending
#   on the scene
i = 0
for scene in scenes:
	### Instantiate the lists for normalized coordinates
	x_norm = []
	z_norm = []
	### Compute the final normalized coordinates
	for x in all_column_x[i]:
		x_norm.append(normalize(x, mins_x[i], normalizer))
	for z in all_column_z[i]:
		z_norm.append(normalize(z, mins_z[i], normalizer))
	### Create the .csv files for each camera recording
	with open("results" + "_" + str(i) + ".csv", "w") as f:
		writer = csv.writer(f, delimiter = ',')
		writer.writerow(all_frames[i])
		writer.writerow(all_personIDs[i])
		writer.writerow(x_norm)
		writer.writerow(z_norm)
		writer.writerow(all_groupIDs[i])
	### Increment the counter
	i += 1