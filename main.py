import streamlit as st
from PIL import Image, ImageDraw

# Function to highlight the angle pairs
def highlight_angles(image_path, angle_pairs, color='red'):
    # Open the image
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Coordinates of the 8 angles
    angle_coords = {
        1: (425,503),  # Coordinates for Angle 1
        2: (569,513),  # Coordinates for Angle 2
        3: (612,592),  # Coordinates for Angle 3
        4: (491,584),  # Coordinates for Angle 4
        5: (756,918),  # Coordinates for Angle 5
        6: (870,923),  # Coordinates for Angle 6
        7: (916,989),  # Coordinates for Angle 7
        8: (817,999)   # Coordinates for Angle 8
    }

    # Highlight the selected angle pairs
    for angle in angle_pairs:
        x, y = angle_coords[angle]
        draw.ellipse([x-20, y-20, x+20, y+20], outline=color, width=5)

    return img

# Streamlit app

st.title("Parallel Lines and Transversal")
st.sidebar.title("M.R. Sarda Kanya Vidya Mandir, Nashik")
st.write("Class 8 Mathematics")
st.write("Submitted by: Vivek Patil")
st.subheader("Select the angle pairs to highlight using the sidebar on the left.")

# Sidebar for selecting angle type and pairs
st.sidebar.title("Angle Selection")

# Image path
image_path = "lines.png"  # Replace with your image file

# Display an empty image initially
highlighted_image = Image.open(image_path)

# Select angle type
angle_type = st.sidebar.radio(
    "Select the type of angle pairs to highlight:",
    ("Alternate Angles", "Corresponding Angles", "Interior Angles")
)

# Highlight based on selected angle type
if angle_type == "Alternate Angles":
    st.sidebar.write("Select the Alternate Angle Pairs:")
    if st.sidebar.checkbox("Pair 1 (4, 6)", key="alt1"):
        highlighted_image = highlight_angles(image_path, [4, 6], color='blue')
    if st.sidebar.checkbox("Pair 2 (3, 5)", key="alt2"):
        highlighted_image = highlight_angles(image_path, [3, 5], color='blue')
    if st.sidebar.checkbox("Pair 3 (1, 7)", key="alt3"):
        highlighted_image = highlight_angles(image_path, [1, 7], color='blue')
    if st.sidebar.checkbox("Pair 4 (2, 8)", key="alt4"):
        highlighted_image = highlight_angles(image_path, [2, 8], color='blue')

elif angle_type == "Corresponding Angles":
    st.sidebar.write("Select the Corresponding Angle Pairs:")
    if st.sidebar.checkbox("Pair 1 (1, 5)", key="corr1"):
        highlighted_image = highlight_angles(image_path, [1, 5], color='green')
    if st.sidebar.checkbox("Pair 2 (2, 6)", key="corr2"):
        highlighted_image = highlight_angles(image_path, [2, 6], color='green')
    if st.sidebar.checkbox("Pair 3 (3, 7)", key="corr3"):
        highlighted_image = highlight_angles(image_path, [3, 7], color='green')
    if st.sidebar.checkbox("Pair 4 (4, 8)", key="corr4"):
        highlighted_image = highlight_angles(image_path, [4, 8], color='green')

elif angle_type == "Interior Angles":
    st.sidebar.write("Select the Interior Angle Pairs:")
    if st.sidebar.checkbox("Pair 1 (4, 5)", key="int1"):
        highlighted_image = highlight_angles(image_path, [4, 5], color='purple')
    if st.sidebar.checkbox("Pair 2 (3, 6)", key="int2"):
        highlighted_image = highlight_angles(image_path, [3, 6], color='purple')

# Display the highlighted image
st.image(highlighted_image, caption="Highlighted Angles")
