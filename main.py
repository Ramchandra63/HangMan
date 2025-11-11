from words import words
import random
import streamlit as st
from hangman import HANGMAN_PICS

st.set_page_config(page_title="Hangman Game 🎯", page_icon="🎮")
st.title('🎯 Hangman Game')
st.write("Guess the word one letter at a time!")

if 'word_to_guess' not in st.session_state:
    st.session_state.word_to_guess = None
    st.session_state.guessed_letters = []
    st.session_state.lives = 6
    st.session_state.game_over = False
    st.session_state.game_started = False

if st.button('🎮 New Game'):
    st.session_state.word_to_guess = random.choice(words).lower()
    st.session_state.guessed_letters = []
    st.session_state.lives = 6
    st.session_state.game_over = False
    st.session_state.game_started = True
    st.rerun()

if st.session_state.game_started and st.session_state.word_to_guess:
    word_to_guess = st.session_state.word_to_guess
    guessed_letters = st.session_state.guessed_letters
    lives = st.session_state.lives


    st.markdown(f"```\n{HANGMAN_PICS[6 - lives]}\n```")


    st.write(f"❤️ Lives remaining: {lives}/6")


    display = ""
    for letter in word_to_guess:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    st.markdown(f"## {display}")

    if not st.session_state.game_over:
        if "_" not in display:
            st.session_state.game_over = True
            st.success("🎉 You WIN the game! Congratulations!")
            st.balloons()
        elif lives == 0:
            st.session_state.game_over = True
            st.error(f"😥 Game Over! The word was: **{word_to_guess}**")
    if st.session_state.game_over:
        if lives > 0:
            st.success(f"🎉 You WIN the game! The word was: **{word_to_guess.upper()}**")
            st.balloons()
        else:
            st.error(f"😥 Game Over! You lose. The word was: **{word_to_guess.upper()}**")


    if not st.session_state.game_over:
        st.write("### Select a letter:")


        keyboard_rows = [
            'QWERTYUIOP',
            'ASDFGHJKL',
            'ZXCVBNM'
        ]

        for row in keyboard_rows:
            cols = st.columns(len(row))
            for idx, letter in enumerate(row):
                with cols[idx]:
                    letter_lower = letter.lower()
                    if letter_lower in guessed_letters:
                        st.button(letter, disabled=True, key=f"btn_{letter}")
                    else:
                        if st.button(letter, key=f"btn_{letter}"):
                            st.session_state.guessed_letters.append(letter_lower)

                            if letter_lower not in word_to_guess:
                                st.session_state.lives -= 1
                                if st.session_state.lives == 0:
                                    st.session_state.game_over = True

                            st.rerun()

        if guessed_letters:
            st.write(f"**Guessed letters:** {', '.join(sorted(guessed_letters)).upper()}")
    else:
        if guessed_letters:
            st.write(f"**Guessed letters:** {', '.join(sorted(guessed_letters)).upper()}")
        st.write("Click 'New Game' to play again!")
else:
    st.info("👆 Click 'New Game' to start playing!")