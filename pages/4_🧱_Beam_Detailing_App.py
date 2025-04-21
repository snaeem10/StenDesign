import streamlit as st
import math
import pandas as pd
from io import BytesIO



def get_bar_area(bar_designation):
    bar_areas = {'#4': 0.20, '#5': 0.31 ,'#6':0.44 ,'#7':0.60,'#8':0.79,'#9':1.00,'#10':1.27}
    if bar_designation in bar_areas:
        return bar_areas[bar_designation]
    else:
        raise ValueError("Bar designation not supported.")
def get_bar_areaSI(bar_designation):
    bar_areas = {'T8': 50.3, 'T10': 78.5 ,'T12':113.1 ,'T16':201.1,'T20':314.2,'T25':490.9,'T32':804.2}
    if bar_designation in bar_areas:
        return bar_areas[bar_designation]
    else:
        raise ValueError("Bar designation not supported.")

st.set_page_config(page_title="Beam Detailing App")
st.title("BEAM DETAILING SOFTWARE")
st.markdown("""
    <style>
        .big-heading {
            font-size: 24px;
            font-weight: bold;
            color: #FFFFFF;
        }
    </style>
""", unsafe_allow_html=True)

# Display the custom styled heading
st.markdown('<p class="big-heading">Hey Welcome to Sten-Design .</p>', unsafe_allow_html=True)
st.markdown("""
Instructions

1. This App will give you beam deatil.  
2. Upload your beam reinforcing area in excel format shared below .  
3. If you want the beam reinforcement area from ETABS in the format shared below with just one click Download our application.
""")
if st.button("⬇️ Download Application"): 
    st.markdown("[Click to download from Drive](https://drive.google.com/file/d/164T8lA6qM9z5wgfiRReACpAeGaYevIl1/view?usp=sharing)")
st.markdown("""
            
4. The File  geenerated from the application will be uploaded here.
Instructions""")

# File uploader
uploaded_file = st.file_uploader("", type=["xlsx"])
st.header("Excel Upload Format")

st.markdown("""
<div style="background-color: #7AFF5F49; padding: 20px; border-radius: 6px; opacity: 0.8;">


<div style="overflow-x: auto;">
  <table style="width: max-content; border-collapse: collapse;">
    <tr>
      <th>Beam Mark</th><th>LFT</th><th>RFT</th><th>MFT</th><th>LFB</th><th>RFB</th><th>MFB</th><th>LTT</th><th>MTT</th><th>RTT</th><th>LTB</th><th>MTB</th><th>RTB</th>
    </tr>
    <tr>
      <td>17</td><td>0.186</td><td>0.181</td><td>0.037</td><td>0.062</td><td>0.060</td><td>0.185</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td><td>0.000</td>
    </tr>
    <tr>
      <td>18</td><td>0.042</td><td>0.159</td><td>0.032</td><td>0.015</td><td>0.053</td><td>0.116</td><td>0.739</td><td>0.739</td><td>0.739</td><td>0.739</td><td>0.739</td><td>0.739</td>
    </tr>
  </table>
</div>

</div>
<ul style="display: flex; flex-wrap: wrap;">
  <div style="flex: 50%; padding-right: 10px;">
    <li><code>LFT</code>: LEFT FLEXURE TOP REINF AREA</li>
    <li><code>RFT</code>: RIGHT FLEXURE TOP REINF AREA</li>
    <li><code>MFT</code>: MIDSPAN FLEXURE TOP REINF AREA</li>
    <li><code>LFB</code>: LEFT FLEXURE BOTTOM REINF AREA</li>
    <li><code>RFB</code>: RIGHT FLEXURE BOTTOM REINF AREA</li>
    <li><code>MFB</code>: MIDSPAN FLEXURE BOTTOM REINF AREA</li>
  </div>
  <div style="flex: 50%; padding-left: 10px;">
    <li><code>LTT</code>: LEFT TORSION TOP REINF AREA</li>
    <li><code>MTT</code>: MIDSPAN TORSION TOP REINF AREA</li>
    <li><code>RTT</code>: RIGHT TORSION TOP REINF AREA</li>
    <li><code>LTB</code>: LEFT TORSION BOTTOM REINF AREA</li>
    <li><code>MTB</code>: MIDSPAN TORSION BOTTOM REINF AREA</li>
    <li><code>RTB</code>: RIGHT TORSION BOTTOM REINF AREA</li>
  </div>
</ul>


""", unsafe_allow_html=True)
st.header("Choose Unit System")
system = st.selectbox(
    "Select a system:",
    ["FPS", "SI"]
)
if system == "FPS":
  st.header("Bar Designation")
  bar_designation = st.selectbox("Select Bar #)", ['#4', '#5' , '#6' ,'#7' ,'#8' ,'#9','#10'])
  try:
      bar_area = get_bar_area(bar_designation)
      st.success(f"Using {bar_designation} bar with area = {bar_area:.3f} in²")
  except ValueError as e:
      st.error(e)
  results_list = []
