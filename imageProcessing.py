from PIL import Image, ImageDraw, ImageFont
import datetime

# OVERLAY THE TEXT ON THE IMAGE
def overlay_text(image_path, text, output_path):
    try:
        # Open the image
        image = Image.open(image_path)

        # Calculate the crop coordinates
        target_width = 1080
        target_height = 1920
        
        width, height = image.size
        x1 = (width - target_width) // 2
        y1 = (height - target_height) // 2
        x2 = x1 + target_width
        y2 = y1 + target_height
        
        # Crop the image
        image = image.crop((x1, y1, x2, y2))
        
        # Create a drawing object
        draw = ImageDraw.Draw(image)
        
        # Set up the font
        #font_path = "/Library/Fonts/arial.ttf"  # Path to your desired font file 
        font_path = "./fonts/Inconsolata-Regular.ttf"
        font_size = 90
        font = ImageFont.truetype(font_path, font_size)
        
        # Set up the text position
        text_position = (50, target_height/3)  # (x, y) coordinates of the text's top-left corner
        
        # Set up the text color
        #text_color = (225, 225, 225)  # RGB values for white
        text_color = (0, 0, 0)  # RGB values for black
    
        # Wrap the text into multiple lines
        max_width = target_width - text_position[0] * 2
        lines = []
        current_line = ""
        words = text.split()
        for word in words:
            test_line = current_line + word + " "
            if draw.textsize(test_line, font=font)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line.strip())
                current_line = word + " "
        lines.append(current_line.strip())
        
        # Draw the text on the image
        line_height = font.getsize('hg')[1]  # Get the height of a line of text
        
        for i, line in enumerate(lines):
            # Calculate the rectangle dimensions based on the line of text
            line_y = text_position[1] + i * line_height

            text_width, text_height = draw.textsize(line, font=font)
            rect_x1 = text_position[0]
            rect_y1 = line_y
            rect_x2 = text_position[0] + text_width
            rect_y2 = line_y + text_height
            
            # Draw the white rectangle
            #draw.rectangle([(rect_x1, rect_y1), (rect_x2, rect_y2)], outline='teal', fill='orange', width=25) 

            
            background = Image.new("RGBA", image.size, (0,0,0,0))
            draw = ImageDraw.Draw(background)
            draw.rounded_rectangle([(rect_x1, rect_y1), (rect_x2, rect_y2)], 30, fill=(255,255,255,100), outline=None)      
            image = Image.composite(background, image, background)


            # Draw the text on the image
            #draw.text((text_position[0], line_y), line, font=font, fill=text_color)

        draw2 = ImageDraw.Draw(image)

        for i, line in enumerate(lines):
            # Calculate the rectangle dimensions based on the line of text
            line_y = text_position[1] + i * line_height
            text_width, text_height = draw2.textsize(line, font=font)

            draw2.text((text_position[0], line_y), line, font=font, fill=text_color)

        
        
        
        # Save the modified image
        current_datetime = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        output_filename = f"{output_path}Motivational_{current_datetime}.jpg"
        print(output_filename)
        image.save(output_filename)
        
        print("Image with overlay text saved successfully!")
        return output_filename
    except Exception as e:
        print(f"Error overlaying text onto the image: {str(e)}")



#font_path = "/fonts/Open_Sans/static/OpenSans_Condensed-Bold.ttf"