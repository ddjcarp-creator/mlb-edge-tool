import pandas as pd

def rolling_form(df, window=14):
    df = df.sort_values(["player_name", "game_date"])

    df["is_hr"] = (df["events"] == "home_run").astype(int)

    rolling = df.groupby("player_name").rolling(window, on="game_date").agg({
        "launch_speed": "mean",
        "launch_angle": "mean",
        "is_hr": "sum",
        "barrel": "mean"
    }).reset_index()

    rolling.rename(columns={
        "launch_speed": "ev_rolling",
        "launch_angle": "la_rolling",
        "is_hr": "hr_form",
        "barrel": "barrel_form"
    }, inplace=True)

    return rolling