elif system == "SI":
    st.header("Bar Designation")
    bar_designation = st.selectbox("Select Bar", ['T8', 'T10' , 'T12' ,'T16' ,'T20' ,'T25','T32'])
    try:
      bar_area = get_bar_areaSI(bar_designation)
      st.success(f"Using {bar_designation} bar with area = {bar_area:.3f} mm²")
    except ValueError as e:
      st.error(e)
    results_list = []
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    unique_name_list = df["Unique Name"].tolist()
    if st.button("Show Calculation Results"):
        
        for i in range(len(unique_name_list)):
            
            b2_to_m2 = df.iloc[i, 1:13].tolist()  # Row 2 (index 1), columns B to M (1:13)"
              
            left_top_long = b2_to_m2[0]
            middle_top_long= b2_to_m2[1]
            right_top_long= b2_to_m2[2]       
            left_bottom_long= b2_to_m2[3] 
            middle_bottom_long= b2_to_m2[4]
            right_bottom_long= b2_to_m2[5]
            left_top_tors = b2_to_m2[6]
            middle_top_tors = b2_to_m2[7]
            right_top_tors = b2_to_m2[8]
            left_bottom_tors = b2_to_m2[9]  
            middle_bottom_tors  = b2_to_m2[10]
            right_bottom_tors = b2_to_m2[11]
            
              
            eff_left_bottom = left_bottom_long + 0.5 * left_bottom_tors
            eff_middle_bottom = middle_bottom_long + 0.5 * middle_bottom_tors
            eff_right_bottom = right_bottom_long + 0.5 * right_bottom_tors

            eff_left_top = left_top_long + 0.5 * left_top_tors
            eff_middle_top = middle_top_long + 0.5 * middle_top_tors
            eff_right_top = right_top_long + 0.5 * right_top_tors

            provided_bottom_effective = max(eff_left_bottom, eff_right_bottom)
            bottom_main_bars = max(math.ceil(provided_bottom_effective / bar_area), 2)
            provided_middle_bottom_area = bottom_main_bars * bar_area
            extra_bottom_area = eff_middle_bottom - provided_middle_bottom_area
            additional_bottom_bars = max(math.ceil(extra_bottom_area / bar_area), 2) if extra_bottom_area > 0 else 0
            total_bottom_bars = bottom_main_bars + additional_bottom_bars

            top_main_bars = max(math.ceil(eff_middle_top / bar_area), 2)
            provided_middle_top_area = top_main_bars * bar_area
            provided_top_effective = max(eff_left_top, eff_right_top)
            extra_top_area = provided_top_effective - provided_middle_top_area
            additional_top_bars = max(math.ceil(extra_top_area / bar_area), 2) if extra_top_area > 0 else 0
            total_top_bars = top_main_bars + additional_top_bars

            results_list.append({
            'BEAM MARK': unique_name_list[i],
            'TOP BARS': top_main_bars,
            'TOP EXTRA': additional_top_bars,
            'BOTTOM BARS': bottom_main_bars,
            'BOTTOM CURTAILED': additional_bottom_bars,
            })

        

        st.header("Calculation Results")


        df = pd.DataFrame(results_list)
        st.dataframe(df)
        def to_excel(df):
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Sheet1')
            return output.getvalue()
        excel_data = to_excel(df)
        st.markdown("### Download the results as an Excel file")
        st.download_button(
        label="📥 Download Excel File",
        data=excel_data,
        file_name="calculated_results.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2025 Sten Design. All rights reserved.</p>", unsafe_allow_html=True)
