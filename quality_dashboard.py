import pandas as pd
import matplotlib.pyplot as plt

def generate_quality_report(batch_id):
    """Generate QA report for sawmill batch"""
    data = {
        'board_id': [f'B{i:03d}' for i in range(1, 21)],
        'grade': ['Select']*5 + ['No.1']*8 + ['No.2']*7,
        'moe_mpa': [12000, 11500, 11000, 10800, 11200, 9500, 9000, 8800, 9200, 8900, 7000, 6800, 6500, 6200, 6000, 5800, 5500, 5200, 5000, 4800]
    }
    df = pd.DataFrame(data)
    
    print(f"--- Quality Report: Batch {batch_id} ---")
    print(df['grade'].value_counts())
    print(f"Avg MOE: {df['moe_mpa'].mean():.0f} MPa")
    
    plt.figure()
    df['grade'].value_counts().plot(kind='bar')
    plt.title(f'Grade Distribution - Batch {batch_id}')
    plt.savefig('grade_distribution.png')
    return df

if __name__ == "__main__":
    generate_quality_report("TM-2024-001")
