# STEPS INVOLVED IN DATA VISUALIZATION
#step 01: IMPORT LIBERIES
import seaborn as sns
import matplotlib.pyplot as plt

# STEP 02: set a theme 
sns.set_theme(style="ticks", color_codes=True)

# STEP 03 : import dataset(YOU CAN IMPORT YOUR OWN DATA)
khasti= sns.load_dataset("titanic")
print(khasti)

# STEP 04: BASIC graph 
# P= sns.countplot(x=" ", y= " ", data= khasti)
# plt.show()           


 
