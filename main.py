import tkinter
from PIL import ImageTk
from pytube import YouTube



root = tkinter.Tk()
root.title("YouTube Downloader")
root.geometry("800x600")
root.config(bg="brown")
root.resizable(0, 0)
root.iconbitmap("youtube_icon.ico")

# function for the download functionality.
def download_function():
    url = input_feild.get()
    if url == "" or url == " ":
        pass
    else:
        print(url)
        my_video = YouTube(url)
        message = f"{my_video.title}, downloading"
        url_label = tkinter.Label(texboxFrame, font=("Arial",10, "bold"), text=message)
        url_label.grid(padx=5, pady=10)
        my_video = my_video.streams.get_highest_resolution()
        root.title(my_video.title)
        my_video.download()
        download_message = f"DOWNLOADING COMPLETED. go to the folder of this App."
        download_message_label = tkinter.Label(texboxFrame, font=("Arial", 10, "bold"), text=download_message)
        download_message_label.grid(padx=5, pady=10)

bodyFrame = tkinter.Frame(root, width=800, height=600, highlightcolor="white",highlightthickness=5, bg="brown")
bodyFrame.pack()
topFrame = tkinter.Frame(bodyFrame, width=800, highlightcolor="white", highlightthickness=3, height=70, bg="black")
topFrame.pack(pady=10, padx=10)
label1 = tkinter.Label(topFrame, text="SuperTube Video Downloader", bg="brown", font=("Arial", 25, "bold"))
label1.pack(pady=10,padx=5)

middleFrame = tkinter.Frame(bodyFrame, width=800, height=30, bg="brown")
middleFrame.pack()
# cover_img = ImageTk.PhotoImage(file="project_image.jpg")
img_label = tkinter.Label(middleFrame, text="Go to YouTube, copy the video link and paste it in the textbox below.", bg="brown", font=("Arial",16,"italic"), fg="black")
img_label.pack()

bottomFrame = tkinter.Frame(bodyFrame, width=800, height=400, bg="black",highlightbackground="white", highlightcolor="white", highlightthickness=2)
bottomFrame.pack(padx=3)
texboxFrame = tkinter.Frame(bottomFrame, width=800, height=200, bg="brown")
texboxFrame.pack()

#Adding the labe.
label3 = tkinter.Label(texboxFrame, text="Paste Video Link : ", font=("Arial", 13, "bold"))
label3.grid(row=0, column=0)

input_feild = tkinter.Entry(texboxFrame, width=50, font=("Arial", 15, "italic"))
input_feild.grid(pady=20, padx=5)

download_button = tkinter.Button(texboxFrame, text="DOWNLOAD", font=("Arial", 20, "bold"), command=download_function)
download_button.grid(pady=20, padx=5)

#Footer frame.
footer = tkinter.Frame(bodyFrame,width=800,height=50,bg="black")
footer.pack(padx=10, pady=10)
label2 = tkinter.Label(footer, text="Copyrights @ JOB ABE", bg="brown", font=("Arial", 25, "bold"))
label2.pack(pady=10,padx=5)

bottomFrame.pack_propagate(False)
middleFrame.pack_propagate(False)
topFrame.pack_propagate(False)
bodyFrame.pack_propagate(False)




root.mainloop()