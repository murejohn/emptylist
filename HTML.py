HTML

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kenya Vibes</title>
</head>
<body>

    <header>
        <h1>Welcome to Kenya!</h1>
    </header>

    <section id="multimedia">
        <h2>Experience the Sounds and Sights</h2>

        <div>
            <h3>Local Music</h3>
            <audio src="local_music.mp3" controls>
                Your browser doesn't support the audio element.
            </audio>
        </div>

        <div>
            <h3>Wildlife Wonders</h3>
            <video src="wildlife_video.mp4" controls width="640" height="360">
                Your browser doesn't support the video element.
            </video>
        </div>

        <div>
            <h3>Stunning Scenery</h3>
            <img src="kenyan_landscape.jpg" alt="Beautiful Kenyan Landscape" width="800">
        </div>
    </section>

    <section id="registration">
        <h2>Join Our Community Event</h2>
        <form action="/register" method="post">
            <div>
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required placeholder="Enter your full name">
            </div>
            <div>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required placeholder="Your email address">
            </div>
            <div>
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required minlength="8" placeholder="At least 8 characters">
            </div>
            <div>
                <label for="confirm_password">Confirm Password:</label>
                <input type="password" id="confirm_password" name="confirm_password" required>
            </div>
            <button type="submit">Register</button>
        </form>
    </section>

    <section id="crafts">
        <h2>Kenyan Crafts</h2>
        <table>
            <thead>
                <tr>
                    <th>Craft</th>
                    <th>Description</th>
                    <th>Approximate Price (KES)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Maasai Beads</td>
                    <td>Intricately designed beaded jewelry.</td>
                    <td>500 - 5000</td>
                </tr>
                <tr>
                    <td>Wood Carvings</td>
                    <td>Hand-carved figurines and sculptures.</td>
                    <td>1000 - 10000+</td>
                </tr>
                <tr>
                    <td>Kiondo Baskets</td>
                    <td>Handwoven sisal baskets.</td>
                    <td>800 - 3000</td>
                </tr>
            </tbody>
        </table>
    </section>

    <section id="cuisine">
        <h2>Must-Try Kenyan Dishes</h2>
        <ul>
            <li>Ugali and Sukuma Wiki</li>
            <li>Nyama Choma (Grilled Meat)</li>
            <li>Pilau</li>
            <li>Githeri</li>
            <li>Mandazi (Kenyan Doughnuts)</li>
        </ul>
    </section>

    <footer>
        <p>&copy; 2025 Kenya Vibes</p>
    </footer>

</body>
</html>