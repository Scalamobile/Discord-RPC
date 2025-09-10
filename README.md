# Discord-RPC


A user-friendly graphical interface for setting and managing your custom Discord Rich Presence. This tool allows you to easily display custom game activity, status, images, and buttons on your Discord profile without needing to write any code.

## Features

*   **Easy-to-Use GUI**: A simple interface built with Tkinter to manage all Rich Presence settings.
*   **Full Customization**: Set details, state, large and small images, and a start timestamp.
*   **Clickable Buttons**: Add up to two custom buttons with labels and URLs to your presence.
*   **Profile Management**: Save and load different Rich Presence configurations for quick switching.
*   **Live Elapsed Timer**: See a running timer on the GUI that matches the one displayed on Discord.
*   **Persistent Profiles**: Your saved profiles are stored locally in an `rpc_profiles.json` file.

## Installation

This script requires Python 3 and the `pypresence` library.

1.  Clone the repository:
    ```sh
    git clone https://github.com/scalamobile/discord-rpc.git
    cd discord-rpc
    ```

2.  Install the required dependency:
    ```sh
    pip install pypresence
    ```

## How to Use

1.  **Run the application**:
    ```sh
    python index.py
    ```

2.  **Get your Client ID**:
    *   Go to the [Discord Developer Portal](https://discord.com/developers/applications).
    *   Create a new application.
    *   Navigate to the "OAuth2" page and copy your "Client ID".

3.  **Fill in the fields in the GUI**:
    *   **Client ID**: Paste the Client ID from your Discord application. This field is required.
    *   **Details**: The first line of text for your presence.
    *   **State**: The second line of text.
    *   **Large/Small Image Key**: The name of the image assets you uploaded under "Rich Presence" -> "Art Assets" in your Discord application settings.
    *   **Start Time**: The timestamp for the elapsed time counter. Can be in `YYYY-MM-DD HH:MM:SS` format or a Unix timestamp. If left empty, it defaults to the current time when you start the RPC.
    *   **Button 1/2 Label & URL**: The text and link for the clickable buttons. Both a label and a URL are required for a button to appear.

4.  **Manage Profiles**:
    *   **To Save**: Enter a name in the text box next to the profile dropdown and click **Save profile**.
    *   **To Load**: Select a previously saved profile from the dropdown menu to auto-fill the fields.

5.  **Control the Presence**:
    *   Click **Start RPC** to activate your Rich Presence on Discord.
    *   Click **Stop RPC** to deactivate it.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
