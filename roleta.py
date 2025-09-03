import tkinter as tk
from PIL import Image, ImageTk, ImageDraw, ImageFont
import random
import math
import sys
import os

class RoletaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Roleta teste")
        self.root.geometry("600x650")

        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")

        self.base_image = Image.open(os.path.join(base_path, "Roleta.png")).convert("RGBA")

        self.itens = ["Opção 1", "Opção 2", "Opção 3", "Opção 4"]
        self.angulo_atual = 0

        self.canvas = tk.Canvas(root, width=600, height=600, bg="white", highlightthickness=0)
        self.canvas.pack()
        self.roleta_id = self.canvas.create_image(300, 300)

        self.canvas.create_polygon(290, 20, 310, 20, 300, 50, fill="red")

        tk.Button(root, text="Girar", command=self.girar, font=("Arial", 14)).pack(pady=10)

        self.desenhar_roleta()

    def desenhar_roleta(self):
        """Desenha a roleta com os textos nos setores"""
        img = self.base_image.copy()
        draw = ImageDraw.Draw(img)

        n = len(self.itens)
        angulo_por_setor = 360 / n
        raio_texto = 200

        try:
            font = ImageFont.truetype("arial.ttf", 18)
        except:
            font = ImageFont.load_default()

        for i, item in enumerate(self.itens):
            angulo = i * angulo_por_setor + angulo_por_setor / 2
            rad = math.radians(angulo)

            x = img.width/2 + raio_texto * math.cos(rad)
            y = img.height/2 - raio_texto * math.sin(rad)

            draw.text((x-20, y-10), item, fill="white", font=font)

        img_rot = img.rotate(self.angulo_atual, resample=Image.BICUBIC)
        self.current_image = ImageTk.PhotoImage(img_rot)
        self.canvas.itemconfig(self.roleta_id, image=self.current_image)

    def girar(self):
        n = len(self.itens)
        angulo_por_setor = 360 / n
        
        escolhido = random.randint(0, n-1)
        
        angulo_final = 360 * random.randint(5, 8) + (escolhido + 0.5) * angulo_por_setor
        
        while self.angulo_atual < angulo_final:
            self.angulo_atual += 15  
            self.desenhar_roleta()
            self.root.update()
            self.root.after(5)
        
        print("Saiu:", self.itens[escolhido])

if __name__ == "__main__":
    root = tk.Tk()
    app = RoletaApp(root)
    root.mainloop()
