#!/usr/bin/env python
# coding: utf-8

# In[25]:


import os
import pandas as pd

# Step 1: Set the path to the folder with the CSV files
csv_folder = "C:/Users/User/Desktop/education and life/TMP/Project 1- Transborder frieght data analysis/data1/dot1/2023"  

# Step 2: Get the list of CSV files
csv_files = [file for file in os.listdir(csv_folder) if file.endswith('.csv')]

# Step 3: Read and merge all CSVs
all_data = pd.concat(
    [pd.read_csv(os.path.join(csv_folder, file)) for file in csv_files],
    ignore_index=True
)

# Step 4: Create output path — one directory above `csv_folder`
parent_folder = os.path.dirname(csv_folder)
output_file = os.path.join(parent_folder, "dot1_ytd_2023.csv")

# Step 5: Save the merged DataFrame
all_data.to_csv(output_file, index=False)

print(f"✅ Merged file saved to: {output_file}")


# In[26]:


import os
import pandas as pd

# Step 1: Set the path to the folder with the CSV files
csv_folder = "C:/Users/User/Desktop/education and life/TMP/Project 1- Transborder frieght data analysis/data1/dot1/2024"  # Example: "data/monthly_files"

# Step 2: Get the list of CSV files
csv_files = [file for file in os.listdir(csv_folder) if file.endswith('.csv')]

# Step 3: Read and merge all CSVs
all_data = pd.concat(
    [pd.read_csv(os.path.join(csv_folder, file)) for file in csv_files],
    ignore_index=True
)

# Step 4: Create output path — one directory above `csv_folder`
parent_folder = os.path.dirname(csv_folder)
output_file = os.path.join(parent_folder, "dot1_ytd_2024.csv")

# Step 5: Save the merged DataFrame
all_data.to_csv(output_file, index=False)

print(f"✅ Merged file saved to: {output_file}")


# In[27]:


import os
import pandas as pd

# Step 1: Set the path to the folder with the CSV files
csv_folder = "C:/Users/User/Desktop/education and life/TMP/Project 1- Transborder frieght data analysis/data1/dot2/2023"  # Example: "data/monthly_files"

# Step 2: Get the list of CSV files
csv_files = [file for file in os.listdir(csv_folder) if file.endswith('.csv')]

# Step 3: Read and merge all CSVs
all_data = pd.concat(
    [pd.read_csv(os.path.join(csv_folder, file)) for file in csv_files],
    ignore_index=True
)

# Step 4: Create output path — one directory above `csv_folder`
parent_folder = os.path.dirname(csv_folder)
output_file = os.path.join(parent_folder, "dot2_ytd_2023.csv")

# Step 5: Save the merged DataFrame
all_data.to_csv(output_file, index=False)

print(f"✅ Merged file saved to: {output_file}")


# In[28]:


import os
import pandas as pd

# Step 1: Set the path to the folder with the CSV files
csv_folder = "C:/Users/User/Desktop/education and life/TMP/Project 1- Transborder frieght data analysis/data1/dot2/2024"  # Example: "data/monthly_files"

# Step 2: Get the list of CSV files
csv_files = [file for file in os.listdir(csv_folder) if file.endswith('.csv')]

# Step 3: Read and merge all CSVs
all_data = pd.concat(
    [pd.read_csv(os.path.join(csv_folder, file)) for file in csv_files],
    ignore_index=True
)

# Step 4: Create output path — one directory above `csv_folder`
parent_folder = os.path.dirname(csv_folder)
output_file = os.path.join(parent_folder, "dot2_ytd_2024.csv")

# Step 5: Save the merged DataFrame
all_data.to_csv(output_file, index=False)


print(f"✅ Merged file saved to: {output_file}")


# In[29]:


import os
import pandas as pd

# Step 1: Set the path to the folder with the CSV files
csv_folder = "C:/Users/User/Desktop/education and life/TMP/Project 1- Transborder frieght data analysis/data1/dot3/2023"  # Example: "data/monthly_files"

# Step 2: Get the list of CSV files
csv_files = [file for file in os.listdir(csv_folder) if file.endswith('.csv')]

# Step 3: Read and merge all CSVs
all_data = pd.concat(
    [pd.read_csv(os.path.join(csv_folder, file)) for file in csv_files],
    ignore_index=True
)

