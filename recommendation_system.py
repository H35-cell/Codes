import tkinter as tk
from tkinter import ttk

# Sample data: movies and their genres
movies = {
    "Inception": ["Action", "Sci-Fi"],
    "The Matrix": ["Action", "Sci-Fi"],
    "Toy Story": ["Animation", "Family"],
    "The Lion King": ["Animation", "Family"],
    "The Godfather": ["Crime", "Drama"],
    "Pulp Fiction": ["Crime", "Drama"],
}

# Function to recommend movies based on selected genre
def recommend_movies(selected_genres):
    recommended = []
    for movie, genres in movies.items():
        if any(genre in selected_genres for genre in genres):
            recommended.append(movie)
    return recommended

# Function to handle recommendation request
def on_recommend():
    selected_genres = [genre for genre, var in genre_vars.items() if var.get()]
    recommendations = recommend_movies(selected_genres)
    recommendations_listbox.delete(0, tk.END)
    if recommendations:
        for movie in recommendations:
            recommendations_listbox.insert(tk.END, movie)
    else:
        recommendations_listbox.insert(tk.END, "No recommendations available.")

# Create the main window
root = tk.Tk()
root.title("Movie Recommendation System")

# Create a frame for the genre selection
frame_genres = tk.Frame(root)
frame_genres.pack(padx=10, pady=10)

# Define genres
genres = ["Action", "Sci-Fi", "Animation", "Family", "Crime", "Drama"]

# Create genre checkbuttons
genre_vars = {}
for genre in genres:
    var = tk.BooleanVar()
    chk = tk.Checkbutton(frame_genres, text=genre, variable=var)
    chk.pack(anchor=tk.W)
    genre_vars[genre] = var

# Create a button to get recommendations
btn_recommend = tk.Button(root, text="Get Recommendations", command=on_recommend)
btn_recommend.pack(pady=10)

# Create a listbox to display recommendations
recommendations_listbox = tk.Listbox(root, width=50, height=10)
recommendations_listbox.pack(padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
