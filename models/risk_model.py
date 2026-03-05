def calculate_risk(savings_ratio):
    if savings_ratio < 0.1:
        return "High"
    elif savings_ratio < 0.25:
        return "Medium"
    else:
        return "Low"