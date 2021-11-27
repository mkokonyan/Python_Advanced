import json
from tkinter import Button, Label
from gui_shop_demo.helpers import clean_screen
from gui_shop_demo.canvas import tk
from PIL import Image, ImageTk

def render_products():
    clean_screen()
    with open("db/products.txt", "r") as file:
        products = file.readlines()
        column_counter = 1
        for product in products:
            current_product = json.loads(product)
            Label(text=current_product.get("name")).grid(row=0, column=column_counter)
            # TODO render image for
            Button(tk, text=f"Buy {current_product.get('id')}").grid(row=2,column=column_counter)
            column_counter += 1
