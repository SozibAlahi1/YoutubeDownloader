from pytube import YouTube
link = str(input("Enter Your Youtube Link : "))
print("please wait a coupple of .....................")
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()

print("Download Finished")

