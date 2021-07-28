# dim-explorer

## How to build?

docker build -f Dockerfile -t dim-explorer:latest .

## How to run?

docker run -p 8501:8501 dim-explorer:latest



## Some code snippets

'''
img_file_buffer = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))


chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

option = st.sidebar.selectbox(
    'Select an Analyzer?',
     pd.DataFrame({
        'second column': ['Prediction', 'Time aggregate', 'Dimension aggregate', 'Other']
    }))

'You selected:', option

'''
