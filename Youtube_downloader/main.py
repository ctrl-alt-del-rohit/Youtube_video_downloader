from pytube import YouTube

link=input("Enter the link to your video: ")
video=YouTube(link)

print("Video Title: ",video.title)
print("Video Views:",video.views)

download_video=video.streams.get_highest_resolution()
download_video.download()
print("Video Downloaded!!!!!")