# Step 4: Create output path — one directory above `csv_folder`
parent_folder = os.path.dirname(csv_folder)
output_file = os.path.join(parent_folder, "dot3_ytd_2023.csv")

# Step 5: Save the merged DataFrame
all_data.to_csv(output_file, index=False)

print(f"✅ Merged file saved to: {output_file}")


# In[30]:


import os
import pandas as pd

# Step 1: Set the path to the folder with the CSV files
csv_folder = "C:/Users/User/Desktop/education and life/TMP/Project 1- Transborder frieght data analysis/data1/dot3/2024"  # Example: "data/monthly_files"

# Step 2: Get the list of CSV files
csv_files = [file for file in os.listdir(csv_folder) if file.endswith('.csv')]

# Step 3: Read and merge all CSVs
all_data = pd.concat(
    [pd.read_csv(os.path.join(csv_folder, file)) for file in csv_files],
    ignore_index=True
)

# Step 4: Create output path — one directory above `csv_folder`
parent_folder = os.path.dirname(csv_folder)
output_file = os.path.join(parent_folder, "dot3_ytd_2024.csv")

# Step 5: Save the merged DataFrame
all_data.to_csv(output_file, index=False)

print(f"✅ Merged file saved to: {output_file}")


# In[31]:


# Step 1: Set path to the folder containing the CSV files
csv_folder = "C:/Users/User/Desktop/education and life/TMP/Project 1- Transborder frieght data analysis/data1/dot1"  # Example: r"C:\Users\User\Documents\transport_data"

# Step 2: Get all CSV files in the folder
csv_files = [file for file in os.listdir(csv_folder) if file.endswith('.csv')]

# Step 3: Read and merge all CSV files into one DataFrame
df_dot1 = pd.concat(
    [pd.read_csv(os.path.join(csv_folder, file), low_memory=False) for file in csv_files],
    ignore_index=True
)

# Step 4: Preview the merged data
print(f"✅ Merged {len(csv_files)} files into one DataFrame with shape: {df_dot1.shape}")
print(df_dot1.head())


# In[32]:


# Step 1: Set path to the folder containing the CSV files
csv_folder = "C:/Users/User/Desktop/education and life/TMP/Project 1- Transborder frieght data analysis/data1/dot2"  # Example: r"C:\Users\User\Documents\transport_data"

# Step 2: Get all CSV files in the folder
csv_files = [file for file in os.listdir(csv_folder) if file.endswith('.csv')]

# Step 3: Read and merge all CSV files into one DataFrame
df_dot2 = pd.concat(
    [pd.read_csv(os.path.join(csv_folder, file), low_memory=False) for file in csv_files],
    ignore_index=True
)

# Step 4: Preview the merged data
print(f"✅ Merged {len(csv_files)} files into one DataFrame with shape: {df_dot2.shape}")
print(df_dot2.head())


# In[33]:


# Step 1: Set path to the folder containing the CSV files
csv_folder = "C:/Users/User/Desktop/education and life/TMP/Project 1- Transborder frieght data analysis/data1/dot3"  # Example: r"C:\Users\User\Documents\transport_data"

# Step 2: Get all CSV files in the folder
csv_files = [file for file in os.listdir(csv_folder) if file.endswith('.csv')]

# Step 3: Read and merge all CSV files into one DataFrame
df_dot3 = pd.concat(
    [pd.read_csv(os.path.join(csv_folder, file), low_memory=False) for file in csv_files],
    ignore_index=True
)

# Step 4: Preview the merged data
print(f"✅ Merged {len(csv_files)} files into one DataFrame with shape: {df_dot3.shape}")
print(df_dot3.head())


# In[34]:


df_list = [df_dot1, df_dot2, df_dot3]


# In[36]:


#Filling empty rows with N/A

for df in df_list:
    df.fillna("N/A", inplace=True)


# In[24]:


output_folder = "C:/Users/User/Desktop/education and life/TMP/Project 1- Transborder frieght data analysis/power BI data"

df_dot1.to_csv(os.path.join(output_folder, "dot1_cleaned.csv"), index=False)
df_dot2.to_csv(os.path.join(output_folder, "dot2_cleaned.csv"), index=False)
df_dot3.to_csv(os.path.join(output_folder, "dot3_cleaned.csv"), index=False)

