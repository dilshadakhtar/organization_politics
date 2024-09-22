import streamlit as st

# Initialize game state variables for two players
if "player1_power" not in st.session_state:
    st.session_state.player1_power = 50
if "player1_influence" not in st.session_state:
    st.session_state.player1_influence = 50
if "player2_power" not in st.session_state:
    st.session_state.player2_power = 50
if "player2_influence" not in st.session_state:
    st.session_state.player2_influence = 50
if "turn" not in st.session_state:
    st.session_state.turn = 1  # Tracks whose turn it is


# Function to check if the game is over
def check_game_over():
    if st.session_state.player1_power >= 100 and st.session_state.player1_influence >= 100:
        st.success("Player 1 has won the Game of Thrones and now rules the organizational kingdom!")
        return True
    elif st.session_state.player2_power >= 100 and st.session_state.player2_influence >= 100:
        st.success("Player 2 has won the Game of Thrones and now rules the organizational kingdom!")
        return True
    elif st.session_state.player1_power <= 0 or st.session_state.player1_influence <= 0:
        st.error("Player 1 has lost all power and influence. Player 2 wins!")
        return True
    elif st.session_state.player2_power <= 0 or st.session_state.player2_influence <= 0:
        st.error("Player 2 has lost all power and influence. Player 1 wins!")
        return True
    return False


# Function to display the status of both players
def display_status():
    st.write(
        f"**Player 1 - Power:** {st.session_state.player1_power}, **Influence:** {st.session_state.player1_influence}")
    st.write(
        f"**Player 2 - Power:** {st.session_state.player2_power}, **Influence:** {st.session_state.player2_influence}")


# Game introduction
st.title("Organizational Politics: Game of Thrones Edition (Two Players)")
st.subheader("Welcome to the Game of Organizational Politics!")
st.write("Players will take turns navigating the treacherous world of organizational politics.")
st.write("Each player will make decisions to either increase or decrease their power and influence.")

# Display the current status of both players
st.header("Current Status")
display_status()

# Check if the game is over before proceeding
if not check_game_over():
    # Display whose turn it is
    if st.session_state.turn == 1:
        st.subheader("Player 1's Turn")
    else:
        st.subheader("Player 2's Turn")

    # Make decisions for the current player
    if st.session_state.turn == 1:
        # Player 1's options
        if st.button("Player 1: Build alliances with key stakeholders"):
            st.session_state.player1_influence += 20
            st.session_state.player1_power += 10
            st.write("Player 1 built alliances, gaining influence and power.")
            st.session_state.turn = 2  # Switch to Player 2's turn after Player 1 acts

        if st.button("Player 1: Sabotage Player 2"):
            st.session_state.player1_power += 30
            st.session_state.player2_power -= 20
            st.session_state.player1_influence -= 10
            st.write("Player 1 sabotaged Player 2, gaining power but losing some influence.")
            st.session_state.turn = 2

        if st.button("Player 1: Play neutral"):
            st.session_state.player1_power += 5
            st.session_state.player1_influence += 5
            st.write("Player 1 played neutral, making small gains.")
            st.session_state.turn = 2

        if st.button("Player 1: Backstab an ally"):
            st.session_state.player1_power += 40
            st.session_state.player1_influence -= 20
            st.write("Player 1 backstabbed an ally, gaining significant power but losing influence.")
            st.session_state.turn = 2

        if st.button("Player 1: Align with senior management"):
            st.session_state.player1_power += 25
            st.session_state.player1_influence += 15
            st.write("Player 1 aligned with senior management, boosting both power and influence.")
            st.session_state.turn = 2

    else:
        # Player 2's options
        if st.button("Player 2: Build alliances with key stakeholders"):
            st.session_state.player2_influence += 20
            st.session_state.player2_power += 10
            st.write("Player 2 built alliances, gaining influence and power.")
            st.session_state.turn = 1  # Switch back to Player 1's turn after Player 2 acts

        if st.button("Player 2: Sabotage Player 1"):
            st.session_state.player2_power += 30
            st.session_state.player1_power -= 20
            st.session_state.player2_influence -= 10
            st.write("Player 2 sabotaged Player 1, gaining power but losing some influence.")
            st.session_state.turn = 1

        if st.button("Player 2: Play neutral"):
            st.session_state.player2_power += 5
            st.session_state.player2_influence += 5
            st.write("Player 2 played neutral, making small gains.")
            st.session_state.turn = 1

        if st.button("Player 2: Backstab an ally"):
            st.session_state.player2_power += 40
            st.session_state.player2_influence -= 20
            st.write("Player 2 backstabbed an ally, gaining significant power but losing influence.")
            st.session_state.turn = 1

        if st.button("Player 2: Align with senior management"):
            st.session_state.player2_power += 25
            st.session_state.player2_influence += 15
            st.write("Player 2 aligned with senior management, boosting both power and influence.")
            st.session_state.turn = 1

    # After each turn, display updated status
    st.header("Updated Status")
    display_status()

    # Check the outcome after each turn
    check_game_over()

# If game is over, display the endgame message
if st.session_state.turn == 0:
    st.write("The game has ended. Thank you for playing!")
