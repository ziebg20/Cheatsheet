import tkinter as tk
from PIL import Image, ImageDraw, ImageFont, ImageTk
import random

class Magic8BallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Magic 8-Ball")

        self.canvas = tk.Canvas(root, width=600, height=600)
        self.canvas.pack()

        self.draw_8ball()
        
        self.question_label = tk.Label(root, text="Ask the Magic 8-Ball a question:")
        self.question_label.pack()
        
        self.question_entry = tk.Entry(root, width=50)
        self.question_entry.pack()
        
        self.ask_button = tk.Button(root, text="Ask", command=self.give_answer)
        self.ask_button.pack()
        
        self.answer_label = tk.Label(root, text="", font=("Arial", 14), wraplength=300)
        self.answer_label.pack()
        
        self.responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes – definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
    
    def draw_8ball(self):
        # Create an image with a black circle and a white square in the middle
        image_size = (600, 600)
        circle_center = (300, 300)
        circle_radius = 300
        square_size = 250

        self.image = Image.new("RGB", image_size, "white")
        self.draw = ImageDraw.Draw(self.image)

        # Draw black circle
        self.draw.ellipse((circle_center[0] - circle_radius, circle_center[1] - circle_radius,
                      circle_center[0] + circle_radius, circle_center[1] + circle_radius), fill="black")

        # Draw white square in the middle
        self.draw.rectangle((circle_center[0] - square_size//2, circle_center[1] - square_size//2,
                        circle_center[0] + square_size//2, circle_center[1] + square_size//2), fill="purple")

        # Convert the image to a PhotoImage
        self.ball_photo = ImageTk.PhotoImage(self.image)

        # Display the image on the canvas
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.ball_photo)
    
    def give_answer(self):
        answer = random.choice(self.responses)
        
        # Load a font
        font = ImageFont.truetype("arial.ttf", 24)
        
        # Calculate text size and position
        text_bbox = self.draw.textbbox((0, 0), answer, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        text_x = (600 - text_width) // 2
        text_y = (600 - text_height) // 2
        
        # Redraw the 8-ball and draw the answer in the white square
        self.draw_8ball()
        self.draw.text((text_x, text_y), answer, fill="black", font=font)
        
        # Update the canvas with the new image
        self.ball_photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.ball_photo)

if __name__ == "__main__":
    root = tk.Tk()
    app = Magic8BallApp(root)
    root.mainloop()
