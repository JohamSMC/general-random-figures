import os
import random

import drawSvg as draw
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg
from tqdm import tqdm

line_thickness = 0.5
pattern_figures = []


def check_folder():
    if not os.path.isdir('figures-SVG'):
        os.makedirs('figures-SVG')

    if not os.path.isdir('figures-PNG'):
        os.makedirs('figures-PNG')

    if not os.path.isdir('figures-PDF'):
        os.makedirs('figures-PDF')


def read_input_values():
    number_figures: int = int(input("Type the number of figures: "))

    png = ""
    while (png != "YES") and (png != "NO"):
        png = input("You want the figures in PNG format(Yes/No): ").upper()
    png: bool = True if png == "YES" else False

    pdf = ""
    while (pdf != "YES") and (pdf != "NO"):
        pdf = input("You want the figures in PDF format(Yes/No): ").upper()
    pdf: bool = True if pdf == "YES" else False

    return number_figures, png, pdf


def save_figures(window: draw, num_figure: int, png: bool, pdf: bool):
    window.saveSvg(f"figures-SVG/figure_{num_figure}.svg")

    if png:
        window.savePng(f"figures-PNG/figure_{num_figure}.png")

    if pdf:
        drawing = svg2rlg(f"figures-SVG/figure_{num_figure}.svg")
        renderPDF.drawToFile(drawing, f"figures-PDF/figure_{num_figure}.pdf")


def main():

    number_figures, png, pdf = read_input_values()

    for num_figure in tqdm(range(1, number_figures+1)):
        window = draw.Drawing(40, 50, origin=(0, 0), displayInline=False)
        window.append(draw.Rectangle(
            5, 5, 30, 40, stroke_width=line_thickness, fill="white", stroke="black"))

        current_pattern_unique = False
        while not current_pattern_unique:
            vertical_line_position = random.randint(6, 34)  # 6,34
            horizontal_line_position = random.randint(6, 44)  # 6,44
            radius_circle_1 = random.randint(2, 48)  # 2,48
            radius_circle_2 = random.randint(2, 48)  # 2,48
            radius_circle_3 = random.randint(2, 48)  # 2,48
            radius_circle_4 = random.randint(2, 48)  # 2,48

            current_figure_pattern = f"LV-{vertical_line_position};LH-{horizontal_line_position};"
            "C1-{radius_circle_1};C2-{radius_circle_2};C3-{radius_circle_3};C4-{radius_circle_4}"

            if (num_figure == 1) or (current_figure_pattern not in pattern_figures):
                current_pattern_unique = True
                pattern_figures.append(current_figure_pattern)

                # Linea Horizontal
                window.append(
                    draw.Line(
                        0, horizontal_line_position, 40, horizontal_line_position,
                        stroke_width=line_thickness, fill='none', stroke='black'))
                # Linea Vertical
                window.append(
                    draw.Line(
                        vertical_line_position, 0, vertical_line_position, 50,
                        stroke_width=line_thickness, fill='none', stroke='black'))

                # window.append(draw.Line(0, 6, 40, 6, stroke_width=line_thickness, fill='none', stroke='black')) # Linea Horizontal - Limite Inferior
                # window.append(draw.Line(0, 44, 40, 44, stroke_width=line_thickness, fill='none', stroke='black')) # Linea Horizontal - Limite Superior

                # window.append(draw.Line(6, 0, 6, 50, stroke_width=line_thickness, fill='none', stroke='black')) # Linea Vertical - Limite Inferior
                # window.append(draw.Line(34, 0, 34, 50, stroke_width=line_thickness, fill='none', stroke='black')) # Linea Vertical - Limite Superior

                # window.append(draw.Line(5, 5, 35, 45, stroke_width=line_thickness, fill='none', stroke='black')) # Linea Transversal 1
                # window.append(draw.Line(5, 45, 35, 5, stroke_width=line_thickness, fill='none', stroke='black')) # Linea Transversal 2

                window.append(draw.Circle(35,  45, radius_circle_1, stroke_width=line_thickness,
                                          fill='none', stroke='black'))  # Circulo cuadrante 1
                window.append(draw.Circle(5,  45, radius_circle_2, stroke_width=line_thickness,
                                          fill='none', stroke='black'))  # Circulo cuadrante 2
                window.append(draw.Circle(5,  5, radius_circle_3, stroke_width=line_thickness,
                                          fill='none', stroke='black'))  # Circulo cuadrante 3
                window.append(draw.Circle(35,  5, radius_circle_4, stroke_width=line_thickness,
                                          fill='none', stroke='black'))  # Circulo cuadrante 4

                # window.append(draw.Circle(5,  45, 48, stroke_width=line_thickness, fill='none', stroke='black')) # Circulo cuadrante 2

                # window.append(draw.Circle(0,  0, 10, stroke_width=1, fill='none', stroke='black'))
                # window.append(draw.Circle(40,  50, 10, stroke_width=1, fill='none', stroke='black'))

                clean_edges(window)

                window.setPixelScale(4)  # Set number of pixels per geometry unit
                # window.setRenderSize(113, 151)  # Alternative to setPixelScale

                save_figures(window, num_figure, png, pdf)

    print("----------------------------------------------")
    print("COMPLETED SCRIPT")
    print("Figures in SVG format : " + str(number_figures))
    print("Figures in PNG format : " + str(number_figures if png else 0))
    print("Figures in PDF format : " + str(number_figures if pdf else 0))
    print("----------------------------------------------")


def clean_edges(window: draw):
    window.append(draw.Rectangle(
        0, 0, 5, 50, stroke_width=line_thickness, fill="white", stroke="none"))
    window.append(draw.Line(
        5, 5, 5, 45, stroke_width=line_thickness, fill='none', stroke='black'))

    window.append(draw.Rectangle(
        0, 0, 40, 5, stroke_width=line_thickness, fill="white", stroke="none"))
    window.append(draw.Line(
        5, 5, 35, 5, stroke_width=line_thickness, fill='none', stroke='black'))

    window.append(draw.Rectangle(
        35, 0, 5, 50, stroke_width=line_thickness, fill="white", stroke="none"))
    window.append(draw.Line(
        35, 5, 35, 45, stroke_width=line_thickness, fill='none', stroke='black'))

    window.append(draw.Rectangle(
        0, 45, 50, 5, stroke_width=line_thickness, fill="white", stroke="none"))
    window.append(draw.Line(
        5, 45, 35, 45, stroke_width=line_thickness, fill='none', stroke='black'))


if __name__ == '__main__':
    check_folder()
    main()
