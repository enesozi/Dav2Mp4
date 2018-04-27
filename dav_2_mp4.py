import os
from subprocess import call

def main():
	for dirpath, dirnames, filenames in os.walk("."):
		files = [f for f in filenames if f.endswith(".dav")]
		for filename in files:
			mp4Name = os.path.join(dirpath, filename.replace("dav", "mp4"))
			file_path = os.path.join(dirpath, filename)
			print("Converting: " + filename)
			call(['ffmpeg', '-y', '-i', file_path, "-vcodec", "libx264", "-crf", "24", mp4Name])
			print("Converted: " + filename)

if __name__ == "__main__":
	main()		