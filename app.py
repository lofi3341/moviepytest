import os
import pathlib
import streamlit as st
from moviepy.editor import VideoFileClip

# Function to extract audio from video
def extract_audio(video_path):
    # Load the video clip
    clip = VideoFileClip(video_path)
    
    # Extract audio
    audio_clip = clip.audio
    
    # Save audio to a temporary file
    temp_audio_path = os.path.join('temp', 'extracted_audio.wav')
    audio_clip.write_audiofile(temp_audio_path)
    
    return temp_audio_path

# Main function for Streamlit app
def main():
    st.title('Video Audio Extractor')
    st.write('Upload a video file and extract audio')

    uploaded_file = st.file_uploader("Choose a video file", type=['mp4', 'mov', 'avi'])

    temp_dir = 'temp'
    os.makedirs(temp_dir, exist_ok=True)  # Ensure temp directory exists

    if uploaded_file is not None:
        video_path = os.path.join(temp_dir, uploaded_file.name)
        with open(video_path, 'wb') as f:
            f.write(uploaded_file.read())
        st.success('Video successfully uploaded.')

        if st.button('Extract Audio'):
            st.write('Extracting audio...')
            audio_path = extract_audio(video_path)
            st.success('Audio extracted successfully!')

            st.audio(audio_path, format='audio/wav')
            st.write('Extracted Audio')  # Add caption here

    # Clean up temporary directory
    if os.path.exists(temp_dir):
        for file in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, file)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                st.error(f"Error cleaning up temporary files: {e}")

if __name__ == "__main__":
    main()
