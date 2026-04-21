import pandas as pd
import random
import datetime

# ---------- Generate synthetic ITSM dataset ----------
records = []

for i in range(1, 5001):  # 5000 records
    record = {
        'Incident_ID': f'IM{i:07d}',  # Unique ticket ID
        'CI_Name': f'SUB{random.randint(1,999):03d}',  # Random system name
        'CI_Cat': random.choice(['database', 'subapplication', 'network', 'server', 'storage']),
        'CI_Subcat': random.choice(['Web Application', 'Email Service', 'File Server', 'SQL Server', 'Network Switch']),
        'Impact': random.randint(1, 5),
        'Urgency': random.randint(1, 5),
        'Priority': random.randint(1, 5),
        'Category': random.choice(['incident', 'request']),
        'Status': random.choice(['open', 'closed', 'in-progress']),
        'No_of_Reassignments': random.randint(0, 30),
        'Handle_Time_hrs': round(random.uniform(1, 4000), 2),
        'Closure_Code': random.choice(['Resolved', 'Other', 'Pending']),
        'Open_Time': (
            datetime.datetime(2012, 1, 1)
            + datetime.timedelta(days=random.randint(0, 365 * 3))
        ).strftime("%Y-%m-%d %H:%M:%S")
    }
    records.append(record)

# ---------- Create DataFrame ----------
df = pd.DataFrame(records)

# ---------- Save to CSV ----------
df.to_csv("itsm_data.csv", index=False, encoding="utf-8")

print("✅ File created successfully: itsm_data.csv")
print(f"Total Records: {len(df)}")
print("Columns:", list(df.columns))



import pandas as pd
df = pd.read_csv("itsm_data.csv")
print(df.head())
