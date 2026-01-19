import sys
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from PIL import Image

def create_duplex_visiting_card_pdf(front_img, back_img, output_pdf):
    # A4 size
    page_width, page_height = A4

    # Visiting card size (8.7 cm × 5.2 cm)
    card_width = 3.43 * inch
    card_height = 2.05 * inch

    # Minimal safe margins
    margin_x = 0.3 * inch
    margin_y = 0.3 * inch

    # Calculate max cards that fit
    cols = int((page_width - 2 * margin_x) // card_width)
    rows = int((page_height - 2 * margin_y) // card_height)

    total_cards = cols * rows

    # Center the grid
    grid_width = cols * card_width
    grid_height = rows * card_height
    start_x = (page_width - grid_width) / 2
    start_y = (page_height - grid_height) / 2

    c = canvas.Canvas(output_pdf, pagesize=A4)

    # -------- PAGE 1 : FRONT --------
    Image.open(front_img)  # validation

    for row in range(rows):
        for col in range(cols):
            x = start_x + col * card_width
            y = page_height - start_y - (row + 1) * card_height

            c.drawImage(
                front_img,
                x,
                y,
                width=card_width,
                height=card_height,
                preserveAspectRatio=True,
                mask='auto'
            )

    c.showPage()

    # -------- PAGE 2 : BACK --------
    Image.open(back_img)  # validation

    for row in range(rows):
        for col in range(cols):
            x = start_x + col * card_width
            y = page_height - start_y - (row + 1) * card_height

            c.drawImage(
                back_img,
                x,
                y,
                width=card_width,
                height=card_height,
                preserveAspectRatio=True,
                mask='auto'
            )

    c.showPage()
    c.save()

    print(f"PDF created successfully: {output_pdf}")
    print(f"Cards per page: {total_cards} ({cols} × {rows})")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage:")
        print("python visiting_card_a4_duplex.py front.jpg back.jpg output.pdf")
        sys.exit(1)

    front_image = sys.argv[1]
    back_image = sys.argv[2]
    output_file = sys.argv[3]

    create_duplex_visiting_card_pdf(front_image, back_image, output_file)
