from bokeh.plotting import figure, output_file, show
import pandas as pd
#x = [1,2,3,5,6]
#y = [0,2,9,5,9]
#read csv file 
 
df = pd.read_csv('cars.csv')
output_file('index.html')

product = df['product']
ps = df['psell']

#adding plot
p = figure(
    y_range = product,
    plot_width=800,
    plot_height=600,
    title='products by price',
    x_axis_label='psell',
    #y_axis_label='Y axis'
    tools=""
)

#render glyph
#p.line(x, y, legend='tesy', line_width=2)
p.hbar(
    y=product,
    right=ps,
    left=0,
    height=0.4,
    color='red',
    fill_alpha=1
)

show(p)

