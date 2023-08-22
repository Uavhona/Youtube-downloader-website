from tkinter.filedialog import askdirectory
import moviepy.editor as mp


# function to convert video to mp3
def convert_to_mp3():
    # getting video url from entry
    video_link = url_entry.get()
    # checking if the entry is empty
    if video_link == '':
        showerror(title='Error', message='Provide the video link please!')
    else:
        try:
            # creating a YouTube object
            video = YouTube(video_link)
            # getting the highest resolution stream
            stream = video.streams.get_highest_resolution()
            # getting the video file path
            file_path = stream.download()
            # converting the video to mp3
            mp.VideoFileClip(file_path).audio.write_audiofile(file_path[:-3] + "mp3")
            # popup for displaying the video converted success message
            showinfo(title='Conversion Complete', message='Video has been converted to MP3 successfully.')
        except:
            # notify the user if errors are caught
            showerror(title='Error', message='An error occurred while converting the video!\n'\
                'Below might be the causes\n->Unstable internet connection\n->Invalid link')


# function to select directory to save the downloaded video
def select_directory():
    # ask the user to select a directory to save the downloaded video
    selected_directory = askdirectory()
    # update the download location text entry with the selected directory
    download_location_entry.delete(0, END)
    download_location_entry.insert(0, selected_directory)


# the function to run the download_video function as a thread   
def downloadThread():
    t2 = threading.Thread(target=download_video)
    t2.start()


# the function to run the searchResolution function as a thread
def searchThread():
    t1 = threading.Thread(target=searchResolution)
    t1.start()


# the function to run the convert_to_mp3 function as a thread
def convertThread():
    t3 = threading.Thread(target=convert_to_mp3)
    t3.start()


# create a new button to convert video to mp3
convert_button = Button(window, text='Convert to MP3', command=convertThread)
convert_button.grid(row=2, column=2, padx=5, pady=5)

# add a new label to display the download location text entry
download_location_label = Label(window, text='Download Location')
download_location_label.grid(row=3, column=0, padx=5, pady=5)

# add a new text entry to display the download location
download_location_entry = Entry(window, width=30)
download_location_entry.grid(row=3, column=1, padx=5, pady=5)

# add a new button to select directory to save the downloaded video
select_directory_button = Button(window, text='Select Directory', command=select_directory)
select_directory_button.grid(row=3, column=2, padx=5, pady=5)
