# Define the candlestick data
candlestick = go.Candlestick(
    x=bitcoin_data.index,
    open=bitcoin_data['Open'],
    high=bitcoin_data['High'],
    low=bitcoin_data['Low'],
    close=bitcoin_data['Close'])

# Create a candlestick figure   
fig = go.Figure(data=[candlestick])
fig.update_layout(title='Bitcoin prices')                        

# Show the plot
fig.show()

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
# QRcode generator
from flask import Flask, render_template, request
import segno
from io import BytesIO
from base64 import b64encode
from PIL import Image

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def generateQR():
    link = request.form.get('link')
    color = request.form.get('color', '#000000')  # Default to black if no color is selected

    # Generate QR code as a PNG image
    qr = segno.make(link)
    memory = BytesIO()
    qr.save(memory, kind='png', scale=10)
    memory.seek(0)
    
    # Open the image with PIL
    qr_image = Image.open(memory).convert("RGBA")
    
    # Convert hex color to RGB
    r, g, b = (int(color[i:i+2], 16) for i in (1, 3, 5))

    # Create a new image to apply the color
    colored_image = Image.new("RGBA", qr_image.size, (255, 255, 255, 0))  # Transparent background
    pixels = qr_image.load()
    new_pixels = colored_image.load()

    for y in range(qr_image.height):
        for x in range(qr_image.width):
            pixel = pixels[x, y]
            if pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0:  # If pixel is black
                new_pixels[x, y] = (r, g, b, pixel[3])  # Apply the selected color
            else:
                new_pixels[x, y] = pixel  # Preserve other colors

    # Save the colored image to memory
    output_memory = BytesIO()
    colored_image.save(output_memory, format='PNG')
    output_memory.seek(0)
    
    # Encode image as base64
    base64_img = 'data:image/png;base64,' + b64encode(output_memory.getvalue()).decode('ascii')
    
    return render_template('index.html', data=base64_img)

if __name__ == '__main__':
    app.run(debug=True)

#html file
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
      href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap"
      rel="stylesheet"
    />
    <title>QR Code Generator</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: "Poppins", sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            text-align: center;
        }
        .container {
            background-color: white;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 500px;
            width: 100%;
        }
        .title {
            margin-bottom: 2rem;
        }
        h1 {
            font-size: 2rem;
            color: #252525;
        }
        h2 {
            font-size: 1.2rem;
            color: #666666;
            margin-bottom: 1.5rem;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }
        input[type="text"] {
            padding: 0.8rem;
            border-radius: 5px;
            border: 1px solid #cccccc;
            font-size: 1rem;
            width: 100%;
        }
        button {
            padding: 0.8rem;
            border-radius: 5px;
            background-color: #252525;
            color: white;
            border: none;
            font-size: 1rem;
            cursor: pointer;
        }
        button:hover {
            background-color: #444444;
        }
        .generated {
            margin-top: 2rem;
            text-align: center;
        }
        .generated img {
            width: 200px;  /* This should make the QR code larger */
            height: auto;
        }       
        .generated p {
            margin-top: 1rem;
            font-size: 1rem;
            color: #333333;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="title">
            <h1>QR Code Generator🔥</h1>
            <h2>Insert a link below to generate a QR code</h2>
        </div>
        <form action="/" method="POST">
            <input type="text" name="link" placeholder="Enter a URL" required />
            <input type="color" name="color" value="#000000" />
            <button type="submit">Generate QR</button>
        </form>
        {% if data %}
        <div class="generated">
            <img src="{{ data }}" alt="Generated QR Code">
            <p>Here is the QR code generated for you!🚀</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
