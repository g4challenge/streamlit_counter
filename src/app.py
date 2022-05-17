import streamlit as st
from PIL import Image
import tornado
import streamlit as st
from streamlit.server.server import Server

st.set_page_config(
    page_title="(E)Bike-Counter", page_icon=Image.open("assets/favicon.png"), layout="centered", initial_sidebar_state="auto", menu_items=None)

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0b8f6a;
    color: white;
    width: 100px;
    height: 50px;

}
</style>""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    bike_btn = st.button("Bike me", key='bike')

with col2:
    ebike_btn = st.button("Ebike me",  key="ebike")

with open("bike.txt", "r") as f:
    bike = f.readline()  # starts as a string
    bike = 0 if bike == "" else int(bike)  # check if its an empty string, otherwise should be able to cast using int()

with open("ebike.txt", "r") as f:
    ebike = f.readline()  # starts as a string
    ebike = 0 if ebike == "" else int(ebike)  # check if its an empty string, otherwise should be able to cast using int()

if bike_btn: # TODO Tornado call
    bike += 1  
    with open("bike.txt", "w") as f:
        f.truncate()
        f.write(f"{bike}")

with col1:
    bike_element = '<h1 style="font-family:Courier; color:black; font-size: 6em;">{}</h1>'.format(bike)
    st.markdown(bike_element, unsafe_allow_html=True)

if ebike_btn: # TODO Tornado call
    ebike += 1  
    with open("ebike.txt", "w") as f:
        f.truncate()
        f.write(f"{ebike}")

with col2:
    ebike_element = '<h1 style="font-family:Courier; color:black; font-size: 6em;">{}</h1>'.format(ebike)
    st.markdown(ebike_element, unsafe_allow_html=True)

st.balloons()

# Dynamic
#class StreamlitAPIHandler(tornado.web.RequestHandler):
#    def get(self, path):
#        fn = Server.get_current()._api_map.get(path, default_api_handler)
#        result = fn(self.request.arguments)
#        self.write({'message': result})



#def handle_balloons(args):
#    return f"🎈 BALLOONS: {args}"

#Server.get_current().add_api_route('balloons', handle_balloons)

#result = httpx.get('http://localhost:8501/api/balloons')
#st.write(result)
#st.write(result.text)