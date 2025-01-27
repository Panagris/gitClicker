from flask import Flask, redirect

app = Flask(__name__)

# Variable to store click count
click_count = 0


@app.route('/r/<path:spotify_id>')
def track_and_redirect(spotify_id):
    global click_count
    click_count += 1  # Increment click count
    # Construct the Spotify URL
    spotify_url = f"https://open.spotify.com/track/{spotify_id}"
    return redirect(spotify_url)  # Redirect to Spotify


@app.route('/clicks')
def get_clicks():
    global click_count
    return {"clicks": click_count}  # Return the click count as JSON


@app.route('/reset-clicks', methods=['POST'])
def reset_clicks():
    global click_count
    click_count = 0  # Reset the click count
    return {"message": "Click count reset successfully", "clicks": click_count}, 200


if __name__ == "__main__":
    app.run(debug=True)
