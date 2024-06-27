import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser

# Initialize the main window
root = tk.Tk()
root.title("Leuphana Community App")
screen_width, screen_height = 414, 896
root.geometry(f"{screen_width}x{screen_height}")

# Define global variables
formal_font = ("Arial", 16)
formal_font_bold = ("Arial", 16, "bold")
heading_font = ("Arial", 18, "bold")
event_font = ("Arial", 16, "italic")

# Define colors
background_color = "#f2f0f0"
accent_color = "#8B0000"
text_color = "#4B4B4B"
button_bg_color = "#ffffff"
button_active_bg_color = "#d3d3d3"

# Set background color for the root window
root.configure(bg=background_color)

# Function to clear all widgets from a given frame
def clear_widgets(root):
    for i in root.winfo_children():
        i.destroy()

# Function to set background image for a given frame (root window)
def set_background(frame, image_file_path):
    clear_widgets(frame)  # Clear existing widgets before setting background
    abs_path = os.path.join(os.path.dirname(__file__), image_file_path)
    img = Image.open(abs_path).resize((screen_width, screen_height), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    label = tk.Label(frame, image=img)
    label.image = img
    label.place(x=0, y=0, relwidth=1, relheight=1)  # Place image in the frame

# Function to open a URL in the web browser
def open_url(url):
    webbrowser.open(url)

# Function to create the welcome page
def create_welcome_page():
    set_background(root, "images/homepage.jpg")

    find_people_button = tk.Button(root, text="JOIN US!", font=formal_font_bold, bg=button_bg_color,
                                   activebackground=button_active_bg_color, fg=accent_color, bd=0,
                                   command=create_main_features_page)
    find_people_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

# Function to create the main features page
def create_main_features_page():
    set_background(root, "images/features_background.jpg")

    title_label = tk.Label(root, text="LEUPHANA", font=heading_font, fg=accent_color, bg=background_color)
    title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    subtitle_label = tk.Label(root, text="COMMUNITY APP", font=heading_font, fg=accent_color, bg=background_color)
    subtitle_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

    # Define feature buttons with their respective labels and commands
    feature_buttons = [
        ("Information Hub", lambda: create_info_hub()),
        ("Community Forum", lambda: create_community_forum()),
        ("Well-being Resources", lambda: create_wellbeing_page()),
        ("Community Connections", lambda: create_community_connections_page())
    ]

    # Create buttons for each feature with appropriate formatting
    for index, (feature, command) in enumerate(feature_buttons, start=1):
        feature_button = tk.Button(root, text=feature, font=formal_font_bold,  # Use formal_font_bold for all buttons
                                   fg=accent_color,  # Use accent_color for all buttons
                                   bg=button_bg_color,
                                   activebackground=button_active_bg_color, bd=0, command=command)
        # Place buttons in a vertical column in the middle of the window
        button_y_position = screen_height * 0.3 + (index - 1) * 70
        feature_button.place(relx=0.5, rely=0.3 + (index - 1) * 0.1, anchor=tk.CENTER)
    feature_button.place(relx=0.5, rely=0.3 + (index - 1) * 0.1, anchor=tk.CENTER)

# Function to create the information hub page
def create_info_hub():
    set_background(root, "images/info_hub.jpg")
    tk.Label(root, text="Information Hub", font=formal_font_bold, bg=background_color).place(relx=0.5, y=100,
                                                                                             anchor=tk.CENTER)

    info_text = """Welcome to the Information Hub!"""
    tk.Label(root, text=info_text, font=formal_font, wraplength=screen_width - 40, bg=background_color).place(relx=0.5,
                                                                                                              y=200,
                                                                                                              anchor=tk.CENTER)

    # Buttons to navigate to specific resources
    tk.Button(root, text="Visit Library", command=lambda: open_url("https://www.leuphana.de/services/miz/literaturrecherche/digitale-bibliothek.html"),
              font=formal_font, bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=300, anchor=tk.CENTER)
    tk.Button(root, text="Student Services", command=lambda: open_url("https://www.leuphana.de/en/services/student-service.html"),
              font=formal_font, bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=350, anchor=tk.CENTER)

    # Button to return to main features page
    tk.Button(root, text="Back to Features", command=create_main_features_page, font=formal_font_bold,
              bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=400,
                                                                                                      anchor=tk.CENTER)

# Function to create the community forum page
def create_community_forum():
    set_background(root, "images/community_forum.jpg")
    tk.Label(root, text="Community Forum", font=formal_font_bold, bg=background_color).place(relx=0.5, y=100,
                                                                                             anchor=tk.CENTER)

    forum_text = """Welcome to the Community Forum!
    Share your thoughts, ask questions, and connect with other students."""
    tk.Label(root, text=forum_text, font=formal_font, wraplength=screen_width - 40, bg=background_color).place(relx=0.5,
                                                                                                               y=200,
                                                                                                               anchor=tk.CENTER)

    # create the Chatbot
    global text_box, entry_box

    text_box = tk.Text(root, bg="#17202A", fg="#EAECEE", font="Helvetica 14", width=60)
    text_box.place(x=0, y=250, relwidth=1, relheight=0.4)

    scroll_bar = tk.Scrollbar(text_box)
    scroll_bar.place(relheight=1, relx=0.974)

    entry_box = tk.Entry(root, bg="#2C3E50", fg="#EAECEE", font="Helvetica 14", width=55)
    entry_box.place(x=5, rely=0.7, relwidth=0.7, relheight=0.05)

    send_button = tk.Button(root, text="Send", font="Helvetica 13 bold", bg="#ABB2B9", command=send_message, width=10)
    send_button.place(relx=0.77, rely=0.7, relwidth=0.2, relheight=0.05)

    # create a button to return to main features page
    tk.Button(root, text="Back to Features", command=create_main_features_page, font=formal_font_bold,
              bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=700,
                                                                                                      anchor=tk.CENTER)

# Function to create the wellbeing page
def create_wellbeing_page():
    set_background(root, "images/wellbeing.jpg")
    tk.Label(root, text="Well-being Resources", font=formal_font_bold, bg=background_color).place(relx=0.5, y=100,
                                                                                                  anchor=tk.CENTER)

    wellbeing_text = """Well-being Tips:
    - Tip 1: Stay active and exercise regularly.
    - Tip 2: Maintain a balanced diet.
    - Tip 3: Get enough sleep and rest.
    - Tip 4: Take breaks and manage stress effectively."""
    tk.Label(root, text=wellbeing_text, font=formal_font, wraplength=screen_width - 40, bg=background_color).place(
        relx=0.5, y=200, anchor=tk.CENTER)

    # Buttons to access wellbeing resources
    tk.Button(root, text="Contact Counselor", command=lambda: open_url("https://stw-on.de/en/lüneburg/counselling/psychotherapeutic-counselling-centre-2-2"),
              font=formal_font, bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=300, anchor=tk.CENTER)
    tk.Button(root, text="Book Appointment", command=lambda: open_url("https://www.doctolib.de/"),
              font=formal_font, bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=350, anchor=tk.CENTER)
    tk.Button(root, text="Visit University Sports Page", command=lambda: open_url("https://www.leuphana.de/services/hochschulsport.html"),
              font=formal_font, bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=400, anchor=tk.CENTER)

    # Button to return to main features page
    tk.Button(root, text="Back to Features", command=create_main_features_page, font=formal_font_bold,
              bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=450,
                                                                                                      anchor=tk.CENTER)

# Function to create the community connections page
def create_community_connections_page():
    clear_widgets(root)
    set_background(root, "images/community_connections.jpg")  # Assuming you have an appropriate image for this page

    tk.Label(root, text="Community Connections", font=formal_font_bold, bg=background_color).place(relx=0.5, y=50,
                                                                                                      anchor=tk.CENTER)

    # Buttons to join various community groups
    tk.Button(root, text="Join Flohmarkt Group", command=lambda: open_url("https://t.me/joinchat/VWR-V8VWp2_GOs1F"),
              font=formal_font, bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=100, anchor=tk.CENTER)
    tk.Button(root, text="Join Sharing is Caring", command=lambda: open_url("https://kurzelinks.de/gc8u"),
              font=formal_font, bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=150, anchor=tk.CENTER)
    tk.Button(root, text="Join International Group", command=lambda: open_url("https://t.me/leuphana_internationals"),
              font=formal_font, bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=200, anchor=tk.CENTER)
    tk.Button(root, text="Join Digital Media Students", command=lambda: open_url("https://chat.whatsapp.com/EP3Svyshxp956ZU7yJ6qnv"),
              font=formal_font, bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=250, anchor=tk.CENTER)

    # Button to return to main features page
    tk.Button(root, text="Back to Features", command=create_main_features_page, font=formal_font_bold,
              bg=button_bg_color, activebackground=button_active_bg_color, fg=text_color, bd=0).place(relx=0.5, y=350, anchor=tk.CENTER)


# Function to send a message in the community forum
def send_message():
    message = entry_box.get()
    if message:
        text_box.config(state=tk.NORMAL)
        text_box.insert(tk.END, "You: " + message + "\n")
        text_box.config(state=tk.DISABLED)
        entry_box.delete(0, tk.END)

        response = get_bot_response(message)
        text_box.config(state=tk.NORMAL)
        text_box.insert(tk.END, "Bot: " + response + "\n")
        text_box.config(state=tk.DISABLED)
        text_box.see(tk.END)

# Function to get a bot response in the community forum
def get_bot_response(message):
    responses = {
        "hello": "Hello! Welcome to the Leuphana Community Forum",
        "hi": "Hi there! Welcome to the Leuphana Community Forum",
        "help": "Sure, I'm here to help. What do you need assistance with?",
        "bye": "Goodbye! Have a great day!"
    }
    return responses.get(message.lower(), "I'm sorry, I don't understand that.")

# Call the welcome page to start the app
create_welcome_page()

# Run the main event loop
root.mainloop()
